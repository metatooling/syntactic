"""Support for custom syntax."""

import codecs
import encodings
import functools
import importlib
import io
import re
import typing as t

import importlib_metadata


UTF8 = encodings.search_function("utf8")

MAGIC_PACKAGE_NAME = "__syntax__"


def get_transformer_pairs(source: str) -> t.List[t.Tuple[str, str]]:
    """Return the module and function names of requested transformers.

    Searches for ``from __syntax__ import ...``.

    """
    module_function_pairs: t.List[t.Tuple[str, str]] = []
    for line in source.splitlines():
        match = re.fullmatch(
            fr"from\s+([\w\s.]+{MAGIC_PACKAGE_NAME})\s+import\s+(\w.*?)$", line
        )
        if match:
            module_name = match.group(1)
            function_names = [name.strip() for name in match.group(2).split(",")]
            for function_name in function_names:
                module_function_pairs.append((module_name, function_name))

    return module_function_pairs


def decode(source_bytes: bytes, errors="strict"):
    """Decode the utf-8 input and transform it with the named transformers."""

    source, length = UTF8.decode(source_bytes, errors)
    transformer_pairs = get_transformer_pairs(source)

    for module_name, function_name in transformer_pairs:
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        source = function(source)

    return source, length


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    """A buffered incremental decoder for custom syntax."""

    def _buffer_decode(
        self, input, errors, final
    ):  # pylint: disable=bad-option-value,redefined-builtin
        if final:
            return decode(input, errors)
        return "", 0


class StreamReader(UTF8.streamreader):  # type: ignore
    """decode is deferred to support better error messages"""

    _stream = None
    _decoded = False

    @property
    def stream(self):
        """Get the stream."""
        if not self._decoded:
            text, _ = decode(self._stream.read())
            self._stream = io.BytesIO(text.encode("UTF-8"))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Set the stream."""
        self._stream = stream
        self._decoded = False


CODEC_MAP = {
    ci.name: ci  # pylint: disable=no-member
    for ci in [
        codecs.CodecInfo(  # type:ignore
            name="syntactic",
            encode=UTF8.encode,
            decode=decode,
            incrementalencoder=UTF8.incrementalencoder,
            incrementaldecoder=IncrementalDecoder,
            streamreader=StreamReader,
            streamwriter=UTF8.streamwriter,
        )
    ]
}


def main():
    """Register the codec with Python."""
    codecs.register(CODEC_MAP.get)
