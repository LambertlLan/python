# __author: Lambert
# __date: 2017/8/18 15:19
s = 'i am 特斯拉'
s_to_gbk = s.encode('gbk')  # 编码为gbk打印出b'i am \xcc\xd8\xcb\xb9\xc0\xad'
gbk_to_s = s_to_gbk.decode('gbk')  # 解码为utf-8打印出i am 特斯拉
print(s)
print(s_to_gbk)
