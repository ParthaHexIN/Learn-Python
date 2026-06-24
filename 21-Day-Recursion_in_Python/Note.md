# Recursion in python
Recursion is the process of defining something in terms of itself.

## Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
## Example:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
 
print(factorial(5))  # Output: 120
```

## Important Notes:
* Must have a base case to avoid infinite recursion.
* Used in algorithms like Fibonacci, Tree Traversals.
