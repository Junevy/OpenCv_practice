class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prt(self):
        return self.name

stu = Student('junevy', 23)
# stu.name = 'juenvy'
# stu.age = 26

print(stu.prt())