# __author: Lambert
# __date: 2017/8/21 14:55
# r+,w+,a+
# f = open('poem', 'r+', encoding='utf8') # 读写模式
# f = open('poem', 'w+', encoding='utf8')  # 写读模式,打开时清空文件
f = open('poem', 'a+', encoding='utf8')  # 追加写模式,打开时光标位于最后
# print(f.read())  # read后光标会到最后，这是必须移动光标位置才会读出值
f.write('hello world') # write 会将光标移到最后
f.seek(0)
print(f.read())
f.close()
