# # Example 1: Add Two Numbers Using User Input
add = lambda a, b: a + b
x =int (input("Enter first number:"))
y = int (input("Enter Second number:"))
print ("sum=",add(x,y))


# # Example 2: Square a User Input
square = lambda x: x * x
num = int(input("Enter your Number :"))
print ("square=", square(num))


# Example 3: Check Even or Odd with User Input
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
num = int(input("Enter a number: "))
print(is_even(num))

