# __author: Lambert
# __date: 2017/9/6 11:59
import pickle


def foo():
    print('foo')


f = open('pickle', 'rb')
data = f.read()
data = pickle.loads(data)
data()
