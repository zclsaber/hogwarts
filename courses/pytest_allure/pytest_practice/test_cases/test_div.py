import pytest

from ..base_func.base import Base


class TestDiv(Base):
    @pytest.mark.P0
    @pytest.mark.parametrize('a,b,expected', [[1, 1, 1], [-0.01, -0.02, 0.5], [-0.01, 0.02, -0.5],
                                              [10, 0.02, 500]], ids=['整数int', '浮点float', '负浮点minus float', '整浮int float'])
    def test_div1(self, a, b, expected):
        result = self.cal.div_func(a, b)
        assert expected == result

    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,expected', [[99, 0, 'ZeroDivisionError']], ids=['被除数为0'])
    def test_div2(self, a, b, expected):
        with pytest.raises(eval(expected)) as e:
            result = self.cal.div_func(a, b)