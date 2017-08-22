# __author: Lambert
# __date: 2017/8/16 14:19
_user = 'admin'
_passwd = '123'

for i in range(3):
    username = input('username:')
    password = input('password:')
    if username == _user and _passwd == password:
        print("登录成功")
        login_success = True
        break
    else:
        print("用户名或密码错误")
else:  # for循环正常完成会执行，break后不会执行
    print("尝试次数过多")
