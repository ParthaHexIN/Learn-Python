# Comments, Escape Sequences & Print Statement in Python

---

# 1. Comments

### What are Comments?

Comments are **notes written inside the code** to explain what the program does.
Python **ignores comments** during execution.

---

## Types of Comments

### Single-line Comment

```python
# This is a comment
print("Hello World")
```

---

### Multi-line Comment (commonly written like this)

```python
"""
This is a
multi-line comment
"""
```

---

## Why Use Comments?

* To explain code logic
* To make code easier to understand
* To improve readability and maintenance

---

# 2. Escape Sequences

## What are Escape Sequences?

Escape sequences are **special characters used inside strings** to perform specific tasks.
They start with a backslash `\`.

---

## Common Escape Sequences

| Escape Sequence | Meaning      | Example    |
| --------------- | ------------ | ---------- |
| `\n`            | New line     | Line break |
| `\t`            | Tab space    | Adds space |
| `\\`            | Backslash    | Prints `\` |
| `\'`            | Single quote | Prints `'` |
| `\"`            | Double quote | Prints `"` |

---

## Example

```python
print("Hello\nWorld")
print("Hello\tWorld")
print("This is a backslash \\")
print("She said \"Hello\"")
```

Output:

```
Hello
World
Hello    World
This is a backslash \
She said "Hello"
```

---

# 3. Print Statement

## What is print()?

The `print()` function is used to **display output on the screen**.

---

## Basic Example

```python
print("Hello World")
```

---

## Printing Multiple Values

```python
name = "Partha"
age = 21

print("Name:", name, "Age:", age)
```

---

## Using sep Parameter

`sep` defines the **separator between values**.

```python
print("Python", "Java", "C++", sep="-")
```

Output:

```
Python-Java-C++
```

---

## Using end Parameter

`end` defines what comes at the **end of the line**.

```python
print("Hello", end=" ")
print("World")
```

Output:

```
Hello World
```

---

## Combining Everything

```python
print("Hello\nWorld", end=" ")
print("Python\tProgramming")
```
