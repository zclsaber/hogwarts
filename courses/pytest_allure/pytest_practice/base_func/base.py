from .calculator import Calculator
from .log_util import logger


class Base:
    def setup_class(self):
        # 没有特殊需求，在类里面实例化一次就够用了，所以可以提到类里进行
        logger.info('实例化 calc 对象')
        self.cal = Calculator()

    def teardown_class(self):
        logger.info('结束测试')

    def setup(self):
        logger.info('开始计算')

    def teardown(self):
        logger.info('结束计算')
