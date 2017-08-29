# __author: Lambert
# __date: 2017/8/21 9:53
# f = open('poem', 'r', encoding='utf8')
# # for i in f:  # 读文件常用方式，要求文件编码为utf8
# #     print(i)
# print(f.tell())  # 显示光标当前位置
# print(f.read(2))  # 返回两个字符，并会使光标发生移动
# f.seek(0)  # 移动光标
# print(f.tell())
f = open('test', 'a', encoding='utf8')
f.truncate(3)  # 从第三个字节开始向后截，一个中文为三个字节
f.close()
