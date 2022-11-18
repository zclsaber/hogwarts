import pytest

search_list = ['appium', 'selenium', 'pytest']
search_list_para = ['appium', 'selenium', 'abcd']
response = ['101', '202', '303']

@pytest.mark.parametrize('name', search_list_para)
def test_parameterize(name):
    assert name in search_list


@pytest.mark.parametrize('input_val, expect', [('3 + 5', 7), ('1 * 2', 2)], ids=['1', '2'])
def test_multi_para(input_val, expect):
    assert eval(input_val) == expect


@pytest.mark.parametrize('wd', search_list, ids=['1', '2', '3'])
@pytest.mark.parametrize('code', response, ids=['a', 'b', 'c'])
def test_decal(wd, code):
    print(f"wd: {wd}, code:{code}")