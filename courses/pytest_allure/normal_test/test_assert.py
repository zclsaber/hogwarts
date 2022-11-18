import pytest


def test_a():
    assert False

@pytest.mark.corr
def test_b():
    a = 1
    b = 2
    expect = 3
    assert a + b == expect
    print('bbb')

@pytest.mark.err
def test_c():
    assert 'abc' in 'abcdef'
    print('ccc')


import sys
def test_d():
    assert ('linux' in sys.platform), "This is not a linux system"