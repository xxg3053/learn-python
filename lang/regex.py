import json
import re

a = 'c|C++|Jave|C#|Python|Javascript'

print(a.index('Python')>-1)
print('Python' in a)
print(a.find('Python1') > -1)

r = re.findall('Python', a)
print(r)
if len(r) > 0:
    print('字符串中不包含Python')

# 找出所有数字
b = 'ad234cad89s0f0dfds'
r = re.findall('\d', b)
print(r)
# 非数字
r = re.findall('\D', b)
print(r)


# json解析
json_str = '{"name":"kenfo"}'
m = json.loads(json_str)
print(m)
print(m["name"])

# 序列化
j = [{"name":"kenfo"}]
json_str = json.dumps(j)
print(json_str)