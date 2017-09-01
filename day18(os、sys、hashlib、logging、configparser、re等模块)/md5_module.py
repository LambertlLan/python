# __author: Lambert
# __date: 2017/9/1 11:02
import hashlib

m = hashlib.md5()
print(m)
m.update('hello '.encode('utf8'))  # 必须是bytes类型
m.update('world'.encode('utf8'))  # 5eb63bbbe01eeed093cb22bb8f5acdc3 在原有基础上更新,生成新字符串并转换
# print(m.digest())  # 转为二进制
print(m.hexdigest())  # 打印十六进制的值

m2 = hashlib.md5()
m2.update('hello world'.encode('utf8'))  # 5eb63bbbe01eeed093cb22bb8f5acdc3

print(m2.hexdigest())
