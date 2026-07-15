# Squares of Numbers
numbers = {x:x**2 for x in range (1,11)}
print(numbers)

# cubes of number
cubes = {x:x**3 for x in range (1,11)}
print (cubes)

# even numbers only
even = {x:x**2 for x in range (1,11) if x % 2==0}
print (even)

# odd number only 
odd ={x:x**2 for x in range (1,11) if x % 2!=0}
print (odd)

# Convert Celsius to Fahrenheit
celsius = [0,10,20,30,40,50]
temperature = {c:(c*9/5) +32 for c in celsius}
print (temperature)