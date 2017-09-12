# __author: Lambert
# __date: 2017/9/12 10:16


class Foo:
    # 类的属性
    @property
    def per(self):
        print('per')
        return 1

    # 设置用于赋值的方法
    @per.setter
    def per(self, value):
        print(value)

    # 设置用于del的方法
    @per.deleter
    def per(self):
        print('delete')

    # 不常用写法
    # def f1(self):
    #     return 123
    #
    # def f2(self, val):
    #     print(val)
    #
    # def f3(self):
    #     print('del')
    #
    # per = property(fget=f1, fset=f2, fdel=f3 ,doc="注释，可有可无")


obj = Foo()
s = obj.per
print(s)
# 调用@per.setter下的方法
obj.per = 2
# 调用@per.delete下的方法
del obj.per
# 注：此类方法只会调用对应方法，不会真的去设置或者删除
