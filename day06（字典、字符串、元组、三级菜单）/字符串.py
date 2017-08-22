# __author: Lambert
# __date: 2017/8/17 16:12

a = '123'
b = 'abc'
c = 'ABC'
st = 'hello world {name} is {age}'
print(a + b)  # 效率太低
d = '------'.join([a, b, c])  # 拼接字符串 123------abc------ABC
# 'my title title'.split(' ')  # 字符串分割为['my', 'title', 'title']
# 'my title title'.rsplit('i',1)  # 字符串分割为['my title t', 'tle'] 只分割一次，以右为准
# st.count('l')  # 计算l在字符串中的个数
# st.capitalize()  # 首字母大写
# st.center(50,'-')  # 一共打印50个字符，st放中间，其余用-补充 -------------------hello world--------------------
# st.ljust(50,'-')  # 一共打印50个字符，st放中间，其余用-补充  hello world---------------------------------------
# st.rjust(50, '-')  # 一共打印50个字符，st放中间，其余用-补充 ---------------------------------------hello world
# st.endswith('ld')  # 以什么结尾
# st.startswith('he')  # 以什么开头
# st.expandtabs(tabsize=20)  # st = 'hello\t world' 在\t加入空格
# st.find('fff')  # 查找元素，并将找到的第一个元素索引值返回，找不到则返回-1
# st.index('l')  # 同上，找不到则报错
# st.format(name='lambert',age="321")  # 格式化输出字符串 st = 'hello world {name} is {age}' 返回新值
# st.format_map({'name': 'lambert', 'age': 352})  # 格式化输出字符串(参数为字典) st = 'hello world {name} is {age}' 返回新值
# 'abc456'.isalnum()  # 是否是字母或数字
# '100'.isdecimal()  # 是否是十进制
# '100'.isnumeric()  # 是否是整数
# '100.123'.isdigit()  # 是否是整数
# '100'.isidentifier()  # 是否是合法变量
# '100'.islower()  # 是否是全小写
# '100'.isupper()  # 是否是全大写
# '  '.isspace() # 是否是空格
# 'My Title'.istitle()  # 是否是标题
# 'My Title'.lower()  # 大写转小写
# 'My Title'.upper()  # 小写变大写
# 'My Title'.swapcase()  # 小写变大写,大写变小写
# '    my title ok'.strip()  # 去掉空格
# 'my\n'.strip() == 'my'  # 去掉换行符
# 'my\n'.lstrip() == 'my'  # 去掉左边的符号
# 'my\n'.rstrip() == 'my'  # 去掉右边的符号
# 'my title title'.replace('title', 'lesson', 1)  # 替换title1次，不加为全部替换
# 'my title title'.title()  # 转为标题
print()
