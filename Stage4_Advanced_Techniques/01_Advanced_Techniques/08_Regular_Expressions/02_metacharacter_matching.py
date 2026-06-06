import re

s = "fanyunfei1 @@python2 !!666 ##it3"
result = re.findall(r'[5-7]', s)
print(result)

# 匹配账号
r = '^[0-9a-zA-Z]{6,10}$'
S='123456_'
print(re.findall(r, s))

# 匹配QQ号
r = '^[1-9][0-9]{4,10}$'
S = '123453678'
print(re.findall(r, s))

# 匹配邮箱
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.d.e.f.g@qq.com.a.z.c.d.e'
print(re.findall(r, s))