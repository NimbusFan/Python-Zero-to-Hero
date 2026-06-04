# socket服务端开发
import socket

# 创建socket对象
socket_server = socket.socket()

# 绑定ip地址和端口
socket_server.bind(('localhost', 8888))

# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数类参数，表示接收的链接数量

# 等待客户端连接
# result: tuple = socket_server.accept()
# conn = result[0]    # 客户端和服务端的连接对象
# address = result[1]     # 客户端的地址信息
conn, address = socket_server.accept()
# accept方法返回的是二元元组(链接对象，客户端地址信息)
# 可以通过变量1,变量2=socket_server.accept()的形式,直接接收二元元组内的两个元素
# accept方法是阻塞的方法

print(f"接收到了客户端的连接，客户端的信息是：{address}")

while True:
    # 接收客户端信息
    data: str = conn.recv(1024).decode("utf-8")
    # recv接收的参数是缓冲区大小，一般给1024即可
    # recv的返回值是一个字节数组，即bytes对象，不是字符串，可通过decode方法通过utf-8解码，将字节数组转换为字符串
    # recv是阻塞的方法
    print(f"客户端发来的消息是：{data}")

    # 发送回复消息
    msg = input("输入要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))  # 使用encode将字符串编码为字节数组对象

# 关闭链接
conn.close()
socket_server.close()