# __author: Lambert
# __date: 2017/9/18 17:51
# __author: Lambert
# __date: 2017/9/18 15:53
import time
import threading

begin = time.time()


def add(n):
    sum = 0
    for i in range(n):
        sum += i
    print(i)


def bar(n):
    sum = 0
    for i in range(n):
        sum += i
    print(i)


t1 = threading.Thread(target=add, args=(100000000,))
t1.setDaemon(True)  # 设置守护线程，主线程结束守护线程也结束
t1.start()
t2 = threading.Thread(target=bar, args=(100000000,))
t2.start()

# add(100000000)
# bar(100000000)
end = time.time()
print(end - begin)
# 由于切换线程消耗太多资源，故进行多线程运算和串行运算消耗时间差不多
# 由于python的GIL（全局解释器锁）故线程不能同时进入cpu
