# __author: Lambert
# __date: 2017/8/24 11:16
import time


# 需求：给foo函数和bar函数添加计算时间功能，为了业务员调用不变，不改变foo函数的函数名
# 遵守开放封闭原则，对拓展开放，对修改封闭
def foo():
    print('foo')


def bar():
    print('bar')


# 使用闭包，完成装饰器，不会改变调用方式
def show_time(func):
    def inner():
        start = time.time()
        func()
        time.sleep(2)
        end = time.time()
        print('time:%s' % (end - start))

    return inner


foo = show_time(foo)
bar = show_time(bar)

foo()
bar()

# 不使用装饰器的效果
# def foo():
#     print('foo')
#
#
# def show_time(func):
#     start = time.time()
#     func()
#     time.sleep(2)
#     end = time.time()
#     print('time:%s' % (end - start))
#
#
# foo = show_time(foo)
