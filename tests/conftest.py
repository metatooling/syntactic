"""Pytest setup."""

import subprocess

import pytest

import tests


@pytest.fixture(autouse=True)
def python(virtualenv):
    """Install into a separate virtualenv to get the pth file."""
    subprocess.check_call(
        [str(virtualenv.python), "-m", "pip", "install", str(tests.helpers.PROJECT_DIR)]
    )
