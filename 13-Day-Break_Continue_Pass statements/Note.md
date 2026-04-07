# Break, Continue, and Pass Statements in Python

---

## 1. break Statement

Immediately **stops the loop completely**, even if the condition is still **True**.

---

###  Example

```python 
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```
### Output
``` 
1
2
```
Loop stops when i == 3

## 2. continue Statement

Skips the current iteration and moves to the next loop cycle.

### Example
```python 
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### Output
```
1
2
4
5
```
It skips only 3, not the whole loop

### 3. pass Statement
Does nothing — it's just a placeholder.

Used when Python requires a statement but you don’t want to write logic yet.

### Example
```python
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
``` 
### Output
```
1
2
3
4
5
```