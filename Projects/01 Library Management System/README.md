# Library Management System

A simple yet effective Python-based Library Management System that allows seamless management of books, including adding, searching, issuing, and returning books with real-time status tracking.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Class Documentation](#class-documentation)
- [Example Operations](#example-operations)
- [Future Enhancements](#future-enhancements)

---

## 🎯 Overview

The Library Management System is built using **Object-Oriented Programming (OOP)** principles in Python. It provides a command-line interface (CLI) for librarians to efficiently manage their book inventory and track book availability status.

### Key Highlights:
- ✅ Lightweight and easy to use
- ✅ Real-time book status tracking (Available/Issued)
- ✅ Error handling with try-except blocks
- ✅ Persistent book inventory management
- ✅ User-friendly menu-driven interface

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **Display Books** | View all books in the library with their IDs and names |
| **Add Book** | Add new books to the library with ID, name, and author |
| **Search Book** | Search for a specific book and view its details (ID, Name, Author, Status) |
| **Issue Book** | Mark a book as "issued" to track which books are checked out |
| **Return Book** | Mark an issued book as "available" when returned |
| **Remove Book** | Delete a book from the library inventory |
| **Exit** | Gracefully exit the application |

---

## 🏗️ System Architecture

### Application Flowchart

```
┌─────────────────────────────────────────────┐
│   START: Library Management System         │
└────────────┬────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────┐
│   Display Main Menu                         │
│   1. Display Books   4. Issue Book          │
│   2. Add Book        5. Return Book         │
│   3. Search Book     6. Remove Book         │
│                      7. Exit                │
└────────────┬────────────────────────────────┘
             │
             ▼
        ┌────────────────────────────┐
        │  User Input Selection      │
        └────────┬───────────────────┘
                 │
    ┌────────────┼────────────┬────────────┬────────────┬────────────┬────────────┐
    │            │            │            │            │            │            │
    ▼            ▼            ▼            ▼            ▼            ▼            ▼
  (1)          (2)          (3)          (4)          (5)          (6)          (7)
Display       Add          Search       Issue        Return       Remove       Exit
Books        Book          Book         Book         Book         Book
   │            │            │            │            │            │            │
   │            ▼            │            ▼            ▼            ▼            │
   │    ┌──────────────┐     │    ┌──────────────┐    │    ┌──────────────┐     │
   │    │Input:        │     │    │Input:        │    │    │Input:        │     │
   │    │Book ID       │     │    │Book ID       │    │    │Book ID       │     │
   │    │Name          │     │    └──────┬───────┘    │    └──────┬───────┘     │
   │    │Author        │     │           ▼            │           ▼             │
   │    └──────┬───────┘     │    ┌──────────────┐    │    ┌──────────────┐     │
   │           ▼             │    │Check if ID   │    │    │Check if ID   │     │
   │    ┌──────────────┐     │    │exists        │    │    │exists        │     │
   │    │Check if ID   │     │    └──┬───────┬──┘    │    └──┬───────┬──┘     │
   │    │already exists│     │       │       │        │       │       │         │
   │    └──────┬───────┘     │    YES NO    │        │    YES NO    │         │
   │           │             │       │      ▼        │       │      ▼         │
   │        ┌──┴──┐         │       │   ┌────┐   │       │   ┌────┐         │
   │       YES   NO          │       │   │Error│   │       │   │Error│       │
   │        │      │         │       │   └────┘   │       │   └────┘       │
   │        ▼      ▼         │       ▼            │       ▼                 │
   │    ┌───────┐ ┌──────┐   │    ┌──────┐     │    ┌──────┐              │
   │    │Error  │ │Added │   │    │Check │     │    │Check │              │
   │    └───────┘ └──────┘   │    │Status│     │    │Status│              │
   │        │      │         │    └──┬───┘     │    └──┬───┘              │
   │        └──────┴─────────┼────┬──┘         │       │                  │
   │                         │    │            │    ┌──┴──┐               │
   │                         │ Available    Issued  Available Issued      │
   │                         │    │            │       │        │        │
   │                         │    ▼            │       ▼        ▼        │
   │                         │ ┌──────┐   ┌───┴──┐  ┌──────┐ ┌────┐    │
   │                         │ │Issue │   │Error │  │Return│ │Error│   │
   │                         │ │Book  │   │Issued│  │Book  │ │Already  │
   │                         │ │Status│   │Before   │Status│ │Available│
   │                         │ └──────┘   └────────┘ └──────┘ └────┘    │
   │                         │    │            │       │        │        │
   ▼                         ▼    ▼            ▼       ▼        ▼        ▼
┌──────────────┐    ┌─────────────────────────────────────────────────────┐
│Display All   │    │        Output Result Message                        │
│Books Summary │    │    (Success/Error notifications)                    │
└──────┬───────┘    └─────────────────┬───────────────────────────────────┘
       │                              │
       └──────────────┬───────────────┘
                      │
                      ▼
           ┌─────────────────────────┐
           │ Show Separator Line     │
           │ (====...====)           │
           └────────┬────────────────┘
                    │
                    ▼
           ┌──────────────────────────┐
           │  Prompt for Next Action  │
           │  "Select the option:"    │
           └────────┬───────────────┘
                    │
         ┌──────────┴──────────┐
         │                     │
         ▼                     ▼
    Continue Loop          Exit (case '7')
       │                     │
       └─────────┬───────────┘
                 ▼
           ┌──────────────┐
           │ END Program  │
           └──────────────┘
```

### Data Model

```python
Library
├── books: dict[int, dict]
│   ├── book_id: int
│   └── book_details: dict
│       ├── name: str
│       ├── author: str
│       └── status: str ("available" or "issued")
```

---

## 💻 Installation

### Requirements
- Python 3.10 or higher
- No external dependencies required!

### Steps
1. **Clone or download the project**
   ```bash
   cd "Projects/01 Library Management System"
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

---

## 🚀 Usage

### Running the Application

```bash
python main.py
```

You'll see a menu like this:
```
Welcome to Library Management System
Select the option:

1 -> Display Books
2 -> Add Book
3 -> Search Book
4 -> Issue Book
5 -> Return Book
6 -> Remove Books
7 -> Exit

Enter Option :
```

### Menu Options Explained

#### 1️⃣ Display Books
Shows a list of all books currently in the library.
```
Books are available.
101 , Name: Python Basics
102 , Name: Advanced AI
=======================================
```

#### 2️⃣ Add Book
Add a new book to the library.
```
Enter the book ID: 101
Enter the name of the book: Python Basics
Enter the author name: John Doe
Book Python Basics added successfully with id 101
```

#### 3️⃣ Search Book
Search for a specific book by ID.
```
Enter the book ID: 101
Book ID: 101, Name: Python Basics, Author: John Doe, Status: available
```

#### 4️⃣ Issue Book
Mark a book as issued (checked out).
```
Enter the book ID: 101
Book Issued
```

#### 5️⃣ Return Book
Mark an issued book as available again.
```
Enter the book ID: 101
Book Returned
```

#### 6️⃣ Remove Book
Delete a book from the library inventory.
```
Enter the book ID: 101
Book with ID: 101 removed successfully !!!!
```

#### 7️⃣ Exit
Exit the application.

---

## 📁 Project Structure

```
01 Library Management System/
├── main.py              # Main application file
└── README.md           # Documentation (this file)
```

---

## 📚 Class Documentation

### `Library` Class

**Purpose:** Central class that manages all library operations.

#### Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `books` | `dict` | Dictionary storing all books with book_id as key |

#### Methods

##### `__init__()`
Initializes an empty library.
```python
Library()  # Creates a new library instance
```

##### `add_books(book_id, name, author)`
Adds a new book to the library.
- **Parameters:**
  - `book_id` (int): Unique identifier for the book
  - `name` (str): Title of the book
  - `author` (str): Author's name
- **Returns:** Success or error message
- **Raises:** Returns error if book_id already exists

##### `search_book(book_id)`
Searches for a book by ID.
- **Parameters:**
  - `book_id` (int): Book ID to search for
- **Returns:** Book details (ID, Name, Author, Status) or error message

##### `remove_book(book_id)`
Removes a book from the library.
- **Parameters:**
  - `book_id` (int): ID of book to remove
- **Returns:** Success or error message

##### `display_books()`
Displays all books in the library.
- **Parameters:** None
- **Returns:** Formatted string with all books or "No Books Available"

##### `issue_book(book_id)`
Marks a book as issued (checked out).
- **Parameters:**
  - `book_id` (int): ID of book to issue
- **Returns:** Success or error message
- **Note:** Can only issue books with status "available"

##### `return_book(book_id)`
Marks an issued book as available.
- **Parameters:**
  - `book_id` (int): ID of book being returned
- **Returns:** Success or error message
- **Note:** Can only return books with status "issued"

---

## 💡 Example Operations

### Example 1: Complete Library Workflow

```python
# Initialize library
bk = Library()

# Add books
print(bk.add_books(101, "Python", "ABC"))  
# Output: Book Python added successfully with id 101

print(bk.add_books(102, "AI", "ML"))  
# Output: Book AI added successfully with id 102

# Display all books
print(bk.display_books())
# Output:
# Below 2 Books are available .
# 101 , Name: Python
# 102 , Name: AI

# Issue a book
print(bk.issue_book(101))
# Output: Book Issued

# Search for book
print(bk.search_book(101))
# Output: Book ID: 101, Name: Python, Author: ABC, Status: issued

# Try to issue same book again
print(bk.issue_book(101))
# Output: Book is already issued to someone else.

# Return the book
print(bk.return_book(101))
# Output: Book Returned

# Remove a book
print(bk.remove_book(102))
# Output: Book with ID: 102 removed successfully !!!!
```

### Example 2: Error Handling

```python
# Try to add duplicate book ID
print(bk.add_books(101, "Python", "ABC"))  # Success

print(bk.add_books(101, "Java", "XYZ"))    # Error
# Output: Books id 101 already exists!!!!

# Try to search non-existent book
print(bk.search_book(999))
# Output: Book is not available

# Try to issue non-existent book
print(bk.issue_book(999))
# Output: Book is not available in library.
```

---

## 🔒 Error Handling

The application includes robust error handling:

1. **Duplicate Book ID:** Prevents adding books with existing IDs
2. **Book Not Found:** Handles searches and operations on non-existent books
3. **Invalid Status Transitions:** Prevents issuing already-issued books or returning available books
4. **Input Validation:** Uses try-except blocks to catch invalid input (e.g., non-integer book IDs)
5. **Invalid Menu Options:** Provides feedback for invalid menu selections

---

## 🚧 Future Enhancements

Potential improvements for version 2.0:

1. **Data Persistence**
   - Save books to JSON/CSV file
   - Load books on startup

2. **User Management**
   - Track who issued each book
   - Maintain user lending history
   - Due date management

3. **Advanced Features**
   - Fine calculation for overdue books
   - Book reservations
   - Book categories/genres
   - Search by author or title (partial matching)

4. **UI Improvements**
   - Text-based UI library (e.g., curses)
   - GUI implementation (tkinter/PyQt)
   - Web interface (Flask/Django)

5. **Database Integration**
   - SQLite/MySQL integration
   - Advanced querying capabilities

6. **Code Quality**
   - Unit tests
   - Logging system
   - Configuration file support

---

## 📝 Code Style

- **Language:** Python 3.10+
- **Paradigm:** Object-Oriented Programming (OOP)
- **Control Flow:** Match-case statements (Python 3.10+)
- **Error Handling:** Try-except-finally blocks

---

## 🙋 Support

For questions or issues, review the example operations section or examine the method documentation above.

---

## 📄 License

This is an educational project for learning Python fundamentals.

---

## ✨ Summary

The Library Management System demonstrates core Python concepts including:
- ✅ Classes and Object-Oriented Design
- ✅ Dictionary data structures
- ✅ Control flow (if-elif-else, match-case)
- ✅ Exception handling
- ✅ User input/output
- ✅ Function design
- ✅ Code organization

Perfect for beginners learning Python while building a practical application!
