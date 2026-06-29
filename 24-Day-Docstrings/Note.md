# Python Docstrings – Writing Function Documentation

A **docstring** (documentation string) is a special string used to describe the purpose, behavior, parameters, and return value of a **function**, **class**, **module**, or **method**. Docstrings make code easier to understand, maintain, and use.

In Python, a docstring is written immediately after the definition of a function, class, or module using **triple quotation marks** (`""" """` or `''' '''`).

Python automatically stores the docstring in the object's `__doc__` attribute, allowing it to be accessed programmatically.

---

# Why Use Docstrings?

Docstrings provide several important benefits:

* Explain the purpose of a function or class.
* Improve code readability and maintainability.
* Help other developers understand your code.
* Enable IDEs and documentation tools to display helpful information.
* Serve as built-in documentation for your program.

---

# Basic Docstring Example

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)
```

**Output**

```text
Returns the sum of two numbers.
```

### Explanation

* The string enclosed in triple quotes is the function's **docstring**.
* The expression `add.__doc__` retrieves and prints the documentation associated with the function.

---

# Writing Professional Docstrings

For simple functions, a one-line docstring is sufficient. However, for functions that perform more complex tasks, it is recommended to write a **multi-line docstring** that describes:

* What the function does
* Its parameters
* Its return value
* Any exceptions it may raise (if applicable)

### Example

```python
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two input numbers.
    """
    return a + b
```

---

# Accessing a Docstring

A function's documentation can be accessed using the `__doc__` attribute.

```python
def greet():
    """Displays a welcome message."""
    print("Welcome!")

print(greet.__doc__)
```

**Output**

```text
Displays a welcome message.
```

---

# Docstring vs Comments

| Docstrings                                                        | Comments                                    |
| ----------------------------------------------------------------- | ------------------------------------------- |
| Explain the purpose and usage of functions, classes, and modules. | Explain specific lines or sections of code. |
| Written using triple quotes (`""" """`).                          | Written using the `#` symbol.               |
| Stored in the object's `__doc__` attribute.                       | Ignored by Python during execution.         |
| Can be viewed using `help()` or `__doc__`.                        | Cannot be accessed programmatically.        |

---

# Best Practices for Writing Docstrings

* Begin with a short, clear summary of the function.
* Use complete and meaningful sentences.
* Describe all parameters and their expected data types.
* Clearly specify the return value and its data type.
* Mention any exceptions raised by the function when necessary.
* Keep the documentation concise, accurate, and up to date.

---

# Summary

* A **docstring** is a built-in documentation string used to describe Python functions, classes, methods, and modules.
* Docstrings are written immediately below the definition using triple quotes.
* They can be accessed through the `__doc__` attribute or viewed using the `help()` function.
* Well-written docstrings improve code readability, maintainability, and collaboration, making them an essential part of professional Python programming.
