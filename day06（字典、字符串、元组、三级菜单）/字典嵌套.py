# __author: Lambert
# __date: 2017/8/17 14:26
dic = {'name': 'lan', 'age': 12}
for i in dic:
    print(i, dic[i])  # 循环字典并取值

print(dic.items())
for i, v in dic.items():  # 将字典转为元组并取值
    print(i, v)
