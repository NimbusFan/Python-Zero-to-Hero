from pymysql import Connection

conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456'
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
conn.select_db("test")

# 通过游标对象执行SQL语句
cursor.execute("SELECT * FROM test_pymysql")
results = cursor.fetchall()

for row in results:
    print(row)


conn.close()