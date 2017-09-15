# __author: Lambert
# __date: 2017/9/15 14:51
import os, socket

# 配置文件夹路径
BASEDIR = os.path.dirname(os.path.abspath(__file__))
# 配置socket
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)

while True:
    inp = input('>>>')
    cmd, path = inp.split(' ')
    file_path = os.path.join(BASEDIR, path)
    file_size = os.stat(file_path).st_size
    file_name = os.path.basename(file_path)
    file_info = dict([('file_name', file_name), ('file_size', file_size)])
    sk.sendall(bytes(str(file_info), 'utf8'))
    print(str(sk.recv(1024), 'utf8'))
    with open(file_path, 'rb') as file:
        has_sent = 0
        while has_sent != file_size:
            data = file.read(1024)
            sk.sendall(data)
            has_sent += len(data)
            print(round((has_sent / file_size) * 100, 2))  # 获取上传百分比
        msg = sk.recv(1024)
        print(str(msg, 'utf8'))
