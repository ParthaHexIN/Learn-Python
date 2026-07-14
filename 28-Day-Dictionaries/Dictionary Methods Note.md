
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

# Python Dictionary Methods

| Method | Description |
|--------|-------------|
| `keys()` | Returns all keys in the dictionary. |
| `values()` | Returns all values in the dictionary. |
| `items()` | Returns all key-value pairs as tuples. |
| `get(key)` | Returns the value associated with the specified key. |
| `update()` | Adds new key-value pairs or updates existing ones. |
| `pop(key)` | Removes the specified key and returns its value. |
| `popitem()` | Removes and returns the last inserted key-value pair. |
| `clear()` | Removes all items from the dictionary. |
| `copy()` | Creates a shallow copy of the dictionary. |
| `setdefault()` | Returns the value of a key; if the key does not exist, inserts it with a default value. |
| `fromkeys()` | Creates a new dictionary using the given keys and a common default value. |

---

## Examples

| Method | Example |
|--------|---------|
| `keys()` | `student.keys()` |
| `values()` | `student.values()` |
| `items()` | `student.items()` |
| `get(key)` | `student.get("name")` |
| `update()` | `student.update({"age": 22})` |
| `pop(key)` | `student.pop("age")` |
| `popitem()` | `student.popitem()` |
| `clear()` | `student.clear()` |
| `copy()` | `new_student = student.copy()` |
| `setdefault()` | `student.setdefault("city", "Delhi")` |
| `fromkeys()` | `dict.fromkeys(["a", "b", "c"], 0)` |