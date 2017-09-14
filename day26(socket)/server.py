# __author: Lambert
# __date: 2017/9/14 13:58
# 参数 family = AF_INET  ipv4服务器之间通信 默认
# 参数 family = AF_INET6 ipv6服务器之间通信 默认
# 参数 family = AF_UNIX 用于unix系统进程间的通信

# 参数 type = SOCK_STREAM TCP 默认
# 参数 type = SOCK_Dgram UDP

# 客户端方法
# bind()
# listen()
# accept()
# recv() 接收消息
# send() 发送消息，字节有限制，可能发不完,在py2中可以发字符串，在3中只能发byte类型
# sendall() while True send（）
import socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)  # 控制等待排队个数
while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)  # 不允许发空，发空是阻塞状态
        except Exception as e:  # windows处理强行关闭client报错，linux不会报错会认为data为空
            print(e)
            print('等待重新连接.....')
            break
        else:
            if not data:
                print('对方已下线，重新等待连接')
                break
            print(str(data, 'utf8'))
            inp = input('>>>')
            conn.send(bytes(inp, 'utf8'))  # 转换为byte类型再发送
conn.close()  # 关闭一个用户的连接
# sk.close()  # 关闭客户端的socket连接
