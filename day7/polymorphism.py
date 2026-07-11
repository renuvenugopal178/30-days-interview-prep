
#method overriding

class Animal:
    def sound(self):
        print("animal sound")

class Dog(Animal):
    def sound(self):
        print("bark")

class Cat(Animal):
    def sound(self):
        print("meow")

dog = Dog()
dog.sound()
cat =   Cat()
cat.sound()
#polymorphism