# __author: Lambert
# __date: 2017/9/12 14:04
class Foo:
    '''
    注释也会成为类的成员
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('init')

    def __call__(self, *args, **kwargs):  # obj()可以执行__call__方法
        print('call')

    def __int__(self):  # 调用int(obj)会默认执行该方法
        return 111

    def __str__(self):  # 调用str(obj)会默认执行该方法
        return '123'

    def __add__(self, other):  # 将第一个值obj1传入self，obj2传入other，在obj1+obj2时执行该方法
        return int(self.age + other.age)

    def __del__(self):  # 构造方法在对象初始化时执行，析构方法在这个对象被销毁时执行，但不知道什么时候销毁
        print('在对象被销毁时自动执行')


obj = Foo('lan', 18)
print(obj.__dict__)  # 对象的成员全部显示出来{'age': 18, 'name': 'lan'}
print(Foo.__dict__)  # 类的成员全部显示出来
obj()
print(int(obj))
print(str(obj))  # 等于print(obj)
obj1 = Foo('alex', 18)
obj2 = Foo('tung', 28)
print(obj1 + obj2)


class L:
    def __getitem__(self, item):  # li[8]调用该方法
        if type(item) == slice:  # li[1:4:2]调用
            print('进行切片操作')
            print(item.start)  # 1
            print(item.stop)  # 4
            print(item.step)  # 2
        else:
            print('进行索引操作')
            return item + 10

    def __setitem__(self, key, value):  # li[8] = 100 key为8 value为100
        print(key, value)

    def __delitem__(self, key):  # del li[10] key为10
        print(key)

    def __iter__(self):  # 如果对象中有__iter__方法则是一个可迭代对象，先通过iter方法转换为迭代器，在调用next()方法
        return iter([11, 22, 33])


li = L()
print(li[8])
li[8] = 100
li[1:4:2]
del li[10]
for i in li:
    print(i)
