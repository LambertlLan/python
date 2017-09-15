# __author: Lambert
# __date: 2017/9/14 17:42
import subprocess, socket

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)

while True:
    conn, addr = sk.accept()  # 返回一个元组(conn, addr)
    print(addr)
    while True:
        try:  # 当客户端断开连接时不停止程序
            data = conn.recv(1024)
        except Exception as e:
            print('客户端已断开，等待重新连接......')
            break
        else:
            if not data:  # 如果客户端发送空则重新接收
                break
            # stdout=subprocess.PIPE是将子进程的值放到主进程
            cmd_obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
            cmd_result = cmd_obj.stdout.read()
            # 得到命令返回值的长度以便客户端循环接收
            result_length = bytes(str(len(cmd_result)), encoding='utf8')
            conn.sendall(result_length)
            conn.recv(1024)  # 两条数据同时send可能发生粘包现象所以使用recv来隔断
            conn.sendall(cmd_result)

sk.close()
