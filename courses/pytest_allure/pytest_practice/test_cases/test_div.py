import allure
import pytest

from ..base_func.base import Base
from ..base_func.get_data import *


@allure.feature('add and division')
class TestDiv(Base):
    add_P0_data, add_P0_ids = get_data('data.yml', 'add', 'P0')
    add_P1_data, add_P1_ids = get_data('data.yml', 'add', 'P1')
    @allure.story('P0 div')
    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,expected', add_P0_data, ids=add_P0_ids)
    def test_div1(self, a, b, expected):
        with allure.step('get result'):
            result = self.cal.div_func(a, b)
        with allure.step('get assertion'):
            assert expected == result

    @allure.story('P1 div')
    @pytest.mark.P1
    @pytest.mark.flaky(reruns=5, reruns_delay=2)
    @pytest.mark.parametrize('a,b,expected', add_P1_data, ids=add_P1_ids)
    def test_div2(self, a, b, expected):
        with pytest.raises(eval(expected)) as e:
            with allure.step('get result'):
                result = self.cal.div_func(a, b)
            with allure.step('get assertion'):
                assert expected == result