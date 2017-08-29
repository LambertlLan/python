# __author: Lambert
# __date: 2017/8/29 14:36


def f(x):
    return x + 1


a = [x for x in range(10)]
b = [x * x for x in range(10)]
c = [f(x) for x in range(10)]
print(a)
print(b)
print(c)

t = (123, 321)
e, f = t  # 拿到其中的两个元素e=t[0],f=t[1]
print(e)  # e=123
print(f)  # f = 321
