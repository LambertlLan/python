# __author: Lambert
# __date: 2017/9/18 11:07
import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8081)
sk.connect(address)
while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, encoding='utf8'))
    data = sk.recv(1024)
    print(str(data, encoding='utf8'))
