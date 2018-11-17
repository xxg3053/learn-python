"""
推荐变量小写，常量大写

条件控制
"""

ACCOUNT = 'kenfo'
PASSWORD = '123456'

print("please input your account: ")
user_account = 1 # input()

print('please input your password: ')
user_password = 2 # input()

if user_account == ACCOUNT and user_password == PASSWORD :
    print('success')
elif user_account != ACCOUNT:
    print('account is wrong')
else:
    print('fail')


"""
while 
"""

counter = 1

while counter <= 10:
    counter += 1
    print(counter)
else:
    print('while over')


"""
for
"""

arr = ['apple', 'origin', 'banana']

for i in arr:
    print(i)
else: # 如果使用break，则不会执行else
    print('for over')


# range函数
for x in range(3):
    print(x) # 0 1 2

for x in range(0, 10, 2):
    print(x, end=' | ') # 0 2 4 6 8


print()


"""
枚举  Enum
枚举类型、枚举的名字、枚举的值
单例模式
不需要实例化
"""

from enum import Enum
from enum import IntEnum,unique

# @unique
class VIP(Enum):
    yellow = 1
    green = 2
    black = 3
    red = 4


print(VIP.yellow) # 打印初VIP.yellow
print(VIP.yellow.name)
print(VIP.yellow.value)
# 遍历
for v in VIP:
    print(v) # VIP.yellow

for v in VIP.__members__:
    print(v) # yellow, green...

# 转枚举
print(VIP(1))