# __author: Lambert
# __date: 2017/8/23 17:23
# print(all([1, 2, 3, '']))  # 如果列表里面有空元素返回False
# print(eval('1+2*3'))  # 将字符串转成对象格式
# 迭代器
str = ['a', 'b', 'c', 'd']


def funl(s):
    if s != 'a':
        return s


def fun2(s):
    return s + 'asdg'


# ret = filter(funl, str)  # ret被处理为迭代器<filter object at 0x000002CAFC0EA668> 为一个迭代器对象,filter只能做筛选，不然会不做任何操作
ret = map(fun2, str)  # ret被处理为迭代器<map object at 0x00000143A0DB5240> ['aasdg', 'basdg', 'casdg', 'dasdg']
print(ret)  #
print(list(ret))

from functools import reduce


def add1(x, y):
    return x + y


print(reduce(add1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 先取前两位放入add1中，拿到返回值3，再取第三位一次相加。返回结果就是一个值

# 匿名函数
add2 = lambda a, b: a + b  # 用于简单函数
# 则上面可改写为
print(reduce(lambda a, b: a * b, range(1, 10)))
