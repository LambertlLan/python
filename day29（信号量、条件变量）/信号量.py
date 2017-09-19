# __author: Lambert
# __date: 2017/9/19 11:20
import threading, time


class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(2)
            semaphore.release()


if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 控制同时进入的线程的个数
    thrs = []
    for i in range(13):
        thrs.append(MyThread(i))

    for t in thrs:
        t.start()

        # 信号量，内部有个count，每当一个线程拿到锁，内部count-1，如果减为0则不允许下个线程再拿。
