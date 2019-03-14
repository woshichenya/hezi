
import pymysql

#打开数据库连接
db=pymysql.connect("39.107.239.18","root","wdtx.2016","ceshi_test_chenya",charset='utf8')


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * FROM `ceshi_xinxi`")
'''
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()


#print("Database version : %s " % data)
print("开始输出",data)


data=cursor.fetchmany()
print("开始输出",data)

data=cursor.fetchall()
print("开始输出",data)


data=cursor.fetchone()
print("开始输出",data)

'''


# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
#print("Database version : %s " % data)
print("开始输出",data)
data=cursor.fetchall()
print("开始输出",data)

# 关闭数据库连接
db.close()