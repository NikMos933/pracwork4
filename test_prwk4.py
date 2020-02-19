from prwk4 import check
from prwk4 import pagecheck
import pytest


def test_check_1():
    assert check(4) is True


def test_check_2():
    assert check('as3da241s') is False


def test_pagecheck_1():
    assert pagecheck('< 3 >') is True


def test_pagecheck_2():
    assert pagecheck('<>3') is False



