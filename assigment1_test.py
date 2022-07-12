from unittest import mock
from unittest.mock import patch
from assigment1 import show_square
import pytest

DATA = [
    (
        1,
        {
            "check": {"key": "value"},
            "input": [
                {"number": 1},
                {"number": 2},
                {"number": 3},
                {"number": 4},
            ],
        },
        True,
    ),
    (
        2,
        {
            "check": {},
            "input": [
                {"number": 1},
                {"number": 2},
                {"number": 3},
                {"number": 4},
            ],
        },
        False,
    ),
]


@pytest.mark.parametrize("case,data,expect", DATA)
def test_show_square(case, data, expect):
    patch("assigment1.get_data", return_value=data.get("check")).start()
    assert show_square() == expect
