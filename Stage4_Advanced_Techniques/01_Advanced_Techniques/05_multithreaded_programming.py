# # 单线程
# import time
#
#
# def sing():
#     while True:
#         print("singing......")
#         time.sleep(1)
#
# def dance():
#     while True:
#         print("dancing......")
#         time.sleep(1)
#
# if __name__ == '__main__':
#     sing()
#     dance()


# 多线程
import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target = sing, args = ("singing......", ))
    dance_thread = threading.Thread(target = dance, kwargs = {"msg":"dance......"})

    sing_thread.start()
    dance_thread.start()