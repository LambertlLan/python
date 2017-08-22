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
