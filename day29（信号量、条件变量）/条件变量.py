# __author: Lambert
# __date: 2017/9/19 11:50
import threading, time
from random import randint


class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(1, 100)
            print('生产者', self.name, ":Append" + str(val), L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()  # 通知消费者可以开始吃
                lock_con.release()
            time.sleep(3)


class Customer(threading.Thread):
    def run(self):
        global L
        while True:
            lock_con.acquire()
            if len(L) == 0:
                lock_con.wait()  # 阻塞等待通知
            print('消费者', self.name, ":Delete" + str(L[0]), L)
            del L[0]
            lock_con.release()
            time.sleep(1)


if __name__ == '__main__':
    L = []
    lock_con = threading.Condition()
    threds = []
    for i in range(5):
        threds.append(Producer())
    threds.append(Customer())
    for t in threds:
        t.start()
    for j in threds:
        j.join()
