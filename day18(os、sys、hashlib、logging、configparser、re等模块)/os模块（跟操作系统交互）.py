# __author: Lambert
# __date: 2017/8/31 10:24
import os

print(os.getcwd())  # 获取当前工作目录
os.chdir(r"E:\Lambert")  # 修改当前路径 r为原生字符串，不转义,正反斜杠都可
print(os.getcwd())

print(os.curdir)  # 获取当前文件夹相对路径 得到.
print(os.pardir)  # 获取父文件夹相对路径 得到..
os.makedirs('a\\b\\c')  # 递归创建文件夹，及e:\a\b\c
os.removedirs('a\\b\\c')  # 从后往前如果文件夹为空依次删除
os.rmdir('dirname\\a') # 删除一个文件夹
os.rmdir('dirname')
os.remove('dir.py')  # 只能删文件，不能删文件夹
os.mkdir('dirname')  # 建立一个文件夹
os.mkdir('dirname\\a')  # 在dirname下再建立一个a
# 列出当前路径下的文件
['send.py', '__pycache__', '列表生成式.py', '时间戳日期转换.py', '生成器(generator).py', '生成验证码.py', '迭代器(iterator).py', '随机数.py']
print(os.listdir(r'E:\Lambert\study\Python\day17(列表生成式、生成器、迭代器、time模块、random模块)'))
os.rename('www', 'nnn')  # 修改文件夹\文件名
info = os.stat('./os模块（跟操作系统交互）.py')  # 获取文件信息
print(info.st_atime)  # 最后一次访问时间
print(info.st_mtime)  # 修改时间
print(info.st_ctime)  # 创建时间
print(os.sep)  # 打印操作系统路径分割符,windows下为\，linux下为/
print(os.linesep)  # 打印操作系统换行分割符,windows下为\r\n，linux下打印\n
print(os.pathsep)  # 各个路径之间的分割符,windows为;,linux为:
print(os.system('dir'))# 执行系统命令
print(os.environ)  # 拿环境变量转为字典
print(os.path.abspath('./nnn'))  # 拿绝对路径
print(os.path.split(r'E:\Lambert\study\Python\day17(列表生成式、生成器、迭代器、time模块、random模块)'))  # 找到最后一个进行分割
print(os.path.dirname(r'E:\Lambert\study\Python\day17(列表生成式、生成器、迭代器、time模块、random模块)'))  # 找到文件夹的名字，相对路径则返回相对路径
print(os.path.dirname(__file__))  # 拿到当前文件的文件夹
a = 'E:\Lambert\study\Python'
b = 'day17'
print(os.path.join(a, b))  # 拼接地址，E:\Lambert\study\Python\day17
os.chdir(r"E:/Lambert")
