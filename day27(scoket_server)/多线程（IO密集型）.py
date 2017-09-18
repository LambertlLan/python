# __author: Lambert
# __date: 2017/9/18 14:55
import time
import threading


def foo(n):
    print('foo%s' % n)
    time.sleep(1)


def bar(n):
    print('bar%s' % n)
    time.sleep(2)


print('-------------------main-------------------')
t1 = threading.Thread(target=foo, args=(1,))  # 建立线程对象
t2 = threading.Thread(target=foo, args=(2,))

t1.start()  # 启动线程
t2.start()
# 用time.sleep()模拟IO阻塞，在阻塞时进行其他运算节约时间
