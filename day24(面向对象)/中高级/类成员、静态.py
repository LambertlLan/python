# __author: Lambert
# __date: 2017/9/11 17:51
class Foo:
    # 字段（静态字段），属于类，执行可以通过类访问也可以通过对象访问
    contry = 'China'

    def __init__(self, name):
        # 字段（普通字段），属于对象,执行只能通过对象访问
        self.name = self.contry + name

    # 普通方法
    def show(self):
        # 普通方法需要由对象来调用
        print(self.name)

    # 静态方法
    @staticmethod
    # 静态方法可通过FOO类调用
    def hide():
        print('static')

    # 类方法
    @classmethod
    def classfun(cls):
        print(cls)  # <class '__main__.Foo'>

    @property
    def per(self):
        print('per')


# 类成员：
    #   字段：
    # 普通字段
    # 静态字段
# 方法：
    # 普通方法，保存在类中，由对象来调用 self=》对象
    # 静态方法，保存在类中，由类来调用
    # 类方法，保存在类中，由类直接调用 cls=》当前类
# 应用场景
    # 如果对象中需要保存一些值，执行某功能时，需要使用对象中的值  ->  普通方法
    # 不需要任何对象中的值 -> 静态方法


s = Foo('河南')
print(Foo.contry)
print(s.contry)
s.show()
Foo.hide()
Foo.classfun()
