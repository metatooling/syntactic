"""Support for custom syntax."""

import codecs
import encodings
import functools
import importlib
import io
import re
import typing as t

import importlib_metadata


utf_8 = encodings.search_function("utf8")

MAGIC_PACKAGE_NAME = "__syntax__"


def get_transformer_names(source: str) -> t.List[str]:
    """Return the names of requested transformers.

    Searches for ``from __syntax__ import ...``.

    """
    module_names: t.List[str] = []
    for line in source.splitlines():

        match = re.fullmatch(
            fr"\s*from\s+{MAGIC_PACKAGE_NAME}\s+import\s+(\w+)\s*", line
        )
        if match:
            module_names.extend(match.groups())

    return module_names


@functools.lru_cache(None)
def gather_transformers():
    """Gather transformers from plugins."""

    transformers: t.Dict[str, t.Callable[[str], str]] = {}
    entry_points = importlib_metadata.entry_points()["syntactic.transformers"]

    for entry_point in entry_points:
        module_name, _, name_in_module = entry_point.value.partition(":")

        module = importlib.import_module(module_name)
        transformers[entry_point.name.strip()] = getattr(module, name_in_module)

    return transformers


def decode(b, errors="strict"):
    """Decode the utf-8 input and transform it with the named transformers."""
    transformers = gather_transformers()

    source, length = utf_8.decode(b, errors)
    transformer_names = get_transformer_names(source)

    for transformer_name in transformer_names:

        source = transformers[transformer_name](source)
    return source, length


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    def _buffer_decode(self, input, errors, final):  # pragma: no cover
        if final:
            return decode(input, errors)
        return "", 0


class StreamReader(utf_8.streamreader):  # type: ignore
    """decode is deferred to support better error messages"""

    _stream = None
    _decoded = False

    @property
    def stream(self):
        if not self._decoded:
            text, _ = decode(self._stream.read())
            self._stream = io.BytesIO(text.encode("UTF-8"))
            self._decoded = True
        return self._stream

    @stream.setter
    def stream(self, stream):
        self._stream = stream
        self._decoded = False


codec_map = {
    ci.name: ci
    for ci in [
        codecs.CodecInfo(
            name="syntactic",
            encode=utf_8.encode,
            decode=decode,
            incrementalencoder=utf_8.incrementalencoder,
            incrementaldecoder=IncrementalDecoder,
            streamreader=StreamReader,
            streamwriter=utf_8.streamwriter,
        )
    ]
}


def main():
    codecs.register(codec_map.get)
