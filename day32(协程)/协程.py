# __author: Lambert
# __date: 2017/9/21 17:40
import gevent, time


def foo():
    print('Running in foo', time.time())
    gevent.sleep(1)
    print('Switch to Foo', time.ctime())


def bar():
    print('Running in bar', time.time())
    gevent.sleep(2)
    print('Switch to bar', time.ctime())


start = time.time()
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
end = time.time()
print(end - start)
