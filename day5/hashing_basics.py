student = {
    "name": "Renu",
    "department": "Csd",
    "cgpa": 7.8
}

print("name:",student["name"])
print("department:", student["department"])

student["college"] = "GECK"

print("updated student:", student)

skills = {"python", "java", "python","SQL"}

print("skills:", skills)
print("does python exist?", "python" in skills)
print("does c++ exist?", "c++" in skills)

skills.add("machine learning")
skills.remove("java")

print("updated skills:", skills)


#using a list
student_id = [101, 102, 103, 104] 
target = 103 

for id in student_id: 
    if id == target: 
        print("Found")

student_ids = {101, 102, 103, 104}
target = 103

if target in student_ids:
    print("found")

def frequency_count(items):
    frequency = {}

    for item in items:
        frequency[item] = frequency.get(item, 0) + 1
        
    return frequency
    
numbers = [1, 2, 2, 3, 1, 2, 4]
print(frequency_count(numbers))


def word_frequency(text):
    frequency = {}

    for word in text.lower().split():
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

name = "apple, banana, apple!, orange, banana, apple. "
print(word_frequency(name))