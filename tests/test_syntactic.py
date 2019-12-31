import subprocess

import pytest
import tests.helpers


@pytest.mark.parametrize("filename", ["bangbang.py"])
def test_bangbang(virtualenv, filename):
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
    assert output == "2\nhello\n4\n"
