# __author: Lambert
# __date: 2017/9/8 16:15


class Foo:
    def fun(self, arg):  # self是调用他的那个对象
        print(self, arg)


s1 = Foo()
s2 = Foo()
print(s1)  # <__main__.foo object at 0x000002813C0F4160>
s1.fun(111)  # <__main__.foo object at 0x000002813C0F4160> 111
print(s2)  # <__main__.foo object at 0x000002813C0F4198>
s2.fun(111)  # <__main__.foo object at 0x000002813C0F4198> 111


# 中间人加入参数

class Bar:
    def foo(self, arg):
        print(self.name, self.age, self.hobbit, arg)  # alex 19


s = Bar()
s.name = 'alex'
s.age = '50'
s.hobbit = '大保健'
s.foo(19)

s2 = Bar()
s2.name = 'tung'
s2.age = '30'
s2.hobbit = 'java'
s2.foo(19)
