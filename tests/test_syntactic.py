"""Tests for syntactic."""

import subprocess

import pytest
import tests.helpers


@pytest.mark.parametrize(
    "filename,expected", [("bangbang.py", "2\nhello\n4\n"), ("lambdas.py", "1\n")]
)
def test_bangbang(virtualenv, filename, expected):
    """The bangbang script turns !! into a print() call."""
    subprocess.check_call(
        [virtualenv.python, "-m", "pip", "install", str(tests.helpers.PROJECT_DIR)]
    )

    output = subprocess.check_output(
        [
            virtualenv.python,
            str(
                tests.helpers.PROJECT_DIR.joinpath("tests/examples/").joinpath(filename)
            ),
        ]
    ).decode()
    assert output == expected
