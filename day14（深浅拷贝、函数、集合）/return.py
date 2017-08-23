# __author: Lambert
# __date: 2017/8/23 9:56


def print_info():
    print('alex')
    return 10  # 用于返回值，如果不写python会自动加上，并默认返回None，return下面的代码不再执行


def foo():
    return 1, 2, 3, ['a', 'b']  # 如果return多个对象，会默认封装成一个元组


print(print_info())
print(foo())
