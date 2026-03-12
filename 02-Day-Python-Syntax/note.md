# Understanding Python Syntax

Python syntax refers to the rules that define how Python programs are written and structured. Unlike many other programming languages, Python focuses on readability and simplicity, which makes it easier for beginners to learn.

---

## 1. Indentation

Indentation means leaving spaces at the beginning of a line of code.  
In Python, indentation is very important because it defines a block of code.

Most programming languages use curly brackets `{ }`, but Python uses indentation instead.

Usually **4 spaces** are used for indentation.

### Example

```python
if 5 > 2:
    print("Five is greater than two")
```
Here the print() statement is indented, so Python knows it belongs to the if block.

If indentation is wrong, Python gives an error.

### ❌ Incorrect Example
```python
if 5 > 2:
print("Five is greater than two")
```
## 2. Whitespace

Whitespace refers to spaces, tabs, and blank lines in a program.

In Python, whitespace is used to improve readability and organize code properly.

### Example
```python
x = 10
y = 20
print(x + y)
```
Adding proper spaces makes code clean and easy to understand.

Whitespace does not affect the logic of most Python code except for indentation.

## 3. Statements

A statement is a single instruction that Python can execute.

Each line of Python code is usually a statement.

Example
```python
x = 10
y = 5
print(x + y)
```
Here:
```python
x = 10 → assignment statement

y = 5 → assignment statement

print(x + y) → output statement
``` 
Python also allows multiple statements on one line using semicolons.

Each line of code is a statement. You can write multiple statements on one line using a semicolon (;), but this is not recommended.
Example
```python
x = 5; y = 10; print(x + y)
```

However, writing one statement per line is recommended for readability.

# 4. Comments

Comments are notes written inside the code to explain what the program does.

Python ignores comments during execution.

## Single-line Comment
```python
# This is a comment
print("Hello")
```

## Multi-line Comment (commonly written like this)
```python
"""
This is a
multi-line comment
"""
```

Comments help programmers understand the code later and make programs easier to maintain.

# Notes from Instructor (Important Points)

- Python syntax is simple and readable

- Indentation is mandatory in Python

- Use 4 spaces for indentation

- Write one statement per line for better readability

- Use comments to explain code

- Avoid unnecessary whitespace but keep code clean