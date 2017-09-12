# __author: Lambert
# __date: 2017/9/12 15:43
'''
a.python中一切事物皆对象
b.
    class Foo:
        pass
    obj = Foo()
    # obj是对象，Foo类
    # Foo类也是一个对象，type的对象
'''


class MyType(type):
    def __init__(self, *args, **kwargs):
        print('mytype')

    def __call__(self, *args, **kwargs):
        r = self.__new__()

# Foo = type('Foo', (object), {'func': f1}) 等于下面的class Foo
class Foo(object, metaclass=MyType):  # 类默认由type创建，修改metaclass指定有Mytype 创建
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return 'obj'

    def func(self):
        print(123)


def f1(self):
    print(123)
