# __author: Lambert
# __date: 2017/9/8 15:25
# 定义并执行类中的方法

# class 类名:
#     def 方法名(self, arg):
#         print(arg)
#
#
# 中间人 = 类名()
# 中间人.方法名(1)
# a = str('alex')  # str()就是一个类


class Father:
    def foo(self, *args, **kwargs):
        print(args)
        print(kwargs)


obj = Father
obj.foo(1, 2, 3, name="alex", age="18")
