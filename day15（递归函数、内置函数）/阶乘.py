# __author: Lambert
# __date: 2017/8/23 14:34


def factorial(a):
    _sum = 1
    for i in range(1, a + 1):
        _sum = _sum * i
    return _sum


print(factorial(5))


# 递归运算阶乘
def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


print(fact(5))


# 关于递归的特性：
# 1.调用自身函数
# 2.有一个结束条件

# 但凡是递归做的事情循环都能解决
# 递归的效率在很多时候会很低

# 菲波那切数列（for版本）
# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     bf = 0
#     af = 1
#     ret = 0
#     for j in range(n - 1):
#         ret = af + bf
#         bf = af
#         af = ret
#     return ret
#
#
# for k in range(8):
#     print(fibo(k))


# 递归版本
def fe(n):
    if n <= 1:
        return n
    return fe(n - 1) + fe(n - 2)


print(fe(4))  # 从0位开始算

for k in range(8):
    print(fe(k))
