# __author: Lambert
# __date: 2017/8/16 11:19
name = input('name:')
age = int(input("age:"))
job = input('job:')
salary = input('salary:')

if salary.isdigit():  # 判断是否为数字
    salary = int(salary)
else:
    print('必须为数字')
    exit()  # 退出程序
# %s字符串类型
# %d整数类型
# %f浮点数类型
# '''前面加u是告诉python解释器后面的字符串用unicode解析
msg = '''
--------------------info %s-----------------
Name:%s 
Age:%d
Job:%f
Salary:%d
--------------------end---------------------
you live in %s years
''' % (name, name, age, job, salary, 65 - age)
print(msg)
