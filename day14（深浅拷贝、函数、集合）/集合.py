# __author: Lambert
# __date: 2017/8/22 11:30
li = ['alex', 'lambert', 'tung', 'alex']
s = set(li)  # 去掉重复转为可变集合
print(frozenset(s))  # 去掉重复转为不可变集合
print(list(s))  # 将集合转为列表
print('alex' in s)  # 判断元素在不在集合里面
s.add('uu')  # 添加元素
s.update('opt')  # 作为一个序列挨个添加元素
s.update(['123', 'opt'])  # 分别添加列表中的元素{'lambert', 'opt', 'alex', '123', 'tung'}
s.remove('lambert')  # 删除指定元素
s.pop()  # 随机删除
s.clear()  # 清空
del s  # 删除s

# 交集、并集、差集
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
print(a.intersection(b))  # {4, 5}求交集
print(a & b)  # {4, 5}求交集
print(a.union(b))  # {1, 2, 3, 4, 5, 6, 7, 8}求并集
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8}求并集
print(a.difference(b))  # {1, 2, 3}求b在a的差集
print(a - b)  # {1, 2, 3}求b在a的差集
print(b.difference(a))  # {8, 6, 7}求a在b的差集
print(b - a)  # {8, 6, 7}求a在b的差集
print(a.symmetric_difference(b))  # {1, 2, 3, 6, 7, 8}求a，b的反向交集、对称差集
print(a ^ b)

# 超集、子集
print(a.issuperset(b))  # False a是否为b的超集
print(a > b)  # False a是否为b的超集
print(b.issubset(a))  # False b是否为a的子集
print(b < a)  # False b是否为a的子集
print(set('alex') == set('alexexex'))  # 返回True
print(set('alex') < set('alexwww'))  # 右边包含左边，左边为右边的子集，右边为左边的超集
