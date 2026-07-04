numbers = [64, 34, 25, 12, 22, 11, 90]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("original:", numbers)
print("ascending:", ascending)
print("descending:", descending)

#linear search
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1


def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left =  middle + 1

        else:
            right = middle - 1
    
    return -1

sorted_numbers = sorted(numbers)

print("linear search for 22:", linear_search(numbers, 22))
print("binary search for 22:", binary_search(sorted_numbers, 22))
print("binary search for 100:", binary_search(sorted_numbers,100))
    

