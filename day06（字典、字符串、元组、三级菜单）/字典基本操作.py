# __author: Lambert
# __date: 2017/8/17 11:22
# dic = {'123': '123', 'age': '25'}
dic1 = {'name': 'name', 'age': '23', 'sex': 'nan'}
# dic2 = dict((('name', 'name'), ('age', '23'), ('sex', 'nan')))
# dic3 = dict((['name', 'name'], ['age', '23'], ['sex', 'nan']))
# dic4 = dict([['name', 'name'], ['age', '23'], ['sex', 'nan']])
# print(dic1)
# print(dic2)
# print(dic3)
# print(dic4)
# ret = dic1.setdefault('name', 'alan')  # 如果字典中有不进行任何操作,返回真实的值
# dic1.setdefault('hobby', 'game')  # 字典中没有直接添加
# key = dic1.keys()  # 找出该字典的所以键
# val = dic1.values()  # 找出该字典的所以值
# item = dic1.items()  # 找出该字典的所以键值对
# list(key)  # 转化为列表

# dic1.update(dic)  # 将dic合并到dic1并覆盖相同项
# print(dic)

# dic1.clear()  # 清空
# dic1.pop('name')  # 删除指定项
# dic1.popitem()  # 随机删除一项
# del dic1['name']  # 删除指定项
# dic6 = dict.fromkeys(['host1', 'host2', 'host3'], 'test1')  # 初始化为统一值
# dic6 = dict.fromkeys(['host1', 'host2', 'host3'], ['test1', 'test2'])  # 初始化为列表时，修改一个值会修改所以值
# print(dic6)
# dic6['host2'][1] = 'test3'
# print(dic6)
