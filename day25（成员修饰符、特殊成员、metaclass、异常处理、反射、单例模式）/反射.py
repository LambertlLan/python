# __author: Lambert
# __date: 2017/9/12 18:07
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return '%s-%s' % (self.name, self.age)


# a.  getattr（）
obj = Foo('alex', '18')
n = getattr(obj, 'name')  # 获取对象中的name对象
print(n)
show = getattr(obj, 'show')  # 获取对象中的show对象
print(show())  # alex-18
# b.  hasattr()
print(hasattr(obj, 'show'))  # 判断对象中是否有show这个成员
# c.  setattr()
setattr(obj, 'sex', '男')  # 设置对象中的成员
print(obj.sex)
# d.  delattr()
delattr(obj, 'age')  # 删除对象中的成员
