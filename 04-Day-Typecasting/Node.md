# Typecasting in Python

## What is Typecasting?

Typecasting means **converting one data type into another data type**.

In Python, sometimes we need to convert data types so that operations can work correctly. Python provides built-in functions to perform this conversion.

For example, converting a **string to an integer**, or an **integer to a float**.

---

# Example of Typecasting

```python
x = "10"      # string
y = int(x)    # convert string to integer

print(y)
print(type(y))
```

Output:

```
10
<class 'int'>
```

Here:

* `x` is a **string**
* `int(x)` converts it into an **integer**

---

# Common Typecasting Functions

Python provides several built-in functions for type conversion.

## 1. int()

Converts a value into an **integer**.

Example:

```python
num = int("25")
print(num)
```

---

## 2. float()

Converts a value into a **floating-point number**.

Example:

```python
num = float(10)
print(num)
```

Output:

```
10.0
```

---

## 3. str()

Converts a value into a **string**.

Example:

```python
num = 50
text = str(num)

print(text)
print(type(text))
```

---

## 4. bool()

Converts a value into a **Boolean value** (`True` or `False`).

Example:

```python
print(bool(1))   # True
print(bool(0))   # False
```

---

# Another Practical Example

```python
age = "21"

age_number = int(age)

print(age_number + 5)
```

Output:

```
26
```

Without typecasting, Python would produce an error because `"21"` is a string.

---

# Important Notes

* Typecasting helps avoid **data type errors**.
* Python supports **automatic type conversion** in some cases, but explicit conversion is often safer.
* Always ensure the value can actually be converted (for example `"abc"` cannot be converted to an integer).
