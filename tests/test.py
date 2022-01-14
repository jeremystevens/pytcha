"""Pytest"""

# test_show.py
import pytest


def test_sample1():
    """test 1"""
    assert True


def test_sample2():
    """test 2."""
    assert [1, 2, 3] != [3, 2, 1]


@pytest.mark.xfail()
def test_sample3():
    """test 3."""
    assert False


@pytest.mark.xfail()
def test_sample4():
    """test 4."""
    assert True
