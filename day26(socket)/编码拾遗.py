# __author: Lambert
# __date: 2017/9/15 13:51
# PY3: str bytes
# str: unicode
# bytes:十六进制
s = 'hello 编码'
# str >>>>>>>>> bytes 编码
# 按照utf8的规则去编码
b = bytes(s, 'utf8')  # b'hello \xe7\xbc\x96\xe7\xa0\x81'
print(b)
# 按照utf8的规则编码为十六进制
print(s.encode('utf8'))  # b'hello \xe7\xbc\x96\xe7\xa0\x81'
print(s.encode('gbk'))  # b'hello \xb1\xe0\xc2\xeb'
# bytes >>>>>>>>> str 解码
# 按照utf8的规则解码为unicode编码
print(str(b, 'utf8'))
print(b.decode('utf8'))
