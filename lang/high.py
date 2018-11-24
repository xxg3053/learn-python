from functools import reduce

import time


def add(x, y):
    return x + y

# 匿名函数
f = lambda x, y: x + y


# 三元表达式
x, y = 2,3
r = x if x > y else y

# map
list_x = [1, 2, 3, 4]
m = map(lambda x: x*x, list_x)
print(list(m)) # [1, 4, 9, 16]

# map 多个参数
list_y = [2, 3, 4, 5]
m2 = map(lambda  x, y: x*x + y , list_x, list_y)
print(list(m2)) # [3, 7, 13, 21]

# reduce 连续计算
r = reduce(lambda x, y: x+y, list_x)
print(r) # 10
r1 = reduce(lambda x, y: x+y, list_x, 10)
print(r) # 20 10为初始值


# filter
list_x = [0, 1, 0, 2, 0, 1]
f = filter(lambda x: True if x==1 else False, list_x) # 把1选出来
print(list(f)) # [1, 1]



# 装饰器（注解）
def print_current_time(func):
    def wrapper(*agrs, **kw): # 可变参数
        print('func start')
        func(*agrs, **kw)
        print('func end')
    return wrapper

@print_current_time
def pf(name):
    print('this is a func ', name)

pf('pf')
