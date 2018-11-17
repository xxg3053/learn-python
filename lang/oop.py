
class Student():
    name = ''
    age = 0

    def __init__(self, name, age): # 构造函数，实例化时自动调用， 只能return None，不能return其他
        self.name = name
        self.age = age

    # 行为与特征
    def print_file(self):
        print('name=', self.name, 'age=', self.age)


student = Student('kenfo', 1)
student.print_file()
