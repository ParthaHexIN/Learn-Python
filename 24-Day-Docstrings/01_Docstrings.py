# def greet():
#     """Prints a welcome message."""
#     print("Welcome to Python!")

# greet()

# print(greet.__doc__)


# Multi-Line Function Docstring
def add(a, b):
    """
    Adds two numbers and returns their sum.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

print(add(10, 20))
print(add.__doc__)