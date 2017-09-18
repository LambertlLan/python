# __author: Lambert
# __date: 2017/9/1 10:08
# 跟python解释器进行交互
import sys,os


def post():
    print('post')


def download():
    print('download')


s = sys.argv  # ['sys_module.py', 'download']命令行参数

print(s)
if s[1] == 'post':
    post()
elif s[1] == 'download':
    download()
else:
    sys.exit('error')  # 退出程序,exit(0)为正常退出

import time

print(sys.path)  # 寻找模块的路径
sys.path.append('E:\Lambert\study\Python\day17(列表生成式、生成器、迭代器、time模块、random模块)')  # 自定义模块如果找不到可以添加绝对路径
print(sys.platform)
if sys.platform == 'win32':
    os.system('dir')
else:
    os.system('ls')