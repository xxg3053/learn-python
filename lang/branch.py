"""
推荐变量小写，常量大写

条件控制
"""

ACCOUNT = 'kenfo'
PASSWORD = '123456'

print("please input your account: ")
user_account = input()

print('please input your password: ')
user_password = input()

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
for x in range(0, 10, 2):
    print(x, end=' | ')