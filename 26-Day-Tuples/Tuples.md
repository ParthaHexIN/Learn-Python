# Tuples and Operations on Tuples

## Introduction

A **tuple** is an ordered collection of items in Python.

Unlike lists, tuples are **immutable**, which means their elements **cannot be changed** after the tuple is created.

Tuples can store:

- Integers
- Floating-point numbers
- Strings
- Boolean values
- Mixed data types
- Other tuples

Tuples are created using parentheses `()`.

---

## Characteristics of Tuples

- Ordered
- Immutable (cannot be modified after creation)
- Allow duplicate values
- Can store multiple data types
- Faster than lists for read-only data

---

# Creating a Tuple

## Example

```python
my_tuple = (10, 20, 30)

print(my_tuple)
```

### Output

```text
(10, 20, 30)
```

---

## Tuple with One Element

A single-element tuple **must** include a comma.

### Example

```python
single_element = (5,)

print(single_element)
```

### Output

```text
(5,)
```

Without the comma:

```python
single_element = (5)

print(type(single_element))
```

### Output

```text
<class 'int'>
```

---

# Accessing Tuple Elements

Tuple elements are accessed using indexes.

### Example

```python
my_tuple = (10, 20, 30)

print(my_tuple[1])
```

### Output

```text
20
```

---

## Negative Indexing

```python
my_tuple = (10, 20, 30)

print(my_tuple[-1])
```

### Output

```text
30
```

---

# Tuple Unpacking

Tuple unpacking allows you to assign tuple elements to multiple variables.

### Example

```python
my_tuple = (10, 20, 30)

a, b, c = my_tuple

print(a, b, c)
```

### Output

```text
10 20 30
```

---

# Common Tuple Methods

| Method | Description | Example | Output |
|--------|-------------|---------|--------|
| `count(x)` | Returns the number of times `x` appears in the tuple. | `(1, 2, 2, 3).count(2)` | `2` |
| `index(x)` | Returns the index of the first occurrence of `x`. | `(10, 20, 30).index(20)` | `1` |

---

## Example: `count()`

```python
my_tuple = (1, 2, 2, 3, 4)

print(my_tuple.count(2))
```

### Output

```text
2
```

---

## Example: `index()`

```python
my_tuple = (1, 2, 2, 3, 4)

print(my_tuple.index(3))
```

### Output

```text
3
```

---

# Why Use Tuples?

Tuples are useful because they are:

- Faster than lists for storing fixed data.
- Immutable, making them safe from accidental modification.
- Hashable (when all their elements are hashable), so they can be used as dictionary keys.
- Suitable for storing data that should not change.

---

## Example: Tuple as a Dictionary Key

```python
student = {
    ("Partha", 101): "A"
}

print(student[("Partha", 101)])
```

### Output

```text
A
```

---

# Summary

- Tuples are ordered and immutable collections.
- Created using parentheses `()`.
- A single-element tuple requires a trailing comma.
- Elements are accessed using indexing.
- Tuple unpacking assigns elements to multiple variables.
- Common methods are:
  - `count()`
  - `index()`
- Tuples are faster than lists and useful for storing fixed data.