def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True
        
        seen.add(number)


    return False


print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))

def two_sum(numbers, target):
    seen = {}

    for index,number in enumerate(numbers):
        required = target - number

        if required in seen:
            return [seen[required], index]
        
        seen[number] =  index

    return []

print(two_sum([2, 7, 11, 15], 9))

def valid_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1

        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                      # False

def intersection(first, second):
    first_set = set(first)
    result = set()

    for number in second:
        if number in first_set:
            result.add(number)

    return list(result)


print(intersection([1, 2, 2, 1], [2, 2]))  # [2]

def length_of_longest_substring(text):
    last_seen = {}
    left = 0
    longest = 0

    for right, character in enumerate(text):
        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1

        last_seen[character] = right
        longest = max(longest, right - left + 1)

    return longest


print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3



# Day 5: Hashing and Two Pointers


def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False


def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        required = target - number

        if required in seen:
            return [seen[required], index]

        seen[number] = index

    return []


def valid_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1

        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


def intersection(first, second):
    first_set = set(first)
    result = set()

    for number in second:
        if number in first_set:
            result.add(number)

    return list(result)


def length_of_longest_substring(text):
    last_seen = {}
    left = 0
    longest = 0

    for right, character in enumerate(text):
        if character in last_seen and last_seen[character] >= left:
            left = last_seen[character] + 1

        last_seen[character] = right
        longest = max(longest, right - left + 1)

    return longest


print("Contains duplicate:", contains_duplicate([1, 2, 3, 1]))
print("Two Sum:", two_sum([2, 7, 11, 15], 9))
print("Valid palindrome:", valid_palindrome("A man, a plan, a canal: Panama"))
print("Intersection:", intersection([1, 2, 2, 1], [2, 2]))
print("Longest substring:", length_of_longest_substring("abcabcbb"))