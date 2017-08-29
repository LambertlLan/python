# __author: Lambert
# __date: 2017/8/21 15:42
# with语句自动close
# with open('poem', 'r', encoding='utf8') as f:
#     for i in f:
#         print(i.strip())
# 进行多文件操作
with open('poem', 'r', encoding='utf8') as file_read, open('poem_copy', 'a', encoding='utf8') as file_write:
    number = 0
    for i in file_read:
        number += 1
        if number == 2:
            file_write.write(''.join([i.strip(), 'alex']))
        else:
            file_write.write(i)
