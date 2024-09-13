# 模块级别，整个模块只执行一次
def setup_module():
    print('setup module')


def teardown_module():
    print('teardown module')


def test_case1():
    print('test_case1')


def test_case2():
    print('test_case2')


def setup_function():
    print('setup fucntion')


def teardown_function():
    print('teardwon function')


class TestDemo:
    # 执行类 前后分别执行 setup_class 和 teardown_class
    def setup_class(self):
        print('setup class')

    def teardown_class(self):
        print('teardown class')

    # 执行每一个用例都要执行 setup teardown
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_demo1(self):
        print('test demo1')

    def test_demo2(self):
        print('test demo2')

    def test_demo3(self):
        print('test demo3')

