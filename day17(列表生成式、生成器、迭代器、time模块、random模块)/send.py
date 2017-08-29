# __author: Lambert
# __date: 2017/8/30 0:19


def foo():
    count = yield 1
    print(count)
    yield 2


b = foo()
next(b)
# b.send(None) # 等于next（b）
b.send('eee')  # 将eee赋值给count，并继续执行
