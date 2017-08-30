# __author: Lambert
# __date: 2017/8/30 11:05
import time

print(help(time))
time.time()  # 系统当前时间**************
time.sleep(2)  # 阻塞2秒
time.clock()  # 计算cpu执行的时间
time.gmtime()  # 结构化时间：世界标准时间UTC（英国时间）
time.localtime()  # 结构化时间：本地时间***********
time.localtime(1504075985.8592992) # 时间戳转结构化时间
time.strftime('%Y-%m-%d %H:%M:%S')  # 自定义日期时间格式输出********
sru_time = time.localtime()
time.strftime('%Y-%m-%d %H:%M:%S',sru_time)  #  结构化时间转为自定义格式
a = time.strptime('2017-08-30 14:34:08', '%Y-%m-%d %H:%M:%S')  # 转为结构化时间***********
a.tm_year  # 取结构化时间中的年月日等
time.ctime(time.time())  # 时间戳转日期，不加则获取当前时间
time.mktime(time.localtime())  # 结构化时间转时间戳*************

import datetime

print(datetime.datetime.now())  # 2017-08-30 15:05:08.921036输出常用格式时间
