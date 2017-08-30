# __author: Lambert
# __date: 2017/8/30 15:06
import random

print(random.random())  # 随机数0-1
print(random.randint(1, 8))  # 1-8的随机整数包含1和8
print(random.randrange(1, 8))  # 1-8的随机整数包含1不包含8
print(random.choice('hello'))  # 字符串中随机提取一个值
print(random.choice(['123', 123, [1, 2]]))  # 列表中随机取一个
print(random.sample(['123', 123, [1, 2]], 2))  # 列表中随机取两个值
