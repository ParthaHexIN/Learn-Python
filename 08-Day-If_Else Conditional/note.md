# If–Else Conditional Statements (Refined Notes)

---

## What are Conditional Statements?

**Fact:**  
Conditional statements control the flow of execution in a program based on a condition that evaluates to **True or False**.

In Python, we use:

- `if`  
- `elif`  
- `else`  

---

## How They Actually Work

A condition is evaluated first:

```python
10 > 5   # True
``` 

Then Python decides which block of code to run.

---

## Syntax Breakdown

```python
if condition:
    # code runs if condition is True

elif condition:
    # runs if previous condition was False and this is True

else:
    # runs if all conditions are False
``` 

## Important Rules
* Indentation is mandatory (Python uses it instead of `{ }`)
* Conditions must return `True` or `False`
* You can use multiple `elif`, but only one `else`

## Real Example 
```python
age = 18

if age > 18:
    print("You are an adult")
elif age == 18:
    print("You just became an adult")
else:
    print("You are a minor")
```

### Step-by-Step Execution
* age > 18 → False
* age == 18 → True ✅
* Output → "You just became an adult"


---


