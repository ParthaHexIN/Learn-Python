# Variables and Data Types in Python

## What are Variables?
A **variable** is a name used to store data in a program.  
It allows us to save information that can be used later in the code.

In Python, you do **not need to declare the type** of a variable. The type is automatically assigned based on the value.

### Example
```python
name = "Partha"
age = 20
price = 99.5
```
In the example:

- **name** stores a string

- **age** stores an integer

- **price** stores a float

## Variable Naming Rules

When creating variables in Python, follow these rules:

1. A variable name must start with a letter [A-Z] [a-z] or underscore (_).

2. A variable name cannot start with a number.

3. A variable name can contain letters, numbers, and underscores.

4. Variable names are case-sensitive (age and Age are different).

5. Keywords cannot be used as variable names (like if, for, while, False
True, None, else, while, class, def, return, importetc.).

## Valid Examples
```python 
name = "Partha"
_age = 20
student1 = "Rahul"
```
## Invalid Examples
```python
1name = "Partha"
class = "Python"
```

## Best Practices for Naming Variables

1. Use meaningful names.

2. Use lowercase words separated by underscores.

3. Avoid very short or confusing names.

4. Keep names simple and readable.

## Good Example
```python 
student_name = "Partha"
total_marks = 450
```
```python
Bad Example
x = "Partha"
a = 450
```
## Data Types in Python

A data type defines the type of value stored in a variable.

Python has several built-in data types.

### 1. Integers

Integers are whole numbers without decimal points.

#### Example
```python 
age = 20
year = 2026
```

### 2. Floats

Floats are numbers with decimal points.

#### Example

```python 
price = 99.99
temperature = 36.5
```
### 3. Strings

Strings are text values enclosed in quotes.

#### Example
```python 
name = "Partha"
message = "Hello World"
```

### 4. Booleans

Booleans represent True or False values.

#### Example
```python 
is_student = True
is_logged_in = False
```

### 5. Lists

A list is a collection of items stored in order.
Lists are written using square brackets [ ].

#### Example
```python 
fruits = ["apple", "banana", "mango"]
numbers = [1, 2, 3, 4]
```
Lists can be changed (mutable).

### 6. Tuples

A tuple is similar to a list but cannot be changed after creation.

Tuples use parentheses ( ).

#### Example
```python 
coordinates = (10, 20)
colors = ("red", "green", "blue")
```

### 7. Sets

A set is an unordered collection of unique items.

Sets use curly braces { }.

#### Example
```python 
numbers = {1, 2, 3, 4}
letters = {"a", "b", "c"}
```

Sets do not allow duplicate values.

### 8. Dictionaries

A dictionary stores data in key-value pairs.

#### Example
```python 
student = {
    "name": "Partha",
    "age": 20,
    "course": "Python"
}
```

Here:

name, age, course are keys

"Partha", 20, "Python" are values

## Checking Data Types

Python provides the type() function to check the data type of a variable.

#### Example

```python  
age = 20
print(type(age))
```
#### Output:
```python 
<class 'int'>
``` 
#### More Examples
```python 
name = "Partha"
print(type(name))

price = 99.5
print(type(price))
```
