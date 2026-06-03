# 非单例模式
# class StrTools:
#     pass
#
# s1 = StrTools()
# s2 = StrTools()
#
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))


# 单例模式
from str_tools import str_tool

s1 = str_tool
s2 = str_tool

print(s1)
print(s2)
print(id(s1))
print(id(s2))
