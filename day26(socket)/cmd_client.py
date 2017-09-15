# __author: Lambert
# __date: 2017/9/14 17:43
import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
while True:
    cmd = input('>>>')
    sk.send(bytes(cmd, encoding='utf8'))
    # 第一次先接收数据长度
    length_result = sk.recv(1024)  # 1024控制接收数据的大小单位字节
    sk.send(bytes('111', 'utf8'))
    length_result = int(str(length_result, 'utf8'))
    data = bytes()
    #  判断循环接收数据是否结束
    while len(data) != length_result:
        result = sk.recv(1024)
        data += result
    print(length_result)
    print(str(data, 'gbk'))
