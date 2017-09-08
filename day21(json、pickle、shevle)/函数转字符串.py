# __author: Lambert
# __date: 2017/9/6 11:54
import pickle

f = open('pickle', 'wb')  # wb是写入二进制


def foo():
    print('foo')


data = pickle.dumps(foo)
print(data)
f.write(data)
f.close()
