# __author: Lambert
# __date: 2017/9/21 16:05
from multiprocessing import Process, Manager


def foo(d, l, i):
    d[i] = 1
    d['2'] = 2
    d[0.25] = i
    l.append(i)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))
        p_list = []
        for i in range(10):
            p = Process(target=foo, args=(d, l, i))
            p_list.append(p)
            p.start()
        for i in p_list:
            i.join()
        print(l)
        print(d)
