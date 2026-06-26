#1. Factorial
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))
'''

#2. Sum of First N Numbers

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

n = int(input("Enter N: "))
print("Sum =", sum_numbers(n))


