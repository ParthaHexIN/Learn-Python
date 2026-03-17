# Taking User Input in Python

## What is User Input?

User input means **taking data from the user during program execution**.
In Python, the `input()` function is used to receive input from the user.

The program pauses and waits until the user enters a value.

---

## Syntax

```python
input("message")
```

* The message inside the parentheses is shown to the user.
* The value entered by the user is returned as a **string**.

---

### Example 1: Basic Input

```python
name = input("Enter your name: ")
print("Hello", name)
```

Example Output:

```
Enter your name: Partha
Hello Partha
```

---

### Example 2: Taking Number Input

Since `input()` always returns a **string**, you must convert it if you want a number.

```python
age = int(input("Enter your age: "))
print("Your age is", age)
```

Here:

* `input()` receives the value
* `int()` converts the string to an integer

---

### Example 3: Adding Two Numbers from User

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum =", sum)
```

Example Output:

```
Enter first number: 5
Enter second number: 10
Sum = 15
```

---

# Important Notes

* `input()` always returns **string data**
* Use typecasting (`int()`, `float()`) to convert numbers
* Programs can become **interactive** using user input


## Facts

* input() pauses program execution until the user enters data.

* The returned value is always a string, unless you convert it.

## Possible misunderstanding

Many beginners assume that if a user types 10, Python treats it as a number automatically. It doesn’t. Without int() or float(), it remains a string, which can cause logical errors.

### Example problem:
```python 
a = input("Enter number: ")
b = input("Enter number: ")

print(a + b)
``` 

If the user enters 5 and 10, the result will be:
``` 
510
``` 
because Python is joining strings, not adding numbers.
