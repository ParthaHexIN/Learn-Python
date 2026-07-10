numbers = [x for x in range(1, 6)]
print(numbers)


squares = [x**2 for x in range(1, 6)]
print(squares)



cubes = [x**3 for x in range(1, 6)]
print(cubes)


even = [x for x in range(1, 11) if x % 2 == 0]
print(even)


odd = [x for x in range(1, 11) if x % 2 != 0]
print(odd)


numbers = [1, 2, 3, 4, 5]
result = [x * 10 for x in numbers]
print(result)