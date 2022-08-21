"""
【每日一题20220817】干杯，啤酒金字塔
有一天你贡献了一个非常好的idea，老板给了你一笔奖金。为了庆祝，你把你的朋友们带到可怕的潜水酒吧，并使用奖金购买和建造最大的三维啤酒罐金字塔。然后与朋友们进入狂欢。
啤酒罐金字塔建造的规则是：顶层1罐，第二层4罐，下一层9罐，下一层16罐，25罐…
完成 beeramid 函数以返回您可以制作的啤酒罐完整金字塔的层数，给定以下参数：
您的奖金 bonus，以及啤酒的价格 price
例如：
beeramid(1500, 2)  # should === 12
beeramid(5000, 3) # should === 16
"""


def beeramid(bonus: float, price: float) -> int:
    count = bonus // price
    floor = 0
    cost = 0
    while True:
        floor += 1
        cost += floor ** 2
        if cost > count:
            return floor - 1


floors = beeramid(3, 2)
print(floors)

print(floors.__doc__)