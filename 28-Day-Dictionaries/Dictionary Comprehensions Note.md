# Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

## Syntax

```python
{key: value for item in iterable}
```

---

## Example

```python
squares = {x: x**2 for x in range(5)}

print(squares)
```

### Output

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Explanation

- `range(5)` generates numbers from `0` to `4`.
- Each number becomes a key.
- Its square becomes the value.

---

# When to Use Each Data Structure

| Data Structure | Features | Best For |
|---------------|----------|----------|
| **List** | Ordered, Mutable | Storing sequences and dynamic data |
| **Tuple** | Ordered, Immutable | Fixed collections and dictionary keys |
| **Set** | Unordered, Unique | Removing duplicates and performing set operations |
| **Dictionary** | Key-Value Pairs | Fast lookups and structured data |

---

# Summary

- Dictionaries store data as **key-value pairs**.
- Keys are unique and used to access values.
- Dictionaries are mutable and ordered (Python 3.7+).
- Common methods include:
  - `keys()`
  - `values()`
  - `items()`
  - `pop()`
  - `clear()`
- Dictionary comprehensions provide an efficient way to create dictionaries.
- Choose the appropriate data structure based on your use case.