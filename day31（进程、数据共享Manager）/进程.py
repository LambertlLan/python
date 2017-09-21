# __author: Lambert
# __date: 2017/9/21 11:09
import multiprocessing, time


def foo(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=('alex',))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
