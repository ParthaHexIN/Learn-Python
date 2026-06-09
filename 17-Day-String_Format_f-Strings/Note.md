# Using the .format() Method in Python

## Introduction

The `.format()` method is used to insert values into a string using placeholders `{}`.

It allows you to create dynamic strings by replacing placeholders with variables or values.

---

## Syntax

```python
string.format(value1, value2, ...)
```

---

## Example

```python
name = "Partha"
age = 20

print("My name is {} and I am {} years old.".format(name, age))
```
# f-Strings (Formatted String Literals)



Introduced in **Python 3.6**, f-strings (formatted string literals) are the most concise and readable way to format strings in Python.

They allow you to directly embed variables and expressions inside a string using curly braces `{}`.

---

## Example

```python
name = "Partha"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

# Using Expressions in f-Strings

One of the most powerful features of f-strings is that you can perform calculations and evaluate expressions directly inside the curly braces `{}`.

Python evaluates the expression and inserts the result into the string.

---
## Example
```python
x = 10
y = 5

print(f"The sum of {x} and {y} is {x + y}")
```
### Formatting Numbers
```python
pi = 3.14159265
print(f"Pi rounded to 2 decimal places: {pi:.2f}")
```

### Padding and Alignment
```python
text = "Python"
print(f"{text:>10}")  # Right align
print(f"{text:<10}")  # Left align
print(f"{text:^10}")  # Center align
```

## Important Notes
* Escape Sequences: Use `\n`, `\t`, `\'`, `\"`, and `\\` to handle special characters in strings.
* Raw Strings: Use r"string" to prevent escape sequence interpretation.
* String Encoding & Decoding: Use .encode() and .decode() to work with different text encodings.
* String Immutability: Strings in Python are immutable, meaning they cannot be changed after creation.
* Performance Considerations: Using ''.join(list_of_strings) is more efficient than concatenation in loops.
## Summary
* Python provides various string methods for modification and analysis.
* Case conversion, trimming, finding, replacing, splitting, and joining are commonly used.
* Functions like `len()`, `ord()`, and `chr()` are useful for working with string properties.
* `.format()` allows inserting values into placeholders.
* f-strings provide an intuitive and readable way to format strings.
* f-strings support expressions, calculations, and formatting options.