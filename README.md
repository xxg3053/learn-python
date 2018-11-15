# Python

## 安装模块
```
pip install 
```

## 基础数据类型
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/base.go)
- Number 数字（整数、小数）  
- int 整数  
- float 浮点数   
其他语言： 单精度float, 双精度double   
其他语言：short, int, long   
- 列表
```
[1, 2, -1, 4, 'a', True]
```


## 变量与运算
- 使用=赋值
- 变量名包含：字母、数字、_
- 变量名首字符不能是数字

## 分支、循环、条件与枚举
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/branch.go)


## 包、模块、函数与变量作用域
- 包(文件夹) - 模块 - 类
- 命名空间
- --ini--.py是文件夹变成包
- 导入
```
# 同级目录
import module_name
# 不同包下模块
import namesapce.module_name
# 模块别名
import namespace.module_name as m

from namespace import module_name
# 导入所有变量，* 可以使用__all__=[]来控制
from namespace.module_name import *
# 导入多个变量
from namespace.module_name import val1，val2

```
##### __init__.py
```__init__.py```文件作用：   
- 将文件夹变成包
- 导入包的时候首先执行该文件
- 使用__all__来控制那些模块能导出
- 公共库可以在此导入


## Python函数

## 面向对象

## 正则、JSON

## 高级语法

## 函数式编程

## 爬虫

## Pythonic