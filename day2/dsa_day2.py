# Day 2: Arrays, Strings, Sorting, and Searching


def max_profit(prices):
    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices[1:]:
        minimum_price = min(minimum_price, price)
        current_profit = price - minimum_price
        maximum_profit = max(maximum_profit, current_profit)

    return maximum_profit


def move_zeroes(nums):
    insert_position = 0

    for number in nums:
        if number != 0:
            nums[insert_position] = number
            insert_position += 1

    while insert_position < len(nums):
        nums[insert_position] = 0
        insert_position += 1

    return nums


def is_anagram(first, second):
    if len(first) != len(second):
        return False

    frequency = {}

    for character in first:
        frequency[character] = frequency.get(character, 0) + 1

    for character in second:
        if character not in frequency:
            return False

        frequency[character] -= 1

        if frequency[character] < 0:
            return False

    return True


def first_unique_character(text):
    frequency = {}

    for character in text:
        frequency[character] = frequency.get(character, 0) + 1

    for index, character in enumerate(text):
        if frequency[character] == 1:
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
            left = middle + 1
        else:
            right = middle - 1

    return -1


print("Maximum profit:", max_profit([7, 1, 5, 3, 6, 4]))
print("Move zeroes:", move_zeroes([0, 1, 0, 3, 12]))
print("Valid anagram:", is_anagram("anagram", "nagaram"))
print("First unique character:", first_unique_character("loveleetcode"))
print("Binary search:", binary_search([1, 3, 5, 7, 9, 11], 7))