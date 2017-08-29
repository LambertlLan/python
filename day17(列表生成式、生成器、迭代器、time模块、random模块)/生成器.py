# __author: Lambert
# __date: 2017/8/29 22:30
# s = (x for x in range(5))  # 不占用内存，需要用的时候再生成
# print(s)  # <generator object <genexpr> at 0x0000027C1674B360>
# print(next(s))  # 等价于__next__(),但__next__()是内置特殊方法 in py2:s.next()
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # StopIteration迭代结束


# 生成器就是一个可迭代对象（Iterable）
# l = (x for x in range(1000))
# for i in l:  # 在没有引用是python的垃圾回收机制会将其回收，所以不占用内存
#     print(i)


# 生成器只有两种生成方式
# 1. （x for x in range(10)）
# 2. yield


def foo():  # 只要有yield则为一个生成器函数
    print('ok')
    yield 1
    print('ok2')
    yield 2


g = foo()
# print(g)  # <generator object foo at 0x00000267F398B3B8>
# next(g)
# next(g)
for i in g:
    print(i)  # 执行完每一步之后将yield的值返回


# 什么是可迭代对象
# range(10).__iter__() 内部有iter方法的都是可迭代对象
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         yield b
#         a, b = b, a + b  # 先执行右侧及先算a+b再赋值
#         n += 1
#
# fib(20)
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         yield b
#         a, b = b, a + b  # 先执行右侧及先算a+b再赋值
#         n += 1
#
#
# g = fib(20)
# next(g)
# next(g)
# next(g)
# next(g)
# next(g)
