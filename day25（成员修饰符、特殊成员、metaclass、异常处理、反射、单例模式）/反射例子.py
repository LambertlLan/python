# __author: Lambert
# __date: 2017/9/13 9:52
import s2

while True:
    inp = input('请输入地址>>>')

    if hasattr(s2,inp):
        r = getattr(s2,inp)
        print(r())
    else:
        print('404')
