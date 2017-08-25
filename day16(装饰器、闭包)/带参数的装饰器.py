# __author: Lambert
# __date: 2017/8/25 9:48
import time


def show_time(f):
    def inner(x, y):
        start = time.time()
        f(x, y)
        end = time.time()
        print(end - start)

    return inner


@show_time  # 等于下方的add = show_time(add)
def add(x, y):
    print(x + y)
    time.sleep(2)


# add = show_time(add)

add(1, 2)


# showtime添加参数
def logger(flag=''):
    def show_time2(f):
        def inner(x, y):
            start = time.time()
            f(x, y)
            end = time.time()
            print(end - start)
            if flag:
                print('日志记录')

        return inner

    return show_time2


@logger('true')  # 在show_time外再添加一层就能继续添加参数，通过true控制是否打印日志
def add2(x, y):
    print(x + y)
    time.sleep(2)


@logger()
def bar(x, y):
    print(x + y)
    time.sleep(3)


add2(1, 2)
bar(1, 2)
