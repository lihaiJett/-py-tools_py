import numpy

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 计算两直线的交点
# p1p2为一条线，p3p4为一条线
def c(p1, p2, p3, p4):
    x = -(
        -p3.x * p2.x * p1.y + p2.x * p4.x * p1.y + p1.x * p4.x * p3.y - p2.x * p4.x * p3.y + p1.x * p3.x * p2.y - p1.x * p4.x * p2.y - p1.x * p3.x * p4.y + p3.x * p2.x * p4.y) / (
            p3.x * p1.y - p4.y * p1.y - p1.x * p3.y + p2.x * p3.y - p3.x * p2.y + p4.x * p2.y + p1.x * p4.y - p2.x * p4.y)
    y = -(-(-p2.x * p1.y + p1.x * p2.y) * (p3.y - p4.y) + (p1.y - p2.y) * (-p4.x * p3.y + p3.x * p4.y)) / (
        (-p3.x + p4.x) * (p1.y - p2.y) - (-p1.x + p2.x) * (p3.y - p4.y))
    return P(x, y)


# 判断两条直线是否平行
def isParallel(p1, p2, p3, p4):
    return (p1.x - p2.x) / (p1.y - p2.y) == (p3.x - p4.x) / (p3.y - p4.y)

# 判断是否共线
# def isCollinear(p1,p2,p3,p4):



# 平行时返回端点相交的坐标
# 交点数量为0个或2个
# def intersectionInParallel(p1, p2, p3, p4):
    # if()


def insideLineWhenParallel(p, lp1, lp2):
    return (p.x >= min(lp1.x, lp2.x)) and (p.x <= max(lp1.x, lp2.x))


# a = c(P(4, 0), P(-2, 9), P(5, 8), P(-1, -2))
a = c(P(0, 0), P(0, 9), P(0, 8), P(0, 2))

print(str(a.x) + "," + str(a.y))
