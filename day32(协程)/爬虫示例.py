# __author: Lambert
# __date: 2017/9/22 10:33
from gevent import monkey

monkey.patch_all()  # windows对I/O操作感知不明显，此为增强敏感度
import gevent, time, multiprocessing
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    res = urlopen(url)
    data = res.read()
    print('%d bytes recevied from %s.' % (len(data), url))


# if __name__ == '__main__':
#     start = time.time()
#     l = ['http://www.xiaohuar.com/', 'https://www.python.org/', 'https://www.github.com/']
#     p = []
#     for url in l:
#         t = multiprocessing.Process(target=f, args=(url,))
#         p.append(t)
#         t.start()
#     for t in p:
#         t.join()
#     print(time.time() - start)
start = time.time()
gevent.joinall([
    gevent.spawn(f, 'http://www.xiaohuar.com/'),
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.github.com/'),
])
print(time.time() - start)
# 实测：
# 多线程19秒
# 多进程3.8秒
# 协程3.5秒
