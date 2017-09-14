# __author: Lambert
# __date: 2017/9/13 10:10
# 使用单例模式，使获得的实例为同一实例
class Foo:
    __v = None

    @classmethod
    def get_instans(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v


obj1 = Foo.get_instans()
obj2 = Foo.get_instans()
obj3 = Foo.get_instans()
print(obj1)  # <__main__.Foo object at 0x000002AA8E2A6240>
print(obj2)  # <__main__.Foo object at 0x000002AA8E2A6240>
print(obj3)  # <__main__.Foo object at 0x000002AA8E2A6240>
