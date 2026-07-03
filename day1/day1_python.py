name = "Renu"
cgpa = 7.87
is_graduate = True

print(name)
print(cgpa)
print(is_graduate)


print(type(name))
print(type(cgpa))
print(type(is_graduate))

college = "Government Engineering College Kozhikode"
print(name + " studied at " + college)

#tuple : ordered and immutable
coordinates = (11.2588,75.7804)
print("Tuples:", coordinates)


#set: unique values only
languages = {"python", "java", "c"}
print("set:", languages)

#dictionary: key-value pairs

student = {
    "name": "Renu",
    "department": "CSD",
    "cgpa":7.8

}



student["college"] = "GECK"
print("Dictionary:",student)
print("student name:",student["name"])

#list"ordered and mutable

skills = ["python", " java", "React"]
skills.append("SQL")
skills[0] = "python programming"
print("List:", skills)

marks = 87

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 50:
    grade = "B"
else:
    grade = "fail"

print("grade:",grade)

def is_eligible_for_placement(cgpa):
    return cgpa >=7.0
  
print(is_eligible_for_placement(7.87))

skills = ["python","java", "react", "SQL"]

for skill in skills:
    print("learning:",skill)

count=1

while count <= 5:
    print("count:", count)
    count += 1

for skill in skills:
    if len(skill) > 4:
        print(skill)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

marks = [85,78,92,88]
average = calculate_average(marks)

print("average:", average)

def find_largest(numbers):
    return max(numbers)

def count_even_numbers(numbers):
    count=0

    for number in numbers:
        if number % 2 == 0:
            count+=1

    return count

def greet(name):
    return f"Hello, {name}"

print(find_largest([10,45,7,90]))
print(count_even_numbers([1,2,3,4,5,6]))
print(greet("Renu"))

text = "Hello python"

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("python","world"))
print(text.split())



def is_palindrome(text):
    cleaned = ""

    for character in text.lower():
        if character.isalnum():
            cleaned += character

    return cleaned == cleaned[::-1]

print(is_palindrome("Malayalam"))       # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Python"))          # 

def char_frequency(text):
    frequency = {}

    for character in text.lower():
        if character.isalpha():
           frequency[character]=frequency.get(character,0)+1

    return frequency

print(char_frequency("anomaly detection"))


try:
    number = int(input("enter a number:"))
    print("you entered:", number)
except ValueError:
    print("please enter a valid whole number")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 50:
            return "B"
        return "Fail"

    def introduce(self):
        return f"My name is {self.name} and my grade is {self.get_grade()}."

student1 = Student("Renu", 87)
student2 = Student("Anu", 74)

print(student1.introduce())
print(student2.introduce())