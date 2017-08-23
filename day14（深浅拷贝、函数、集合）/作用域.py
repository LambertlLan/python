# __author: Lambert
# __date: 2017/8/23 10:14
# x = int(2.9)  # int等函数属于built-in及为系统内部函数
#
# g_count = 0  # global作用域
#
#
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         i_count = 2  # local
#         print(i_count)
#
#     print(o_count)
#     inner()
#
#
# outer()
# 函数作用域L<E<G<B

count = 10


def outer():
    # global count
    # count = 5 # 先声明全局变量就可以取到全局变量count

    count = 5  # 重新开辟内存建立变量count = 5
    print(count)  # 输出5

    # count = 5  # 局部作用域不能修改全局作用域，只会重新创建一个内存，故报错调用在定义之前。删除
    def inner():
        nonlocal count  # 如果不是
        count += 1


outer()
print(count)  # 输出10
