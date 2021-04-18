from parsing import cli
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [(["--string",
                            "wesdrttt"],
                           5),
                          (["--string",
                            "wesdrttt",
                            "--file",
                            "testfile.txt"],
                           4)])
def test_arg(test_input, expected):
    assert cli.main_parse(test_input) == expected
