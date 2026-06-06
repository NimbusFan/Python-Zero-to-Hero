import re

str_1 = "fan yun fei you qian duo jin you qian duo jin"

result = re.match("fan", str_1)
if result:
    print(result)
    print(result.span())
    print(result.group())

result = re.search("qian", str_1)
if result:
    print(result)

result = re.findall("qian", str_1)
if result:
    print(result)