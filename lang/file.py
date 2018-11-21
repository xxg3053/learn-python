import os


# 特点：一次性读取整个文件；自动将文件内容分析成一个行的列表。
def read_file_lines():
    file = os.path.join(os.getcwd(), 'base.py')
    lines = None
    with open(file, 'r', encoding='utf-8') as reader:
        lines = reader.readlines()
    print(lines)



# readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
# 比readlines慢得多
def read_file_line():
    try:
        file = os.path.join(os.getcwd(), 'base.py')
        with open(file, 'r', encoding='utf-8') as reader:
            for line in reader:
                print(line)
    finally:
        reader.close()


# 特点是：读取整个文件，将文件内容放到一个字符串变量中。
# 劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。
def read_file():
    file = os.path.join(os.getcwd(), 'base.py')
    with open(file, 'r', encoding='utf-8') as reader:
        print(reader.read())


def write_file():
    file = os.path.join(os.getcwd(), 'test.txt')
    with open(file, 'w', encoding='utf-8') as w:
        w.write('hello world')



read_file_lines()