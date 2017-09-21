# __author: Lambert
# __date: 2017/9/21 15:39
from multiprocessing import Process, Queue
import time


def foo(q):
    print(id(q))
    sum = 0
    for i in range(100000000):
        sum += i
    q.put(sum)


if __name__ == '__main__':
    start = time.time()
    p_list = []
    q = Queue()
    for i in range(5):
        p = Process(target=foo, args=(q,))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    end = time.time()
    print(end - start)
