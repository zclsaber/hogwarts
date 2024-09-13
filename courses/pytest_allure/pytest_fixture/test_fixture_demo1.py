import pytest


@pytest.fixture()
def login():
    print('login!')


def test_search():
    print('search')


def test_cart(login):
    print('check cart')


def test_order(login):
    print('order')