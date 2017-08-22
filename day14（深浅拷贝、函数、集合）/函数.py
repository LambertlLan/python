# __author: Lambert
# __date: 2017/8/22 16:07


# 关键字参数
# def print_info(name, age):
#     print('name:%s' % name)
#     print('age:%s' % age)
#
#
# print_info(age="28", name="alex")

# 默认参数
# def print_info(name, age, sex='male'):  # 默认参数只能跟在最后
#     print('name:%s' % name)
#     print('age:%s' % age)
#     print('sex:%s' % sex)
#
#
# print_info(age="28", name="alex")
# print_info(age="28", name="alex", sex='female')

# 不定参数个数及加法器
# def print_add(*args):
#     number = 0
#     print(''.join(['args:',str(args)]))
#     for i in args:
#         number += i
#     print(number)
#
#
# print_add(1, 2, 3, 4, 5, 6, 7, 8, 9)

def print_info(*args, **kwargs):
    print(args)  # ('alex', 'lambert')  'alex', 'lambert' 转为元组
    print(kwargs)  # {'name': 'alex', 'age': 25}  name="alex", age=25 转为键值对
    for i in kwargs:
        print(':'.join([i,str(kwargs[i])]))

print_info('alex', 'lambert', name="alex", age=25)
