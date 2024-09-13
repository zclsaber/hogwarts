import openpyxl
import pytest
from .operator import add_func

def get_excel():
    book = openpyxl.load_workbook('./params.xlsx')
    sheet = book.active
    cells = sheet['A1':'C3']
    vals = []
    for row in cells:
        data = []
        for cell in row:
            data.append(cell.value)
        vals.append(data)
    return vals

class TestExcel:

    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add_func(self, x, y, expected):
        assert add_func(int(x), int(y)) == int(expected)