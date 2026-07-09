# Introduction to Lists in Python

## Introduction

A **list** is one of the most commonly used data types in Python.

A list is an **ordered**, **mutable (changeable)** collection of items.

Lists can store:

- Integers
- Floating-point numbers
- Strings
- Boolean values
- Other lists
- Mixed data types

Lists are created using square brackets `[]`, with items separated by commas.

---

## Characteristics of Lists

- Ordered (items maintain their order)
- Mutable (items can be changed after creation)
- Allow duplicate values
- Can store multiple data types

---

## Creating a List

### List of Numbers

```python
numbers = [1, 2, 3, 4, 5]

print(numbers)
```

### Output

```text
[1, 2, 3, 4, 5]
```

---

### Mixed Data Types

```python
mixed = [10, "hello", 3.14]

print(mixed)
```

### Output

```text
[10, 'hello', 3.14]
```

---

# Accessing List Elements

List elements are accessed using indexes.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
```

### Output

```text
10
40
```

---

# Common List Methods

## 1. append()

Adds an item to the end of the list.

### Example

```python
my_list = [1, 2, 3]

my_list.append(4)

print(my_list)
```

### Output

```text
[1, 2, 3, 4]
```

---

## 2. insert()

Inserts an item at a specified position.

### Example

```python
my_list = [1, 2, 3]

my_list.insert(1, 99)

print(my_list)
```

### Output

```text
[1, 99, 2, 3]
```

---

## 3. remove()

Removes the first occurrence of the specified value.

### Example

```python
my_list = [1, 99, 2, 3]

my_list.remove(2)

print(my_list)
```

### Output

```text
[1, 99, 3]
```

---

## 4. pop()

Removes and returns the last element by default.

### Example

```python
my_list = [1, 99, 3]

my_list.pop()

print(my_list)
```

### Output

```text
[1, 99]
```

You can also remove an element at a specific index.

```python
my_list = [10, 20, 30]

my_list.pop(1)

print(my_list)
```

### Output

```text
[10, 30]
```

---

## 5. reverse()

Reverses the order of the list.

### Example

```python
my_list = [1, 99, 3]

my_list.reverse()

print(my_list)
```

### Output

```text
[3, 99, 1]
```

---

## 6. sort()

Sorts the list in ascending order.

### Example

```python
my_list = [3, 1, 99]

my_list.sort()

print(my_list)
```

### Output

```text
[1, 3, 99]
```

To sort in descending order:

```python
my_list.sort(reverse=True)

print(my_list)
```

### Output

```text
[99, 3, 1]
```

---

# List Comprehensions

List comprehensions provide a concise and efficient way to create lists.

## Syntax

```python
[expression for item in iterable]
```

---

## Example

```python
squared = [x**2 for x in range(5)]

print(squared)
```

### Output

```text
[0, 1, 4, 9, 16]
```

### Explanation

- `range(5)` generates numbers from `0` to `4`.
- Each number is squared using `x**2`.
- The results are stored in a new list.

---

## Another Example

Create a list of even numbers.

```python
even = [x for x in range(10) if x % 2 == 0]

print(even)
```

### Output

```text
[0, 2, 4, 6, 8]
```

---

# Summary

- Lists are ordered and mutable collections.
- Lists can store multiple data types.
- Common methods include:
  - `append()`
  - `insert()`
  - `remove()`
  - `pop()`
  - `reverse()`
  - `sort()`
- List comprehensions provide a shorter and more efficient way to create lists.