# __author: Lambert
# __date: 2017/9/21 15:39
from multiprocessing import Process, Pipe
import time, os


def foo(child_conn):
    print(child_conn.recv(), '%s进程以收到' % os.getpid())
    sum = 0
    for i in range(100000000):
        sum += i
    child_conn.send(sum)
    child_conn.close()


if __name__ == '__main__':
    start = time.time()
    p_list = []
    parent_conn, child_conn = Pipe()  # 通过PIPE返回两个对象，将child_conn作为参数传给子进程
    for i in range(5):
        parent_conn.send('开始计算')
        p = Process(target=foo, args=(child_conn,))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    print(parent_conn.recv())
    end = time.time()
    print(end - start)
