# __author: Lambert
# __date: 2017/9/8 17:20
class Bar:
    def __init__(self, name, age):  # 构造方法,在s = Bar('alex', '32')时调用
        self.name = name
        self.age = age

    def foo(self, arg):
        print(self.name, self.age, arg)


s = Bar('alex', '32')
s.foo('大保健')
s2 = Bar('tung', '35')
s2.foo('tung')
