"""Tests for syntactic."""

import subprocess

import pytest
import tests.helpers


@pytest.mark.parametrize(
    ["path"],
    (
        (path,)
        for path in tests.helpers.PROJECT_DIR.joinpath("docs/examples/").rglob("*.py")
    ),
)
def test_example(virtualenv, path):
    """After tranforming the syntax, Python gives the expected results on stdout."""
    expected = tests.helpers.parse_expected(path)
    output = subprocess.check_output([str(virtualenv.python), str(path)]).decode()
    assert output == expected
