def is_valid_parentheses(text):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"

    }

    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack[-1] != pairs[character]:
                return False
        
            stack.pop()

    return len(stack) == 0

print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))      # False
print(is_valid_parentheses("([)]"))    # False