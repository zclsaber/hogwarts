import pytest
import csv
from .operator import add_func

def get_csv():
    with open('./params.csv', 'r') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    return data


class TestCSV:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add_func(self, x, y, expected):
        assert add_func(int(x), int(y)) == int(expected)