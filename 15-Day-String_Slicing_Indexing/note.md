# String Indexing and Slicing in Python

## Introduction
In Python, a string is a sequence of characters. Each character in a string has a position called an index. Using indexing, you can access a single character, and using slicing, you can extract a part of the string (substring).

## String Indexing
Each character in a string has a unique position called an **index**. Positive indexing starts from 0 for the first character, while negative indexing starts from -1 for the last character.

```python
text = "Python"

print(text[0])   # Output: P
print(text[1])   # Output: y
print(text[-1])  # Output: n (last character)
print(text[-2])  # Output: o
```
## index position:
```python
P  y  t  h  o  n
0  1  2  3  4  5

P   y   t   h   o   n
-6 -5  -4  -3  -2  -1
```
## String Slicing
Slicing is used to extract a part of a string. The syntax for slicing is:

```Python

string[start:stop:step]
```

* start → starting index
* stop → ending index (not included)
* step → interval or jump between characters

### Example:
```Python
text = "Hello, Python!"

print(text[0:5])    # Output: Hello
print(text[:5])     # Output: Hello
print(text[7:])     # Output: Python!
print(text[::2])    # Output: Hlo yhn
print(text[-6:-1])  # Output: ython
```

### Explanation:
* `text[0:5]` → characters from index 0 to 4
* `text[:5]` → starts from beginning up to index 4
* `text[7:]` → starts from index 7 till the end
* `text[::2]` → selects every second character
* `text[-6:-1]` → uses negative indexing to extract part of the string

## Practical Uses of Slicing
String slicing is useful in many scenarios:

* Extracting substrings
* Reversing strings
* Removing characters
* Manipulating text efficiently

```python 
text = "Welcome to Python!"
print(text[:7])   # Output: Welcome
print(text[-7:])  # Output: Python!
print(text[3:-3]) # Output: come to Pyt
```
### Summary
* Indexing allows accessing individual characters.
* Positive indexing starts from 0, negative indexing starts from -1.
* Slicing helps extract portions of a string.
* The step parameter defines the interval for selection.
* Using [::-1] reverses a string.