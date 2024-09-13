import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print('This is a testing env')
            print(env)
        elif 'dev' in env:
            print('This is a develop env')

    @pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')))
    def test_demo1(self, env):
        if 'test' in env:
            print('This is a testing env')
            print('Testing env ip is:', env['test'])
        elif 'dev' in env:
            print('This is a develop env')