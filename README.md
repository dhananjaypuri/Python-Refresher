# 🐍 Python Refresher - Complete Learning Guide

> A comprehensive Python learning journey covering fundamentals to Object-Oriented Programming. Perfect for refreshing core concepts before diving into MLOps!

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Fundamentals](#fundamentals)
3. [Data Structures](#data-structures)
4. [Control Flow](#control-flow)
5. [Functions & Modules](#functions--modules)
6. [File Operations](#file-operations)
7. [Advanced Concepts](#advanced-concepts)
8. [Object-Oriented Programming](#object-oriented-programming)
9. [Quick Reference](#quick-reference)
10. [How to Use This Repository](#how-to-use-this-repository)

---

## 🎯 Overview

This repository contains a structured Python learning path with **15 core modules** covering essential concepts. Each module includes practical examples and code implementations.

**Total Topics Covered:** 25+ | **Code Files:** 20+ | **Lines of Code:** 500+

---

## 📖 Fundamentals

### 1️⃣ Strings - [01_string.py](01_string.py)

Master string manipulation and operations in Python.

**Key Concepts:**
- String declaration (single, double, and triple quotes)
- String length and indexing
- String slicing
- String methods: `lower()`, `upper()`, `count()`, `find()`, `replace()`
- String concatenation
- String formatting: `.format()` and f-strings
- Built-in `dir()` function

**Quick Example:**
```python
name = "Rishi Madan"
print(name.lower())           # rishi madan
print(name.count('i'))        # 2
full_name = f"Hello {name}!"  # Hello Rishi Madan!
```

---

### 2️⃣ Numeric Data Types - [02_numeric.py](02_numeric.py)

Understand numbers and mathematical operations.

**Key Concepts:**
- Integer and Float types
- Arithmetic operations: `+`, `-`, `/`, `//`, `**`, `%`
- Compound assignment operators: `+=`, `-=`, etc.
- Type conversion: `int()`, `float()`
- Comparison operators
- Built-in `abs()` function

**Quick Example:**
```python
num = 5
print(3 + 2)      # 5
print(3 // 2)     # 1 (floor division)
print(3 ** 2)     # 9 (exponentiation)
print(3 % 2)      # 1 (modulo)
```

---

## 📊 Data Structures

### 3️⃣ Lists - [03_list.py](03_list.py)

A versatile ordered collection for storing multiple items.

**Key Concepts:**
- Creating and accessing lists
- List slicing
- List methods: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `reverse()`, `sort()`
- Sorting in ascending/descending order
- `sorted()` function

**Quick Example:**
```python
courses = ["AI", "ML", "MLOPS", "DATA SCIENCE"]
courses.append("Gen AI")           # Add single item
courses.extend(["Python", "FastAPI"])  # Add multiple items
courses.remove("Python")           # Remove specific item
courses.sort()                     # Sort alphabetically
```

---

### 4️⃣ Tuples - [04_tuples.py](04_tuples.py)

Immutable sequences for protecting data.

**Key Concepts:**
- Creating tuples
- Tuple unpacking
- Indexing and slicing
- `enumerate()` function
- Tuple methods: `count()`, `index()`
- Immutability concept

**Quick Example:**
```python
tuple_1 = (1, 2, 3)
for ind, item in enumerate(tuple_1, start=1):
    print(ind, item)  # 1 1, 2 2, 3 3
print(tuple_1.count(1))    # 1
print(tuple_1.index(2))    # 1
```

---

### 5️⃣ Sets - [05_sets.py](05_sets.py)

Unique items and set operations.

**Key Concepts:**
- Set creation
- Set operations: `union()`, `difference()`, `intersection()`
- Uniqueness property
- No indexing (unordered collection)

**Quick Example:**
```python
course1 = {"AI", "ML", "DL"}
course2 = {"AI", "DATA SCIENCE", "DL", "GEN AI"}
print(course1.union(course2))        # All items
print(course1.difference(course2))   # Only in course1
print(course1.intersection(course2)) # Common items
```

---

### 6️⃣ Dictionaries - [06_dictionary.py](06_dictionary.py)

Key-value pairs for structured data.

**Key Concepts:**
- Creating dictionaries
- Accessing values by key
- Iterating through dictionaries
- Dictionary methods: `keys()`, `values()`, `items()`, `update()`, `pop()`
- Dictionary unpacking in loops
- Deleting with `del`

**Quick Example:**
```python
student = {"name": "Amar", "age": 25, "course": ["AI", "ML"]}
print(student["name"])      # Amar
student.update({"phone": 999...})  # Add/update
for k, v in student.items():
    print(k, "=", v)
del student['age']          # Delete key
```

---

## 🔀 Control Flow

### 7️⃣ Conditionals - [07_conditionals.py](07_conditionals.py)

Make decisions in your code.

**Key Concepts:**
- `if`, `elif`, `else` statements
- Conditional logic
- Return statements
- Truthy and falsy values
- Boolean evaluation

**Quick Example:**
```python
language = "Java"
if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("No Match")
```

---

### 8️⃣ Loops - [08_loops.py](08_loops.py)

Iterate through data efficiently.

**Key Concepts:**
- `for` loops
- `while` loops
- Loop control: `break`, `continue`
- `range()` function
- Loop with conditions

**Quick Example:**
```python
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 2:
        break       # Exit loop
    print(num)

for i in range(1, 11):
    print(i)        # 1 to 10

x = 0
while x < 10:
    print(x)
    x += 1
```

---

## 🛠️ Functions & Modules

### 9️⃣ Functions - [09_functions.py](09_functions.py)

Reusable blocks of code.

**Key Concepts:**
- Function definition and calling
- Parameters and return values
- `*args` (variable positional arguments)
- `**kwargs` (variable keyword arguments)
- Function docstrings

**Quick Example:**
```python
def hello(name):
    return f"Hello {name}"

result = hello("Ajay")
print(result)  # Hello Ajay

def show_data(*args, **kwargs):
    print(args)     # (1, 3)
    print(kwargs)   # {'name': 'Ajay'}

show_data(1, 3, name="Ajay")
```

---

### 🔟 Module Imports - [10 Import/](10%20Import)

Use code from other files and libraries.

**Key Concepts:**
- Creating custom modules
- `import` statements
- `from ... import` statements
- Aliasing with `as`
- Module organization

**Files:**
- [my_module.py](10%20Import/my_module.py) - Custom module with functions
- [app.py](10%20Import/app.py) - Using the custom module

**Quick Example:**
```python
# my_module.py
def greet(name):
    return f"Hi, {name}"

# app.py
from my_module import greet
result = greet("Ajay")  # Hi, Ajay
```

---

## 📁 File Operations

### 1️⃣1️⃣ OS Module - [11_os_module.py](11_os_module.py)

Interact with the operating system.

**Key Concepts:**
- `os.getcwd()` - Get current directory
- `os.listdir()` - List directory contents
- `os.mkdir()`, `os.makedirs()` - Create directories
- `os.remove()`, `os.rmdir()` - Delete files/directories
- `os.walk()` - Traverse directories recursively
- `os.path` module for path operations
- Environment variables

**Quick Example:**
```python
import os
print(os.getcwd())              # Current working directory
print(os.listdir())             # Files in current directory
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(filenames)            # Files in each directory
```

---

### 1️⃣2️⃣ File Handling - [12_Files/](12_Files)

Read and write files efficiently.

**Key Concepts:**
- Reading files: `r` mode
- Writing files: `w` mode
- Binary mode: `rb`, `wb`
- File context manager (`with` statement)
- Chunked reading/writing
- File copying

**Files:**
- [read_file.py](12_Files/read_file.py) - Reading files in chunks
- [write_file.py](12_Files/write_file.py) - Copying text files
- [binary_write.py](12_Files/binary_write.py) - Binary file operations

**Quick Example:**
```python
# Reading
with open("test.txt", "r") as f:
    data = f.read(10)           # Read 10 bytes

# Writing with context manager
with open("output.txt", "w") as f:
    f.write("Hello World")

# Binary file operations
with open("image.jpg", "rb") as rb:
    with open("copy.jpg", "wb") as wb:
        data = rb.read(4096)
        wb.write(data)
```

---

## 🚀 Advanced Concepts

### 1️⃣3️⃣ Comprehensions - [13 Comprehensions/](13%20Comprehensions)

Write concise and elegant code.

**Key Concepts:**
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Conditional comprehensions
- Nested comprehensions
- `zip()` function for pairing

**Files:**
- [01_list.py](13%20Comprehensions/01_list.py) - List comprehensions
- [02_dict.py](13%20Comprehensions/02_dict.py) - Dictionary comprehensions
- [03_sets.py](13%20Comprehensions/03_sets.py) - Set comprehensions

**Quick Examples:**
```python
# List Comprehension
nums = [1, 2, 8, 4]
new_nums = [num**2 for num in nums]  # [1, 4, 64, 16]

even_numbers = [f"{num} is Even" if num % 2 == 0 else "Odd" for num in nums]

# Dictionary Comprehension
names = ["Ajay", "Amar", "Anthony"]
numbers = [i+1 for i in range(3)]
new_dict = {num: name for num, name in zip(numbers, names)}
# {1: 'Ajay', 2: 'Amar', 3: 'Anthony'}

# Set Comprehension
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_nums = {num for num in numbers}  # {1, 2, 3, 4, 5}
```

---

### 1️⃣4️⃣ Exception Handling - [14_exception.py](14_exception.py)

Handle errors gracefully.

**Key Concepts:**
- `try` block - Code that might fail
- `except` block - Handle specific exceptions
- `else` block - Runs if no exception
- `finally` block - Always executes
- Custom exceptions
- Exception types

**Quick Example:**
```python
try:
    with open("README.md") as f:
        data = f.read()
        print(data)
except Exception as e:
    print(f"Error: {e}")
else:
    print("File read successfully")
finally:
    print("This always executes")
```

---

## 🏗️ Object-Oriented Programming

### 1️⃣5️⃣ Classes & OOP - [15 classes/](15%20classes)

Master object-oriented programming.

#### **File 1: Basic Classes** - [01_class.py](15%20classes/01_class.py)

**Concepts:**
- Class definition
- Constructor (`__init__`)
- Instance variables
- Instance methods
- Creating objects

**Example:**
```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return f"{self.first} {self.last}"

emp_1 = Employee('Ajay', 'Sharma', 5000000)
print(emp_1.fullname())  # Ajay Sharma
```

---

#### **File 2: Class Variables** - [02_class_variables.py](15%20classes/02_class_variables.py)

**Concepts:**
- Class variables (shared across instances)
- Instance variables (unique to each instance)
- Modifying class variables
- Class vs instance namespace

**Example:**
```python
class Student:
    roll_number = 0
    
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        Student.roll_number += 1
        self.roll_number = Student.roll_number

st_1 = Student("Ajay", ["English", "Maths"])
st_2 = Student("Rajan", ["English", "Maths"])
print(st_1.roll_number)     # 1
print(st_2.roll_number)     # 2
print(Student.roll_number)  # 2
```

---

#### **File 3: Class Methods** - [03_class_methods.py](15%20classes/03_class_methods.py)

**Concepts:**
- `@classmethod` decorator
- Class method syntax
- `cls` parameter
- Modifying class state

**Example:**
```python
class Employee:
    company = "Apple"
    
    @classmethod
    def changeCompany(cls, new):
        cls.company = new

emp_1 = Employee()
emp_1.changeCompany("Tesla")
print(Employee.company)  # Tesla
```

---

#### **File 4: Inheritance** - [04_class_inhertitance.py](15%20classes/04_class_inhertitance.py)

**Concepts:**
- Parent and child classes
- `super()` function
- Method overriding
- Multiple inheritance
- Real-world hierarchy

**Example:**
```python
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

class Developer(Employee):
    def __init__(self, fname, lname, pay, lang):
        super().__init__(fname, lname, pay)
        self.lang = lang

dev_1 = Developer("Ajay", "Sharma", 12000, "Python")
```

---

#### **File 5: Property Decorator** - [05_property_decorater.py](15%20classes/05_property_decorater.py)

**Concepts:**
- `@property` decorator for getters
- `@property.setter` decorator
- Computed properties
- Validation in setters
- `__repr__()` and `__str__()` methods

**Example:**
```python
class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @property
    def fullname(self):
        return f"{self.fname} {self.lname}"
    
    @fullname.setter
    def fullname(self, name):
        self.fname, self.lname = name.split()

emp = Student("Ajay", "Sharma")
print(emp.fullname)        # Ajay Sharma
emp.fullname = "Ram Singh"
print(emp.fname)           # Ram
```

---

#### **File 6: Dunder Methods** - [06_dunder.py](15%20classes/06_dunder.py)

**Concepts:**
- Magic/Dunder methods: `__str__()`, `__repr__()`
- Operator overloading: `__add__()`, `__sub__()`, etc.
- Object representation
- String conversion

**Example:**
```python
class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    def __repr__(self):
        return f'Employee("{self.fname}", "{self.lname}", {self.pay})'
    
    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee("Ajay", "Yadav", 30000)
emp_2 = Employee("Raghav", "Kumar", 90000)
print(emp_1)              # Ajay Yadav
print(emp_1 + emp_2)      # 120000
```

---

## 📚 Quick Reference

### String Methods
| Method | Purpose |
|--------|---------|
| `len(s)` | Length of string |
| `s.lower()` | Convert to lowercase |
| `s.upper()` | Convert to uppercase |
| `s.count(x)` | Count occurrences |
| `s.find(x)` | Find index of substring |
| `s.replace(x, y)` | Replace substring |
| `s.split()` | Split string into list |
| `s.join(list)` | Join list into string |

### List Methods
| Method | Purpose |
|--------|---------|
| `append(x)` | Add item to end |
| `insert(i, x)` | Insert at index |
| `extend(list)` | Add multiple items |
| `remove(x)` | Remove first occurrence |
| `pop(i)` | Remove and return item |
| `sort()` | Sort in place |
| `reverse()` | Reverse in place |
| `clear()` | Remove all items |

### Dictionary Methods
| Method | Purpose |
|--------|---------|
| `keys()` | Get all keys |
| `values()` | Get all values |
| `items()` | Get key-value pairs |
| `get(key)` | Get value safely |
| `update(dict)` | Merge dictionaries |
| `pop(key)` | Remove and return value |
| `clear()` | Remove all items |

### Built-in Functions
| Function | Purpose |
|----------|---------|
| `len(x)` | Length of sequence |
| `range(n)` | Generate numbers |
| `enumerate(x)` | Index + value |
| `zip(x, y)` | Pair elements |
| `sorted(x)` | Return sorted list |
| `sum(x)` | Sum of elements |
| `min(x)` / `max(x)` | Minimum/Maximum |
| `int()`, `float()`, `str()` | Type conversion |

---

## 🚀 How to Use This Repository

### 1. **Run Individual Files**
```bash
cd /Users/dhananjaypuri/study/tf-code/Python\ Refresher/
python3 01_string.py
python3 02_numeric.py
# ... and so on
```

### 2. **Explore a Specific Topic**
- Pick a concept from the table of contents
- Open the corresponding Python file
- Run it and observe the output
- Modify the code and experiment

### 3. **Learning Path**
**Beginner:**
- 01_string.py → 02_numeric.py → 03_list.py → 04_tuples.py → 05_sets.py → 06_dictionary.py

**Intermediate:**
- 07_conditionals.py → 08_loops.py → 09_functions.py → 13_Comprehensions/

**Advanced:**
- 10_Import/ → 11_os_module.py → 12_Files/ → 14_exception.py → 15_classes/

### 4. **MLOps Preparation**
These Python fundamentals are crucial for MLOps:
- **Data Handling:** Lists, tuples, dictionaries, comprehensions
- **File Operations:** Working with logs, configs, and data files
- **Functions & Modules:** Writing reusable code and libraries
- **OOP:** Building maintainable ML pipelines and utilities
- **Exception Handling:** Robust error management in production
- **OS Module:** Managing systems and environments

---

## 📊 Summary Statistics

| Category | Topics | Files |
|----------|--------|-------|
| Fundamentals | Strings, Numbers | 2 |
| Data Structures | Lists, Tuples, Sets, Dicts | 4 |
| Control Flow | Conditionals, Loops | 2 |
| Functions & Modules | Functions, Imports, OS | 3 |
| File Operations | File I/O, Binary | 3 |
| Advanced | Comprehensions, Exceptions | 2 |
| OOP | Classes, Inheritance, Properties | 4 |
| **TOTAL** | **25+ Concepts** | **20+ Files** |

---

## 💡 Key Takeaways for MLOps

1. **Data Processing:** Master lists, dicts, and comprehensions for data manipulation
2. **File Handling:** Understand reading/writing config files, logs, and datasets
3. **Functions:** Write modular, reusable code for ML pipelines
4. **OOP:** Structure complex ML systems with classes and inheritance
5. **Error Handling:** Build robust systems with proper exception management
6. **Modules:** Organize code into packages for scalability
7. **OS Operations:** Navigate filesystems and manage environments

---

## 🎓 Next Steps

After completing this refresher:
1. ✅ Review all 20+ Python files in this repo
2. ✅ Run each file and understand the output
3. ✅ Modify examples and experiment
4. ✅ Create your own practice scripts
5. ✅ Proceed to MLOps tools and frameworks

---

## 📝 Notes

- All code uses **Python 3.x**
- Files include comments explaining concepts
- Run files individually or explore in the IDE
- Modify and experiment with the code
- This is a self-contained learning package

---

## 🔗 Related Topics

For MLOps, you'll also need:
- **Virtual Environments:** `venv`, `conda`
- **Package Management:** `pip`, `requirements.txt`
- **Version Control:** `git`, `GitHub`
- **Testing:** `pytest`, `unittest`
- **Logging:** Python's `logging` module
- **APIs:** `requests`, `FastAPI`
- **Data Science:** `NumPy`, `Pandas`, `Scikit-learn`

---

**Happy Learning! 🚀** 

*Created as a comprehensive Python foundation before diving into MLOps.*
