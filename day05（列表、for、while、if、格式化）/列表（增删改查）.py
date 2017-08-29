# __author: Lambert
# __date: 2017/8/16 15:32
a = [1, 2, 3, 4, 5]
print('a', a[1:2])
print('a', a[1:])  # 取到最后一位
print('a', a[1:-1])  # 取到倒数第二位
print('a', a[0::1])  # 从左到右一个一个取
print('a', a[1::2])  # 从左到右隔一个去取
print('a', a[4::-2])  # 从右到左隔一个去取
# 添加
b = a
b.append(123)  # 在最后添加
print('b:', b)
b.insert(1, '321')  # 在指定位置插入
print('b:', b)
# 修改
c = [1, 2, 3, 4, 5]
c[1::2] = ['a', 'b']
print('c:', c)
# 删除
d = [100, 101, 102, 103, 104]
d.remove(100)  # 输入值删除
print('d:', d)
del_d = d.pop(3)  # 输入下标删除并返回删除的值
print('d:', d)
print('del_d:', del_d)
del d[1]  # 可删除数组
print('d:', d)
