# __author: Lambert
# __date: 2017/9/12 17:20
class OldBoyError(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise OldBoyError('自定义异常')
    print(111)
except OldBoyError as e:
    print(e)


# assert 条件,断言，用于强制用户服从，不服从就报错，并且可捕获，但是一般不捕获
print(123)
# assert 1 == 2
print(234)

