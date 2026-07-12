# Sets and Set Methods in Python

## Introduction

A **set** is an unordered collection of unique elements in Python.

Unlike lists and tuples, sets:

- Do not allow duplicate values.
- Do not maintain the order of elements.
- Are mutable, meaning elements can be added or removed.

Sets are created using curly braces `{}` or the `set()` function.

---

## Characteristics of Sets

- Unordered
- Mutable
- Do not allow duplicate values
- Can store different data types
- Support mathematical set operations

---

# Creating a Set

## Example

```python
fruits = {"apple", "banana", "cherry"}

print(fruits)
```

### Possible Output

```text
{'apple', 'banana', 'cherry'}
```

> **Note:** Since sets are unordered, the output order may vary.

---

# Common Set Methods

## 1. `add()`

### Introduction

The `add()` method adds a new element to the set.

### Syntax

```python
set.add(element)
```

### Example

```python
my_set = {1, 2, 3, 4}

my_set.add(5)

print(my_set)
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

## 2. `remove()`

### Introduction

The `remove()` method removes the specified element.

If the element does not exist, it raises a `KeyError`.

### Syntax

```python
set.remove(element)
```

### Example

```python
my_set = {1, 2, 3, 4}

my_set.remove(2)

print(my_set)
```

### Output

```text
{1, 3, 4}
```

---

## 3. `discard()`

### Introduction

The `discard()` method removes the specified element if it exists.

If the element does not exist, no error occurs.

### Syntax

```python
set.discard(element)
```

### Example

```python
my_set = {1, 2, 3, 4}

my_set.discard(10)

print(my_set)
```

### Output

```text
{1, 2, 3, 4}
```

---

## 4. `pop()`

### Introduction

The `pop()` method removes and returns an arbitrary element from the set.

Since sets are unordered, you cannot predict which element will be removed.

### Syntax

```python
set.pop()
```

### Example

```python
my_set = {1, 2, 3, 4}

removed = my_set.pop()

print("Removed:", removed)
print(my_set)
```

### Possible Output

```text
Removed: 1
{2, 3, 4}
```

> **Note:** The removed element may differ each time.

---

# Set Operations

## 1. `union()`

Returns a new set containing all unique elements from both sets.

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

### Output

```text
{1, 2, 3, 4, 5}
```

---

## 2. `intersection()`

Returns a new set containing only the common elements.

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))
```

### Output

```text
{3}
```

---

## 3. `difference()`

Returns elements that are present in the first set but not in the second.

### Example

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b))
```

### Output

```text
{1, 2}
```

---


## Python Set Operations Table

| Operation | Symbol | Method | Example | Output |
|-----------|--------|--------|---------|--------|
| **Union** | `\|` | `union()` | `A = {1,2,3}`<br>`B = {3,4,5}`<br>`A \| B` | `{1,2,3,4,5}` |
| **Intersection** | `&` | `intersection()` | `A & B` | `{3}` |
| **Difference** | `-` | `difference()` | `A - B` | `{1,2}` |
| **Difference (Reverse)** | `-` | `difference()` | `B - A` | `{4,5}` |
| **Symmetric Difference** | `^` | `symmetric_difference()` | `A ^ B` | `{1,2,4,5}` |
| **Subset** | `<=` | `issubset()` | `{1,2} <= {1,2,3}` | `True` |
| **Proper Subset** | `<` | — | `{1,2} < {1,2,3}` | `True` |
| **Superset** | `>=` | `issuperset()` | `{1,2,3} >= {1,2}` | `True` |
| **Proper Superset** | `>` | — | `{1,2,3} > {1,2}` | `True` |
| **Disjoint** | — | `isdisjoint()` | `{1,2}.isdisjoint({3,4})` | `True` |
| **Equality** | `==` | — | `{1,2,3} == {3,2,1}` | `True` |
| **Inequality** | `!=` | — | `{1,2} != {1,2,3}` | `True` |



# Use Case of Sets

Sets are commonly used to:

- Remove duplicate values from a collection.
- Perform mathematical set operations.
- Check membership efficiently.

### Example: Remove Duplicates

```python
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

### Possible Output

```text
{1, 2, 3, 4, 5}
```

---

# Summary

- Sets are unordered collections of unique elements.
- Duplicate values are automatically removed.
- Common methods include:
  - `add()`
  - `remove()`
  - `discard()`
  - `pop()`
- Common set operations include:
  - `union()`
  - `intersection()`
  - `difference()`
- Sets are useful for removing duplicates and performing mathematical operations on collections.

# Important Notes

## Creating an Empty Set in Python

An **empty set** is **not** created using `{}`.

### Example

```python
a = {}
b = set()

print(type(a))
print(type(b))
```

### Output

```text
<class 'dict'>
<class 'set'>
```

## Key Points

- `{}` creates an **empty dictionary (`dict`)**, **not** a set.
- `set()` creates an **empty set (`set`)**.
- To create an empty set, **always use `set()`**.
- This is one of the **most common mistakes** beginners make when learning Python.