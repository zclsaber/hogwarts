import pytest


@pytest.fixture(params=['one', 'two', 'three'])
def signin(request):
    print(f'{request.param} sign in!')


def test_search(signin):
    print('search')


def test_cart(signin):
    print('check cart')


def test_order(login):
    print('order')