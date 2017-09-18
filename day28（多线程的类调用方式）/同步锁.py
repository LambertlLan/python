# __author: Lambert
# __date: 2017/9/18 22:55
import threading, time

num = 100

# 在线程进行计算式时间超出规定时间被强制退出，交给下一个线程，故会出现未进行的运算
# 此时需要加同步锁
lock = threading.Lock()


def foo():
    global num

    lock.acquire()
    temp = num
    time.sleep(0.01)
    num = temp - 1
    lock.release()


threadList = []

for i in range(100):
    t = threading.Thread(target=foo)
    t.start()
    threadList.append(t)

for i in threadList:
    i.join()

print('number:', num)
