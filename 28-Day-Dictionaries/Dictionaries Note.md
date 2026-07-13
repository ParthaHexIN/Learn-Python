# Dictionaries and Dictionary Methods in Python

## Introduction

A **dictionary** is a built-in Python data structure that stores data as **key-value pairs**.

Each **key** is unique and is used to access its corresponding **value**.

Dictionaries are:

- Ordered (Python 3.7 and later)
- Mutable (can be modified)
- Do not allow duplicate keys
- Provide fast lookups using keys

Dictionaries are created using curly braces `{}`.

---

## Characteristics of Dictionaries

- Store data as **key-value pairs**
- Keys must be unique
- Mutable
- Ordered (Python 3.7+)
- Fast access to values using keys

---

# Creating a Dictionary

## Example

```python
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

print(student)
```

### Output

```text
{'name': 'Alice', 'age': 21, 'grade': 'A'}
```

---

# Accessing Dictionary Values

Values are accessed using their keys.

### Example

```python
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A"
}

print(student["name"])
```

### Output

```text
Alice
```

---

# Modifying Dictionary Values

### Updating an Existing Value

```python
student = {
    "name": "Alice",
    "age": 21
}

student["age"] = 22

print(student)
```

### Output

```text
{'name': 'Alice', 'age': 22}
```

---

### Adding a New Key-Value Pair

```python
student["city"] = "New York"

print(student)
```

### Output

```text
{'name': 'Alice', 'age': 22, 'city': 'New York'}
```

---
