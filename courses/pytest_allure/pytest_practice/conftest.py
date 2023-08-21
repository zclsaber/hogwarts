from typing import List
from .base_func.log_util import logger
import pytest


@pytest.fixture(scope='module')
def login():
    print('login!')


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption(parser):
    mygroup = parser.getgroup('hogwarts')
    mygroup.addoption('--env',
                      default='test',
                      dest='env',
                      help='set up own env'
                      )

@pytest.fixture(scope='session')
def addoption(request):
    return request.config.getoption('--env', default='test')


@pytest.fixture(autouse=True, scope='session')
def clear_data():
    yield
    logger.info('clear all data...')