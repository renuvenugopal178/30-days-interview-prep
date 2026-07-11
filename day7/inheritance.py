class Person:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

class Student(Person):
    pass
student = Student("renu")
student.display()

class Teacher(Person):
    pass
teacher = Teacher("Jayasree")
teacher.display()