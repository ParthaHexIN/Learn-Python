# Infinite While Loop in Python

---

## What is an Infinite While Loop?

An infinite `while` loop is a loop that **never stops running** because its condition is always **True**.

---

## Basic Example

```python 
while True:
    print("This will run forever")
```
## Another Example
```pyhton 
i = 1
while i <= 5:
    print(i)
```
### Problem
* `i` is never updated
* So `i <= 5` is always True
* Result → infinite loop