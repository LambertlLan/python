# __author: Lambert
# __date: 2017/9/19 14:42
# __author: Lambert
# __date: 2017/9/19 11:50
import threading, time, queue
from random import randint


class Producer(threading.Thread):
    def run(self):
        while True:
            r = randint(1, 100)
            q.put(r)
            print('生产者', self.name, ":Append" + str(r))
            time.sleep(3)


class Customer(threading.Thread):
    def run(self):
        while True:
            re = q.get()
            print('消费者', self.name, ":Delete",re)


if __name__ == '__main__':
    q = queue.Queue(10)
    threds = []
    for i in range(5):
        threds.append(Producer())
    threds.append(Customer())
    for t in threds:
        t.start()
    for j in threds:
        j.join()
