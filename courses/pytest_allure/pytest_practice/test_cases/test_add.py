import pytest
from ..base_func.calculator import Calculator
from ..base_func.base import Base

def teardwon_module():
    print('全部结束')

class TestAdd(Base):

    @pytest.mark.P0
    def test_add_case1(self):
        result = self.cal.add_func(1, 2)
        assert result == 3

    @pytest.mark.P0
    def test_add_case2(self):
        result = self.cal.add_func(-0.01, 0.02)
        assert result == 0.01

    @pytest.mark.P0
    def test_add_case3(self):
        result = self.cal.add_func(10, 0.02)
        assert result == 10.02

    @pytest.mark.P1
    def test_add_case4(self):
        result = self.cal.add_func(98.99, 99)
        assert result == 197.99

    @pytest.mark.P1
    def test_add_case5(self):
        result = self.cal.add_func(99, 98.99)
        assert result == 197.99

    @pytest.mark.P1
    def test_add_case6(self):
        result = self.cal.add_func(-98.99, -99)
        assert result == -197.99

    @pytest.mark.P1
    def test_add_case7(self):
        result = self.cal.add_func(-99, -98.99)
        assert result == -197.99

    @pytest.mark.P1
    def test_add_case8(self):
        result = self.cal.add_func(99.01, 0)
        assert result == '参数大小超出范围'

    @pytest.mark.P1
    def test_add_case9(self):
        result = self.cal.add_func(-99.01, -1)
        assert result == '参数大小超出范围'

    @pytest.mark.P1
    def test_add_case10(self):
        result = self.cal.add_func(2, 99.01)
        assert result == '参数大小超出范围'

    @pytest.mark.P1
    def test_add_case11(self):
        result = self.cal.add_func(1, -99.01)
        assert result == '参数大小超出范围'

    @pytest.mark.P1
    def test_add_case12(self):
        # try:
        #     result = self.cal.add_func('文', 9.3)
        # except TypeError as e:
        #     print(e)
        # # assert result == '参数大小超出范围'
        with pytest.raises(TypeError) as e:
            result = self.cal.add_func('文', 9.3)