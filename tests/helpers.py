"""Test helpers."""

import pathlib


TESTS_DIR = pathlib.Path(__file__).parent
PROJECT_DIR = TESTS_DIR.parent


def parse_expected(path: pathlib.Path) -> str:
    """Examples are written according to this format.

    <code>
    # ---
    # <expected>
    # <expected>
    # <expected>

    Return the expected lines.
    """
    _code, _separator, expected = path.read_text().partition("# ---\n")
    return "\n".join(line[2:] for line in expected.splitlines()) + "\n"
