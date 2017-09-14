# __author: Lambert
# __date: 2017/9/14 13:59
# client下的方法
# connet()
# recv()
# send()
# sendall()
import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)
while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, encoding='utf8'))
    data = sk.recv(1024)  # 会阻塞等待消息
    print(str(data, encoding='utf8'))  # 将byte类型转换为str
    # sk.send(bytes('yyy', encoding='utf8')) #发送空会阻塞，发送YYY会继续往下走
