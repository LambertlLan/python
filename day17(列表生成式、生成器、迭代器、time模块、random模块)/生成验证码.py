# __author: Lambert
# __date: 2017/8/30 15:28
import random


# 生成四位随机数
def v_code():
    code = ''
    for i in range(4):
        code += str(random.randrange(10))
    print(code)


v_code()


# 生成四位含字母验证码
def va_code():
    code = ''
    for i in range(4):
        al = chr(random.randrange(65, 91))
        num = str(random.randrange(10))
        code += random.choice([al, num])

    print(code)


va_code()
