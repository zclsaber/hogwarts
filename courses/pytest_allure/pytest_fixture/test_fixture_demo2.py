import pytest


@pytest.fixture(scope='module')
def login():
    print('login!')


def test_search(login):
    print('search')


def test_cart(login):
    print('check cart')


def test_order(login):
    print('order')