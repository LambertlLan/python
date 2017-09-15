# __author: Lambert
# __date: 2017/9/15 14:51
import os, socket

# 配置文件夹路径
BASEDIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASEDIR, 'img')
# 配置socket
sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.bind(address)
sk.listen(3)
while True:
    conn, addr = sk.accept()
    print('等待连接......')
    print(addr, '已连接')
    while True:
        try:
            file_info = conn.recv(102400)
            conn.send(bytes('文件大小接受完成', 'utf8'))
        except Exception as e:
            print('客户端已断开连接,等待下一次连接....')
            break
        else:
            if not file_info:
                break
            file_info = eval(str(file_info, 'utf8'))
            file_name = file_info['file_name']
            file_size = file_info['file_size']
            file_path = os.path.join(IMG_DIR, file_name)
            with open(file_path, 'ab') as file:
                has_received = 0
                while has_received != file_size:
                    data = conn.recv(1024)
                    file.write(data)
                    has_received += len(data)
            print('文件%s成功存储在%s' % (file_name, file_path))
            conn.sendall(bytes('上传成功', 'utf8'))
