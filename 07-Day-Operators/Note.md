# Types of Operators in Python

Operators are symbols used to perform operations on variables and values.

---

# 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Meaning        | Example       |
| -------- | -------------- | ------------- |
| `+`      | Addition       | `5 + 3 = 8`   |
| `-`      | Subtraction    | `5 - 3 = 2`   |
| `*`      | Multiplication | `5 * 3 = 15`  |
| `/`      | Division       | `5 / 2 = 2.5` |
| `//`     | Floor Division | `5 // 2 = 2`  |
| `%`      | Modulus        | `5 % 2 = 1`   |
| `**`     | Exponent       | `2 ** 3 = 8`  |

### Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

# 2. Comparison Operators

Used to compare two values. Result is always **True or False**.

| Operator | Meaning               | Example          |
| -------- | --------------------- | ---------------- |
| `==`     | Equal to              | `5 == 5 → True`  |
| `!=`     | Not equal to          | `5 != 3 → True`  |
| `>`      | Greater than          | `5 > 3 → True`   |
| `<`      | Less than             | `5 < 3 → False`  |
| `>=`     | Greater than or equal | `5 >= 5 → True`  |
| `<=`     | Less than or equal    | `5 <= 3 → False` |

### Example

```python
x = 10
y = 5

print(x > y)
print(x == y)
```

---

# 3. Logical Operators

Used to combine multiple conditions.

| Operator | Meaning               | Example                  |
| -------- | --------------------- | ------------------------ |
| `and`    | True if both are true | `True and False → False` |
| `or`     | True if one is true   | `True or False → True`   |
| `not`    | Reverse result        | `not True → False`       |

### Example

```python
a = 10

print(a > 5 and a < 20)
print(a > 5 or a > 20)
print(not(a > 5))
```

---

# 4. Assignment Operators

Used to assign values to variables.

| Operator | Example  | Meaning      |
| -------- | -------- | ------------ |
| `=`      | `x = 5`  | Assign value |
| `+=`     | `x += 3` | x = x + 3    |
| `-=`     | `x -= 2` | x = x - 2    |
| `*=`     | `x *= 2` | x = x * 2    |
| `/=`     | `x /= 2` | x = x / 2    |

### Example

```python
x = 5
x += 3
print(x)
```

---

# 5. Membership Operators

Used to check if a value exists in a sequence (like list, string).

| Operator | Meaning              | Example                     |
| -------- | -------------------- | --------------------------- |
| `in`     | Value exists         | `"a" in "apple" → True`     |
| `not in` | Value does not exist | `"x" not in "apple" → True` |

### Example

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)
print("grape" not in fruits)
```

---

# 6. Identity Operators

Used to compare memory locations of two objects.

| Operator | Meaning         | Example      |
| -------- | --------------- | ------------ |
| `is`     | Same object     | `x is y`     |
| `is not` | Not same object | `x is not y` |

### Example

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)   # True
print(x is z)   # False
```

---

# Important Notes

* Arithmetic operators work with numbers.
* Comparison operators return **Boolean values**.
* Logical operators are used in conditions.
* Assignment operators update variable values.
* Membership operators check presence in sequences.
* Identity operators check whether two variables refer to the same object.
