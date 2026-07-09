

def two_sum_brute_force(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
    return[]

nums = [2,7,11,15]
target = 9


result = two_sum_brute_force(nums,target)
print(result)

def two_sum(nums, target):
    seen = {}

    for index, number in enumerate(nums):
        required = target - number

        if required in seen:
            return [seen[required], index]
        
        seen[number]=index

    return[]

def valid_palindrome(text):
    cleaned = ""

    for character in text.lower():
        if character.isalnum():
            cleaned += character
    
    return cleaned == cleaned[::-1]

def contains_duplicate(nums):
    return len(nums) != len(set(nums))

def reverse_string(chars):
    left = 0
    right = len(chars)-1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -=1
    return chars


def max_subarray(nums):
    current_sum = nums[0]
    best_sum = nums[0]

    for number in nums[1:]:
        current_sum = max(number, current_sum + number)
        best_sum = max(best_sum, current_sum)

    return best_sum


print("Two Sum:", two_sum([2, 7, 11, 15], 9))
print("Valid Palindrome:", valid_palindrome("A man, a plan, a canal: Panama"))
print("Contains Duplicate:", contains_duplicate([1, 2, 3, 1]))
print("Reverse String:", reverse_string(["h", "e", "l", "l", "o"]))
print("Maximum Subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    
