# __author: Lambert
# __date: 2017/9/19 14:01
import time, threading


class Boss(threading.Thread):
    def run(self):
        print('BOSS:今晚大家加班到十点')
        event.set()
        time.sleep(5)
        print('BOSS:<22:00>可以下班啦')
        event.isSet() or event.set()


class Workers(threading.Thread):
    def run(self):
        event.wait()
        print('啊...............')
        time.sleep(1)
        event.clear()
        event.wait()
        print('OhYeah!')


if __name__ == '__main__':
    event = threading.Event()
    L = []
    for i in range(5):
        L.append(Workers())
    L.append(Boss())

    for j in L:
        j.start()
    for t in L:
        t.join()
