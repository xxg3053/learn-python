import os

import kenfotools


class FileTools:
    # 特点：一次性读取整个文件；自动将文件内容分析成一个行的列表。
    def read_file_lines(self, filename):
        lines = None
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as reader:
                    lines = reader.readlines()
            finally:
                reader.close()
        return lines



    # readline()方法每次读取一行；返回的是一个字符串对象，保持当前行的内存
    # 比readlines慢得多
    def read_file_line(self, filename, func):
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as reader:
                    for line in reader:
                        func(line)
            finally:
                reader.close()


    # 特点是：读取整个文件，将文件内容放到一个字符串变量中。
    # 劣势是：如果文件非常大，尤其是大于内存时，无法使用read()方法。
    def read_file(self, filename):
        file = None
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as reader:
                    file = reader.read()
            finally:
                reader.close()
        return file


    def write_file(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as w:
            w.write(data)


    def write_file_feed(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as w:
            w.write(data)
            w.write('\n')


    def remove(self, filename):
        if os.path.exists(filename):
            os.remove(filename)

    def empty(self, filename):
        self.write_file(filename, '')


file = os.path.join(os.getcwd(), 'test.txt')

ft = FileTools()
#print(ft.read_file_lines(file))
#ft.read_file_line(file, lambda line:print(line))

print(kenfotools.file.read_file_lines(file))