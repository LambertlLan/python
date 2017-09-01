# __author: Lambert
# __date: 2017/9/1 11:22
import hashlib

m = hashlib.sha256()  # 常用sha256,算法越复杂安全性越高，但效率越低
m.update('hello'.encode())
print(m.hexdigest())
