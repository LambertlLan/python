import time


def foo():
    print('foo')


def show_time(func):
    start = time.time()
    func()
    time.sleep(2)
    end = time.time()
    print('time:%s' % (end - start))


foo = show_time(foo)
