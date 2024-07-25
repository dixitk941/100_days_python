# As we played around with Flask to beef up our site security and got a taste of how Python works, I got pumped to dive deeper. So, let’s start this journey from Python newbie to Python guru—bring on the coffee, late-night coding, and "kyun nahi chal raha yeh?!" moments! 🐍🚀

## Python Basics

1. High Level Interpreted Language
2. Known for its readability, simplicity, versatility

## Key Features

- Easy to read and write
- Interpreted language
- Dynamically typed
- Object-oriented
- High-level language
- Extensive standard library
- Cross-platform
- Large ecosystem

## Basic Syntax

### Variables
1. `x = 5`  # Integer
2. `y = 3.5`  # Float
3. `z = "karan"`  # String

### Control Flow

```python
if x > 0:
    print("x is positive")
else:
    print("x is negative")

for i in range(5):
    print(i)
```

### Functions

```python
def greet(name):
    return f"hello, {name}!"

print(greet("Karan"))
```

### Classes and Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

person = Person("Karan", 19)
print(person.greet())
```

## Modules and Packages

### mymodule.py

```python
def add(x, y):
    return x + y
```

### main.py

```python
import mymodule

print(mymodule.add(3, 5))
```

## File I/O

**Note:** Python provides built-in functions to read and write to files.

```python
with open("example.txt", "w") as file:
    file.write("hello, world!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

--------------------end-------------------

Day 4
Sign-off
Karan Dixit (dixitk941)

## Day 5 Task:
- Loops, and Practice
