class Calculator:

    def add_func(self, a, b):
        if a > 99 or a < -99 or b >99 or b < -99:
            print('请输入范围为【-99， 99】的整数或浮点数')
            return '参数大小超出范围'
        return a + b

    def div_func(self, a, b):
        if a > 99 or a < -99 or b >99 or b < -99:
            print('请输入范围为【-99， 99】的整数或浮点数')
            return '参数大小超出范围'
        return a / b