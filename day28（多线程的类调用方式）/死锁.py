# __author: Lambert
# __date: 2017/9/19 10:14
import threading, time

lockA = threading.Lock()
lockB = threading.Lock()


class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def doA(self):
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        time.sleep(3)
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        lockA.release()
        lockB.release()

    def doB(self):
        lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        time.sleep(3)
        lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        lockB.release()
        lockA.release()

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

# 输出结果:
# Thread-0 gotlockA Tue Sep 19 10:27:32 2017
# Thread-0 gotlockB Tue Sep 19 10:27:35 2017
# Thread-0 gotlockB Tue Sep 19 10:27:35 2017
# Thread-1 gotlockA Tue Sep 19 10:27:35 2017 程序执行到这个位置时，线程0获得A锁，线程1获得B锁，两个线程需要等待对方释放线程才能继续执行，所以双方都在等待，所以会造成死锁现象
