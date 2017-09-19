# __author: Lambert
# __date: 2017/9/19 10:14
import threading, time

lock = threading.RLock()


class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def doA(self):
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        lock.release()
        lock.release()

    def doB(self):
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, "gotlock", time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == '__main__':
    threadList = []
    for i in range(5):
        threadList.append(Mythread('Thread-%s' % i))

    for j in threadList:
        j.start()

    for j in threadList:
        j.join()

# 递归锁，内部有一个计数器，存的字典
