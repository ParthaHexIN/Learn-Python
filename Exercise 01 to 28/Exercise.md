# Python Collections – Practice Set

This practice set is based on the following topics:

- Introduction to Lists
- List Methods
- Tuples and Operations on Tuples
- Sets and Set Methods
- Dictionaries and Dictionary Methods

These exercises will help you strengthen your understanding of Python's most important collection data structures.

---

# 1. Introduction to Lists

### 1.1. Create a list:

```python
fruits = ["apple", "banana", "cherry"]
```

Perform the following tasks:

- Print the first fruit.
- Replace `"banana"` with `"orange"`.
- Print the length of the list.

### 1.2. Create a list of numbers from **1 to 10**.

Perform the following tasks:

- Print the first three numbers using slicing.
- Print the last three numbers using slicing.

---

# 2. List Methods

### 2.1. Start with `numbers = [5, 2, 9, 1, 7]` and do the following:

- Sort the list in ascending order.
- Append the number `10` to the list.
- Remove the number `2` from the list.

### 2.2. Create a list:

```python
names = ["Alice", "Bob", "Charlie"]
```

Use the `insert()` method to add `"David"` at index `1`.

---

# 3. Tuples and Operations on Tuples

### 3.1. Create a tuple:

```python
coordinates = (10, 20)
```

- Print both elements.

### 3.2. Try to modify the tuple by executing:

```python
coordinates[0] = 50
```

- Observe and note what happens.

### 3.3. Convert the tuple into a list.

Then:

- Change the first element to `50`.
- Convert the list back into a tuple.

---

# 4. Sets and Set Methods

### 4.1. Create a set:

```python
my_set = {1, 2, 3, 3, 4}
```

- Print the set.
- What happens to the duplicate value `3`?

### 4.2. Using the same set, do the following:

- Add `5`.
- Remove `2`.
- Check whether `4` is present in the set.

### 4.3. Create two sets:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

Find:

- Union
- Intersection
- Difference (`a - b`)

---

# 5. Dictionaries and Dictionary Methods

### 5.1. Create a dictionary:

```python
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
```

Perform the following tasks:

- Print the value of `"name"`.
- Change `"grade"` to `"A+"`.
- Add a new key `"city"` with the value `"Delhi"`.

### 5.2. Create a dictionary containing the names of three friends and their phone numbers.

Use:

- `keys()` to display all names.
- `values()` to display all phone numbers.
- `items()` to loop through the dictionary and print each key-value pair.

---

# 6. Bonus Challenges

### 6.1. Remove Duplicates

Write a program that takes a list of numbers and removes all duplicate values using a **set**.

### 6.2. Highest Price

Given a dictionary containing product names and their prices, find the product with the **highest price**.

### 6.3. Merge Dictionaries

Write a program that merges two dictionaries into a single dictionary.