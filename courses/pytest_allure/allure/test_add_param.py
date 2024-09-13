import pytest
from courses.pytest_allure.pytest_practice.base_func.base import Base
import allure
from courses.pytest_allure.pytest_practice.base_func.log_util import logger

def teardwon_module():
    print('全部结束')

# 需要安装 java， allure， allure-pytest
@allure.feature('相加功能')
class TestAdd(Base):

    # 当测试步骤都一样，只有数据不一样时，就可以用参数化
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('P0 用例')
    @allure.story('相加P0用例')
    @pytest.mark.P0
    @pytest.mark.parametrize('a, b, expected', [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02], [98.99, 99, 197.99],
                                                [99, 98.99, 197.99], [-98.99, -99, -197.99]])
    def test_add_case1(self, a, b, expected):
        logger.info(f'输入数据：{a}, {b}, 期望结果是 {expected}')
        with allure.step('step1: 相加操作'):
            result = self.cal.add_func(a, b)
        logger.info((f'实际结果为 {result}'))
        allure.attach.file(r'C:\Users\fu\Downloads\图片1.png', name='计算完成截图')
        with allure.step('step2: 断言操作'):
            assert result == expected

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('相加P1用例')
    @pytest.mark.P1
    @pytest.mark.parametrize('a, b, expected', [[99.01, 0, '参数大小超出范围'], [-99.01, -1, '参数大小超出范围'],
                                                [2, 99.01, '参数大小超出范围'], [1, -99.01, '参数大小超出范围']])
    def test_add_case8(self, a, b, expected):
        logger.info(f'输入数据：{a}, {b}, 期望结果是 {expected}')
        with allure.step('step1: 相加操作'):
            result = self.cal.add_func(a, b)
        logger.info((f'实际结果为 {result}'))
        with allure.step('step2: 断言操作'):
            assert result == expected

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('相加P2用例')
    @allure.link('https://www.baidu.com', name='百度')
    @pytest.mark.P2
    @pytest.mark.parametrize('a, b, expected', [["文", 9.3, "TypeError"]], ids=['exception'])
    def test_add_case12(self, a, b, expected):
        # try:
        #     result = self.cal.add_func('文', 9.3)
        # except TypeError as e:
        #     print(e)
        # # assert result == '参数大小超出范围'
        logger.info(f'输入数据：{a}, {b}, 期望结果是 {expected}')
        with allure.step('step1: 相加操作'):
            with pytest.raises(eval(expected)) as e:
                result = self.cal.add_func(a, b)
                logger.info((f'实际结果为 {result}'))