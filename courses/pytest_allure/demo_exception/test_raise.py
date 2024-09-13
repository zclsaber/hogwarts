import pytest


def test_raises1():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ValueError("value must be 0 or None")


def test_raises2():
    with pytest.raises(ValueError) as exc_info:
        raise ValueError("value must be 111")
    assert exc_info.type is ValueError
    assert exc_info.value.args[0] == "value must be 111"


def test_raises3():
    with pytest.raises(ValueError, match='must be 0 or None'):
        raise ZeroDivisionError("value is 0")


def test_raises4():
    with pytest.raises((ZeroDivisionError, ValueError), match='value is 0'):
        raise ZeroDivisionError("value is 0")