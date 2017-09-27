# __author: Lambert
# __date: 2017/9/27 10:21
import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', db='lanyu', charset='utf8')
# 创建游标（普通游标）
# cursor = conn.cursor()
# 创建游标（获得字典）
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
l = [
    ('pymysql1', 20, 1),
    ('pymysql2', 20, 2),
    ('pymysql3', 20, 1),
]
inp = ('pymysql', 20, 1)
# 添加一条数据
# r = cursor.execute("INSERT INTO userinfo(name,age,par_nid) VALUES(%s,%s,%s)", inp)
# 添加多条数据
# r = cursor.executemany("INSERT INTO userinfo(name,age,par_nid) VALUES(%s,%s,%s)", l)
# 更新数据
# r = cursor.execute('update userinfo set name=%s where nid=%s', ('马狗蛋', 7))
# 删除数据
# r = cursor.execute('delete from userinfo where nid=%s', (11,))
# 查看数据(连表查询)
# r = cursor.execute('select * from userinfo JOIN department on userinfo.par_nid = department.nid')
# 查看数据(修改字段名)
# r = cursor.execute('select nid as id,name as f from userinfo')  # 将nid字段改为id，那么字段改为f
# result = cursor.fetchall()
# cursor.fetchone()  # fetchone类似file.read()会移动指针
# print(result)
# 插入数据时获取自增id
r = cursor.execute('insert into userinfo(name,age,par_nid) VALUES (%s,%s,%s)', ('自增id', 15, 2))
nid = cursor.lastrowid
print(nid)
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
