# __author: Lambert
# __date: 2017/9/1 14:21
# 等级 critical > error >warning > info > debug >notset
import logging

# logging.debug('debug message')  # debug和info级别不够不能在屏幕打印，但可以通过logging.basicConfig配置


# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt="%a,%d %b %Y %H:%M:%S",  # a是周几，b是英文月份，m是数字月份
#                     filename='test.log',  # 加filename则文件显示，不加则屏幕打印
#                     filemode='a'  # 默认为a可以设置为w
#                     )
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


# logger
logger = logging.getLogger()
# logger = logging.getLogger(name) 加入文件名，不然会返回root，在所以文件记录
# 创建一个hanlder,用于写入日志文件
fh = logging.FileHandler('test.log')
# 创建一个handler，用于输出控制台
ch = logging.StreamHandler()
# 创建格式化对象
formater = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', encoding="utf8")
formater.datefmt = "%a,%d %b %Y %H:%M:%S"
# 给hanlder设置格式化对象
fh.setFormatter(formater)
ch.setFormatter(formater)
# 给logger添加hanlder
logger.addHandler(fh)
logger.addHandler(ch)
# logger设置日志等级低于info等级不会记录
logger.setLevel(logging.INFO)


logger.info('5555555555')
