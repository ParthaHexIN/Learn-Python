# Function Arguments & Return Values

## Introduction

Functions can take **parameters (arguments)** as input and **return values** as output.

Arguments allow functions to work with different data, while the `return` statement sends a result back to the caller.

---

# Types of Arguments

Python supports different types of arguments:

1. Positional Arguments
2. Default Arguments
3. Keyword Arguments

---

## 1. Positional Arguments

In positional arguments, values are passed to the function in the same order as the parameters are defined.

### Example

```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### Output

```text
8
```

### Explanation

- `5` is assigned to `a`
- `3` is assigned to `b`
- The function returns `5 + 3`, which is `8`

---

## 2. Default Arguments

Default arguments provide a default value to a parameter.

If no argument is passed, the default value is used.

### Example

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
```

### Output

```text
Hello, Guest!
```

### Example with Custom Value

```python
print(greet("Alice"))
```

### Output

```text
Hello, Alice!
```

### Explanation

- If no argument is given, `"Guest"` is used.
- If an argument is provided, it replaces the default value.

---

## 3. Keyword Arguments

In keyword arguments, you specify the parameter names while calling the function.

The order of arguments does not matter.

### Example

```python
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")
```

### Output

```text
Name: Bob, Age: 20
```

### Explanation

- `name="Bob"` assigns `"Bob"` to `name`
- `age=20` assigns `20` to `age`
- The order can be changed because parameter names are explicitly mentioned.

---

# Return Values

The `return` statement sends a value back from a function.

### Example

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

### Output

```text
25
```

---

# Summary

- Functions can accept arguments and return values.
- **Positional arguments** depend on the order of values.
- **Default arguments** use predefined values if no argument is passed.
- **Keyword arguments** use parameter names and do not depend on order.
- The `return` statement sends a result back to the caller.