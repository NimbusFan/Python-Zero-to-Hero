# def sleep():
#     import random
#     import time
#     print("Sleeping...")
#     time.sleep(random.randint(1, 5))
#
# # 闭包实现装饰器
# def outer(func):
#     def inner():
#         print("我要睡觉了")
#         func()
#         print("我要起床了")
#
#     return inner
#
# fn = outer(sleep)
# fn()

# 装饰器语法糖写法
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我要起床了")

    return inner

@outer
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1, 5))

sleep()