from pymysql import Connection

conn = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123456',
    autocommit = True
)

print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
conn.select_db("test")

# 通过游标对象执行SQL语句
cursor.execute("INSERT INTO test_pymysql VALUES(4),(5),(6)")
# conn.commit()

conn.close()