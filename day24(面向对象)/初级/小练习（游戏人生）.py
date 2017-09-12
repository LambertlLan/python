# __author: Lambert
# __date: 2017/9/11 17:31
class Person:
    def __init__(self, n, g, a, f):
        self.name = n
        self.sex = g
        self.age = a
        self.fight = int(f)

    def grass_fight(self):
        self.fight -= 200

        print('草丛战斗后%s性别%s年龄%s战力为%s' % (self.name, self.sex, self.age, self.fight))

    def self_fight(self):
        self.fight += 100
        print('自我修炼后%s性别%s年龄%s战力为%s' % (self.name, self.sex, self.age, self.fight))

    def many_fight(self):
        self.fight -= 500
        print('多人战斗后%s性别%s年龄%s战力为%s' % (self.name, self.sex, self.age, self.fight))


cang = Person('苍老师', '女', '18', '1000')
dong = Person('东老师', '男', '20', '1500')
bo = Person('波老师', '女', '25', '2000')

cang.grass_fight()
dong.self_fight()
bo.many_fight()