# __author: Lambert
# __date: 2017/9/11 14:02


# 注：父类对应子类，基类对应派生类
class Father:  # 父类，基类
    def basketball(self):
        print('Father basketball')

    def baseball(self):
        print('Father baseball')

    def drink(self):
        print('Father drink')


class Son(Father):  # 子类，派生类
    def soccer(self):
        print('Son soccer')

    def drink(self):  # 重定义父类方法
        super(Son, self).drink()  # 加入父类方法
        # Father.drink(self)  # 也可调用父类的方法，但不推荐
        print('SON drink')


s = Son()
s.soccer()  # 调用自己的方法
s.baseball()  # 调用基类的方法
s.drink()  # 调用重定义方法
