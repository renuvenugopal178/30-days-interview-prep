def countdown(number):
    if number == 0:
        print("done")
        return
    print(number) 
    countdown(number - 1)   


def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def sum_to_n(number):
    if number == 0:
        return 0
    
    return number + sum_to_n(number - 1)

countdown(5)
print("factorial of 5:", factorial(5))
print("sum from 1 to 5:", sum_to_n(5))




   