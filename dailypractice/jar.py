"""
我们混合了一些美味的果汁。我们可以添加一定数量的一些成分。有时我们会倒一点果汁。然后我们想知道我们的果汁有哪些浓度。

例子：

你拿一个空罐子装果汁
每当罐子是空的，浓度总是 0
现在你添加 200 单位的苹果汁
然后你添加 200 单位的香蕉汁
现在苹果汁的浓度是0.5（50%）
然后你倒出 200 个单位
苹果汁的浓度还是50%
然后你再加入 200 单位的苹果汁
现在苹果汁的浓度是0.75，而香蕉汁的浓度只有0.25（300单位苹果汁+100单位香蕉汁）
"""


class Jar:

    def __init__(self):
        self.bottle = {'apple': 0, 'orange': 0}
        self.ml = 0

    def add(self, amount, kind):
        self.bottle[kind] += amount
        self.ml = self.bottle['apple'] + self.bottle['orange']
        # return self.bottle

    def pour_out(self, amount):
        self.ml = self.bottle['apple'] + self.bottle['orange']
        self.bottle['apple'] = (self.ml - amount) / self.ml * self.bottle['apple']
        self.bottle['orange'] = (self.ml - amount) / self.ml * self.bottle['orange']
        self.ml -= amount
        # return self.ml

    def get_total_amount(self):
        return self.ml

    def get_concentration(self, kind):
        conc = self.bottle[kind] / self.ml
        return '{:.0%}'.format(conc)

juice = Jar()
juice.add(800, 'apple')
juice.add(200, 'orange')
juice.pour_out(100)
print(juice.bottle)
# print(juice.ml)
print(juice.get_total_amount())
juice.add(500, 'apple')
print(juice.get_concentration('apple'))
