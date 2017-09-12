# __author: Lambert
# __date: 2017/9/11 14:02

class Grand_father:
    def basketball(self):
        print('GrandFather baseball')


class Father1:  # 父类，基类
    def basketball(self):
        print('Father1 basketball')

    def baseball(self):
        print('Father1 baseball')

    def drink(self):
        print('Father1 drink')


class Father2(Grand_father):  # 父类，基类
    def baseball(self):
        print('Father2 baseball')

    def drink(self):
        print('Father2 drink')


class Son(Father2, Father1):  # 继承多个父类，如果父类中出现相同方法，执行前面的
    def soccer(self):
        print('Son soccer')


s = Son()
s.soccer()
s.baseball()  # 输出Father2 baseball
s.basketball()  # 输出GrandFather baseball
# 寻找规则：
# 先找Father2，再找GrandFather，
# 如果有一个与Father1共同的根则不再向上寻找，
# 并继续找Father1，最后在找共同的根
