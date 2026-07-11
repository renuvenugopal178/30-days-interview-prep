class Student:

    def __init__(self,name,age):

        self.name = name
        self.age = age
#object creation
student1 = Student("renu", 22)
print(student1.name)
print(student1.age)

student2 = Student("anu", 21)
print(student2.name)
print(student2.age)

#method calling
class Student:

    def __init__(self,name,age):

        self.name=name

        self.age=age

    def introduce(self):

        print("Hi")

        print("My name is",self.name)

        print("Age =",self.age)

student1 = Student("Renu",22)

student1.introduce()