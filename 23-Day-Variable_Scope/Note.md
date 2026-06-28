# Python Variable Scope and Lifetime

In Python, every variable has two important characteristics:

* **Scope** – Defines where a variable can be accessed within a program.
* **Lifetime** – Defines how long a variable exists in memory.

Variables are created when they are first assigned a value. Local variables are created when a function is called and are automatically destroyed when the function finishes execution. Understanding variable scope is essential for writing clean, organized, and error-free Python programs.

---

# Types of Variable Scope in Python

Python primarily provides two types of variable scope:

## 1. Local Scope

A variable declared inside a function is called a **local variable**. It can only be accessed within that function. Once the function completes its execution, the local variable is removed from memory.

### Example

```python
def greet():
    message = "Hello!"
    print(message)

greet()
# print(message)  # Error: message is not defined
```

In this example, `message` exists only inside the `greet()` function.

---

## 2. Global Scope

A variable declared outside all functions is called a **global variable**. Global variables are accessible throughout the program, including inside functions (unless shadowed by a local variable with the same name).

### Example

```python
name = "Python"

def display():
    print(name)

display()
print(name)
```

**Output**

```
Python
Python
```

The variable `name` is global, so it can be accessed both inside and outside the function.

---

# Local Variables vs Global Variables

Before comparing them, let's briefly review what a variable is.

A **variable** is a named memory location used to store data. Values are assigned using the assignment operator (`=`).

### Example

```python
x = 5
message = "Hello, World!"
```

Now let's understand the difference between local and global variables.

| Local Variable                       | Global Variable                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------- |
| Declared inside a function           | Declared outside all functions                                                         |
| Accessible only within that function | Accessible throughout the program                                                      |
| Created when the function is called  | Created when the program starts executing (or when first assigned at the global level) |
| Destroyed when the function finishes | Exists until the program terminates                                                    |

---

# Example: Local and Global Variables

```python
x = 10      # Global variable

def my_function():
    y = 5   # Local variable
    print("Inside function:", y)

my_function()

print("Global variable:", x)

# print(y)   # Error: y is not defined
```

**Output**

```
Inside function: 5
Global variable: 10
```

### Explanation

* `x` is a **global variable**, so it can be accessed anywhere in the program.
* `y` is a **local variable**, so it exists only inside `my_function()`.
* Attempting to access `y` outside the function raises a **NameError** because the variable no longer exists.

---

# The `global` Keyword

Normally, assigning a value to a variable inside a function creates a **new local variable**, even if a global variable with the same name already exists.

To modify a global variable from inside a function, Python provides the **`global`** keyword.

### Syntax

```python
global variable_name
```

---

# Example: Modifying a Global Variable

```python
x = 10      # Global variable

def my_function():
    global x
    x = 5    # Modifies the global variable

my_function()

print(x)
```

**Output**

```
5
```

### Explanation

* The statement `global x` tells Python to use the global variable `x` instead of creating a new local variable.
* Therefore, the assignment `x = 5` changes the value of the global variable.

---

# What Happens Without `global`?

```python
x = 10

def my_function():
    x = 5

my_function()

print(x)
```

**Output**

```
10
```

### Explanation

Without the `global` keyword, Python creates a new local variable `x` inside the function. The global variable remains unchanged.

---

# Best Practices

* Prefer **local variables** whenever possible because they make code easier to understand and maintain.
* Use **global variables** only when multiple functions genuinely need to share the same data.
* Avoid modifying global variables inside functions unless absolutely necessary, as excessive use of global variables can make programs difficult to debug and maintain.
* Choose meaningful variable names to improve code readability.

---

# Summary

* **Scope** determines where a variable can be accessed.
* **Lifetime** determines how long a variable exists.
* **Local variables** are declared inside functions and are accessible only within those functions.
* **Global variables** are declared outside functions and can be accessed throughout the program.
* The **`global` keyword** allows a function to modify a global variable.
* Using local variables and minimizing the use of global variables leads to cleaner, more maintainable Python code.
