# List Methods in Python

Python provides several built-in methods to add, remove, modify, and organize list elements.

---

## 1. `append()`

### Introduction

The `append()` method adds an element to the **end** of the list.

### Syntax

```python
list.append(item)
```

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

## 2. `insert()`

### Introduction

The `insert()` method inserts an element at a specified index.

### Syntax

```python
list.insert(index, item)
```

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

## 3. `remove()`

### Introduction

The `remove()` method removes the **first occurrence** of the specified value.

### Syntax

```python
list.remove(value)
```

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

## 4. `pop()`

### Introduction

The `pop()` method removes and returns an element.

If no index is specified, it removes the last element.

### Syntax

```python
list.pop()
```

or

```python
list.pop(index)
```

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

### Example with Index

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

## 5. `reverse()`

### Introduction

The `reverse()` method reverses the order of elements in the list.

### Syntax

```python
list.reverse()
```

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

## 6. `sort()`

### Introduction

The `sort()` method sorts the list in ascending order by default.

### Syntax

```python
list.sort()
```

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

### Descending Order

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

## Introduction

A **list comprehension** is a concise and efficient way to create a new list.

It combines a loop and an expression into a single line of code.

---

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

## Example with Condition

Create a list of even numbers.

```python
even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)
```

### Output

```text
[0, 2, 4, 6, 8]
```

---

# Summary

| Method | Description |
|---------|-------------|
| `append()` | Adds an element to the end of the list. |
| `insert()` | Inserts an element at a specified index. |
| `remove()` | Removes the first occurrence of a specified value. |
| `pop()` | Removes and returns an element (last by default). |
| `reverse()` | Reverses the order of the list. |
| `sort()` | Sorts the list in ascending order by default. |

---

## List Comprehension Summary

- Creates lists in a concise way.
- Can include expressions and conditions.
- Often shorter and faster than traditional loops.

