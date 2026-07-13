
# Common Dictionary Methods

## 1. `keys()`

Returns all keys in the dictionary.

### Example

```python
print(student.keys())
```

### Output

```text
dict_keys(['name', 'age', 'grade', 'city'])
```

---

## 2. `values()`

Returns all values in the dictionary.

### Example

```python
print(student.values())
```

### Output

```text
dict_values(['Alice', 22, 'A', 'New York'])
```

---

## 3. `items()`

Returns all key-value pairs as tuples.

### Example

```python
print(student.items())
```

### Output

```text
dict_items([('name', 'Alice'), ('age', 22), ('grade', 'A'), ('city', 'New York')])
```

---

## 4. `pop()`

Removes a specified key and returns its value.

### Example

```python
student.pop("age")

print(student)
```

### Output

```text
{'name': 'Alice', 'grade': 'A', 'city': 'New York'}
```

---

## 5. `clear()`

Removes all items from the dictionary.

### Example

```python
student.clear()

print(student)
```

### Output

```text
{}
```

---

