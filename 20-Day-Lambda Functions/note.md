# Lambda Functions in Python

## Introduction

In Python, a **lambda function** is a small anonymous function without a name.

It is defined using the `lambda` keyword and has the following syntax:

```python
lambda arguments: expression
```

Lambda functions are often used when a small function is required for a short period of time.

They are commonly used as arguments to higher-order functions such as:

- `map()`
- `filter()`
- `reduce()`

---

## Basic Example

### Regular Function

```python
# Function to double the input
def double(x):
    return x * 2
```

### Equivalent Lambda Function

```python
lambda x: x * 2
```

The lambda function has the same functionality as the `double()` function.

However, the lambda function is **anonymous**, meaning it does not have a name.

---

## Assigning a Lambda Function to a Variable

Although lambda functions are anonymous, you can assign them to a variable.

```python
double = lambda x: x * 2

print(double(5))
```

### Output

```text
10
```

---

## Lambda Function with Multiple Arguments

Lambda functions can accept multiple arguments.

### Regular Function

```python
# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y
```

### Equivalent Lambda Function

```python
lambda x, y: x * y
```

### Example

```python
multiply = lambda x, y: x * y

print(multiply(4, 5))
```

### Output

```text
20
```

---

## Lambda Functions and Expressions

Lambda functions are limited to a **single expression**.

They cannot contain multiple statements like regular functions.

### Example

```python
lambda x, y: print(f"{x} * {y} = {x * y}")
```

This is valid because `print()` is a single expression.

---

## Using Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

### Output

```text
[2, 4, 6, 8, 10]
```

---

## Using Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
```

### Output

```text
[2, 4, 6]
```

---

## Summary

- Lambda functions are small anonymous functions.
- They are defined using the `lambda` keyword.
- Syntax:

```python
lambda arguments: expression
```

- Lambda functions can take multiple arguments.
- They are limited to a single expression.
- They are commonly used with higher-order functions such as:
  - `map()`
  - `filter()`
  - `reduce()`