# For Loop in Python

---

##  What is a For Loop? 

A `for` loop is used to **repeat code for each item in a sequence** (like list, string, numbers).

---

##  Syntax 

```python
for variable in sequence:
    # Code to execute for each item
``` 
### Example 1
```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```

### Example 2 (Numbers using range)
```python
for i in range(5):
    print(i)
```

# Using range() in Python

### What is range()?

The `range()` function generates a **sequence of numbers**.

---

### Example

```python 
for i in range(5):
    print(i)
```


# Important Notes on range() in Python

## Key Points

- `range(5)` starts from **0** by default  
- It stops **before 5** (end value is not included)  
- So it generates numbers from **0 to 4**  

---

# Different Forms of range()

## 1. range(stop)

```python 
range(5)  # 0 to 4
```

## 2. range(start, stop)
```python 
range(2, 6)  # 2 to 5
```
## 3. range(start, stop, step)

```python 
range(1, 10, 2)  # 1, 3, 5, 7, 9
```