# __author: Lambert
# __date: 2017/8/30 10:16


# 生成器都是迭代器，迭代器不一定是生成器
l = [1, 2, 3]
d = iter(l)  # 等于l.__iter__()
print(d)  # <list_iterator object at 0x000002863F378B70>
print(next(d))

# 什么是迭代器？
# 满足两个条件：1.有iter方法2.有next方法

# for循环内部三件事:
# 1.调用可迭代对象的iter方法转为一个迭代器对象
# 2.不断调用迭代器对象的next()方法
# 3.处理StopIteration
# for i in [1, 2, 3]:
#     iter([1, 2, 3])
from collections import Iterable, Iterator

li = [1, 2, 3, 4, 5]
f = iter(li)
print(isinstance(li, list))  # True
print(isinstance(li, Iterable))  # True
print(isinstance(li, Iterator))  # False
print(isinstance(f, Iterator))  # True
