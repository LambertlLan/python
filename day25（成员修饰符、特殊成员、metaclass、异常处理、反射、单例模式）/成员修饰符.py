# __author: Lambert
# __date: 2017/9/12 11:53
class Father:
    def __init__(self):
        self.__name = 'alex'
        print('继承调用父类的__init__()')
    def __pri(self):  # 父类里面的私有字段和函数继承也无法访问
        print('Father private')


class Foo(Father):
    __v = '123'  # 私有静态字段

    def __init__(self):
        self.name = 'alex'
        self.__age = 20  # 私有成员，无法在外部调用
        # self.__pri()
        super(Foo, self).__init__() # 继承时不会执行父类的__init__()

    def show(self):
        self.__f()
        return self.__age  # 可以在外部访问

    def __f(self):  # 私有普通函数
        print('private function')

    def show_private(self):
        r = self.__f()
        return r


obj = Foo()
print(obj.name)
print(obj.show())
obj.show_private()
