# While Loops in Python

---

## What is a While Loop?

A `while` loop in Python is used to **repeat a block of code as long as a condition is True**.

---

## Syntax

```python
while condition:
    # code to run
``` 
* `condition` → checked before every loop
* If condition is True → loop runs
* If condition is False → loop stops

## Example
```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
```
## Output
```python
1
2
3
4
5
```

### How it Works (Step-by-Step)
* `i = 1`
* Check → `i <= 5` → True → print `1`
* Increase `i` → now `i = 2`
* Again check → still True
* Loop continues…
* When `i = 6`, condition becomes False → loop stops