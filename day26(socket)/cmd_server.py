# __author: Lambert
# __date: 2017/9/14 17:42
import subprocess, socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)

while True:
    conn, addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception as e:
            print('客户端已断开，等待重新连接......')
            break
        else:
            if not data:
                break
            cmd_obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)  # stdout=subprocess.PIPE是将子进程的值放到主进程
            conn.sendall(cmd_obj.stdout.read())

conn.close()
