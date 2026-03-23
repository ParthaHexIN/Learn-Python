# Match-Case in Python

Match-case in Python is a **pattern matching statement** introduced in **Python 3.10**.  
It works like an advanced version of `if-elif-else`, but is more powerful and cleaner for matching patterns.

---

## 🔹 Basic Idea 

- `match` → checks a value  
- `case` → defines patterns to compare against  
- The **first matching case runs**  

---

## 🔹 Basic Syntax 

```python
match variable:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default case
```
## 🔹 Example
```python

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")
```
