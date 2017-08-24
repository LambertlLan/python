# __author: Lambert
# __date: 2017/8/24 10:07


# 闭包函数
def outer():
    x = 10

    def inner():  # 条件一 inner是个内部函数
        print(x)  # 条件二 外部环境的一个变量

    return inner  # 结论：内部函数inner就是一个闭包


outer()()
