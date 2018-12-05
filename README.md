# Python

## 安装模块
```
pip install 
```

## 基础数据类型
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/base.py)
- Number 数字（整数、小数）  
- int 整数  
- float 浮点数   
其他语言： 单精度float, 双精度double   
其他语言：short, int, long   
- 列表
```
[1, 2, -1, 4, 'a', True]
```
dict list str int float True False None  

## 变量与运算
- 使用=赋值
- 变量名包含：字母、数字、_
- 变量名首字符不能是数字

## 分支、循环、条件与枚举
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/branch.py)


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
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/func.py)

- 功能性
- 隐藏细节
- 避免编写重复代码
```
round(1.2435, 3) #保留三位小数

def funcname(parameter_list)
    pass
# 1 参数列表可以没有
# 2 return value / None
```
- 没有限制返回类型
- return 之后代码不执行
- 可返回多个值，用,连接
- 多个值返回结果，用单个变量获取返回类型为元组
- 多个返回结果，可以使用过个值接收，序列解包

###### 函数参数
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/func.py)
- 必须参数
- 关键字参数
- 默认参数

## 面向对象
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/oop.py)

- 有意义的面向对象的代码

## 正则、JSON
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/regex.py)

- 特殊的字符序列

## 高级语法
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/high.py)
- map
- reduce
- filter
- 装饰器


## 函数式编程
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/func.py)

- 闭包

## 爬虫
[代码](https://github.com/xxg3053/learn-python/blob/master/crawler/spider.py)
- 爬取html信息
- 正则分析需要的数据
- 下载图片

## Pythonic

#### 日志分析

#### 文件读写
[代码](https://github.com/xxg3053/learn-python/blob/master/lang/file.py)


#### excel读写
[代码](https://github.com/xxg3053/learn-python/blob/master/excel/excel.py)

#### 数据分析
[说明](https://github.com/xxg3053/learn-python/blob/master/DA/README.md)

#### pypi
1. 注册pypi账号 https://pypi.org/user/Kenfo/   
2. 编写setup.py文件
3. 执行如下命令    
```
# 检查setup.py文件
python setup.py check
# 打包上传
python setup.py register sdist upload
```
4. 安装上传的包   
由于本地默认配置的douban的源，因此安装自己的包：
```
pip install -i https://pypi.org/simple/  kenfotools

# 查看已安装包版本信息
pip freeze
# 卸载
pip uninstall
```
 
