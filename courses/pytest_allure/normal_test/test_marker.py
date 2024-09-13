import pytest


@pytest.mark.str
def test_str():
    print('type str')


@pytest.mark.int
def test_int():
    print('type int')


@pytest.mark.float
def test_float():
    print('type float')