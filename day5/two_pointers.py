def reverse_text(text):
    characters = list(text)

    left = 0
    right = len(characters) - 1

    while left < right:
        characters[left], characters[right] = characters[right], characters[left]


        left += 1
        right -= 1

    return "".join(characters)

print(reverse_text("renu"))


def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        current_sum = numbers[left]+numbers[right]
        

        if current_sum == target:
            return[left, right]
        
        else:
            right -= 1

    return []

print(two_sum_sorted([2, 7, 11, 15], 9))