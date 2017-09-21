# __author: Lambert
# __date: 2017/9/21 11:09
import multiprocessing, time


class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()  # 加入父类的方法
        # multiprocessing.Process.__init__(self)

    def run(self):
        sum = 0
        for i in range(100000000):
            sum += i
        print('hello', self.name, time.ctime())


if __name__ == '__main__':
    start = time.time()
    p_list = []
    for i in range(5):
        p = MyProcess()
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()
    end = time.time()
    print(end - start)
