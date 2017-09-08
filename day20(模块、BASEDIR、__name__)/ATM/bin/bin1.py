# __author: Lambert
# __date: 2017/9/5 10:52
import sys, os

# 如果不引用相对路径pycharm默认自动添加根路径，ATM路径获取到并添加到sys.path中
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from module import main

main.main()
print(__file__) # E:/Lambert/study/Python/day20(模块、BASEDIR、__name__)/ATM/bin/bin1.py  pycharm自动改为绝对路径，实际为bin.py