import pytest
import json
from .operator import add_func

def get_json():
    with open('./params.json', 'r') as file:
        data = json.loads(file.read())
        return list(data.values())

class TestJson:

    @pytest.mark.parametrize('x,y,expected', get_json())
    def test_add_func(self, x, y, expected):
        assert add_func(x, y) == expected