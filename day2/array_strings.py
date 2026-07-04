numbers = [10, 20, 30, 40, 50]

print("first item:", numbers[0])
print("last item:", numbers[4])

numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)

print("updated array:", numbers)
print("length:", len(numbers))
print("sum:", sum(numbers))
print("maximum:", max(numbers))
print("minimum", min(numbers))

#string

name = "renu venugopal"

print("lowercase:", name.lower())
print("uppercase:", name.upper())
print("length:", len(name))
print("first character:", name[0])
print("last character:", name[-1])
print("first four character:", name[:4])
print("contains renu:", "renu" in name)

updated_name = name.replace("renu", "Renu")
print("updated name:", updated_name)
