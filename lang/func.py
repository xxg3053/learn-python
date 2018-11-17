a = 1.2345
print(round(a, 3)) #

# 实现两个数字相加
# 打印输入的参数

def add(x, y):
    result = x + y
    return result

# 递归调用，python默认有最大次数限制995次  Previous line repeated 995 more times
# 使用sys.setrecursionlimit() 改变最大限制
#def print(code):
    #print(code)
    pass

# print(add(1, 2))

# x,y 为形参
# 必须参数
def swap(x, y):
    return y, x

sp = swap(1, 2)
print(type(sp)) # 返回元组
print(sp[0], sp[1]) # 不建议使用该方式取值

sp1, sp2 = swap(1, 2) # 多个变量接收
print(sp1, sp2)

# 关键字参数
# 增加代码可读性
def swap1(x=3, y=6):
    return y, x

print(swap(y=1, x=2))


"""
函数式编程
"""

# 闭包 = 函数 + 环境变量
def curve_pre():
    a = 10
    def curev(x):
        return a * x
    return curev

a = 11 # a不受影响
f = curve_pre()
print(f(1))

# 匿名函数 lambda