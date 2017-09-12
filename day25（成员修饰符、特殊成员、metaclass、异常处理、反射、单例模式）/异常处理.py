# __author: Lambert
# __date: 2017/9/12 16:34
# 最基本的try
while True:
    try:  # try中代码块一旦出错后面不再执行
        i = int(input('请输入数字>>>'))
        print(i)
        raise Exception('出错啦')  # 主动触发异常、
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:  # Exception代表所有错误类型，可替换成IndexError，如果替换只可捕获一种错误
        # e是Exception的对象，对象中封装了错误信息
        # 上述代码如果出错自动执行当前代码块
        print(e)
    else:
        print('如果不出错会执行else')
    finally:
        print('不管出不出错都会执行')
