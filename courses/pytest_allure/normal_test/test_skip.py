import pytest

@pytest.mark.skip(reason='code is unavailable')
def test_skip():
    assert False

# 使用语句
def check_in():
    return False

def test_func():
    print('start')
    if not check_in():
        pytest.skip('unsupported configuration')
    print('end')


if __name__=='__main__':
    pytest.main(['test_sample.py', '-vs'])