# __author: Lambert
# __date: 2017/9/14 17:43
import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
while True:
    cmd = input('>>>')
    sk.send(bytes(cmd, encoding='utf8'))
    data = sk.recv(10240)  # 10240控制接收数据的大小单位字节
    print(str(data, 'gbk'))
