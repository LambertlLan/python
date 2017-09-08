# __author: Lambert
# __date: 2017/8/22 9:53
import copy

s = [[1, 2], 'alex', 'lambert']
s3 = s.copy()  # 浅copy
# s3 = copy.deepcopy(s)  # 深copy

s3[1] = 'linux'
print(s3)  # [[1, 2], 'linux', 'lambert']
print(s)  # [[1, 2], 'alex', 'lambert']
s3[0][1] = 'alex'
print(s3)  # [[1, 'alex'], 'linux', 'lambert']
print(s)  # [[1, 'alex'], 'alex', 'lambert']
# 深copy
# 总结：a = ['a',[1,2,3]]
# 1.b = a是将指向的['a',[1,2,3]]的整体内存地址给b，故a的值改变b也会改变
# 2. b = a.copy()是将'c'和[1,2,3]的内存地址分别赋给b，故修改a中的'a'，b不会变化，修改a中的[1,2,3]，b中会相因变化
# 3. b = copy.deepcopy(a)是将a中的所有内存拷贝出来开辟新内存储存并给b，故a修改任意值b不会发生变化
