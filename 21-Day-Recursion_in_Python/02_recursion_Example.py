# 1. Print Numbers from 1 to N
'''
def numbers(n):
    if n == 0:
        return
    numbers(n - 1)
    print(n)

numbers(10)
'''

# 2. Factorial of a Number
'''
def number (n):
    if n == 0 or n == 1:
        return 1
    return n * number( n - 1 )

print (number(5))
'''

# 3. Sum of First N Numbers
'''
def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)
print (sum(5))
'''

# 4. Reverse a String
'''
def reverse_string(text):
    if len(text) == 0:
        return ""
    return reverse_string(text[1:]) + text[0]

print(reverse_string("PYTHON"))
'''


# 5. Fibonacci Series
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")

'''
# 6. Calculate Power
'''
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 5))
'''
# 7. Find Maximum Element in a List
'''
def find_max(arr, n):
    if n == 1:
        return arr[0]

    return max(arr[n - 1], find_max(arr, n - 1))

numbers = [10, 45, 8, 99, 23]
print(find_max(numbers, len(numbers)))
'''


#8.  Count Digits
'''
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))
'''
# 9. Sum of Digits

'''
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))
'''
# 10.Check Palindrome
'''
def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

print(palindrome("madam"))
'''
