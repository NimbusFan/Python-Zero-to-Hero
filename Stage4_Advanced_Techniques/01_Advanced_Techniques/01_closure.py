# 闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
# fn1 = outer("youqianduojin")
# inner = fn1("fanyunfei")
#

# 闭包修改外部变量
def outer(num1):

    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner

fn = outer(20)
fn(10)
fn(10)
