# Library Management System Practice with Custom Modules

A library wants to have a system to manage its books. This system includes features such as adding books, removing books, searching for books, and showing all books. You should implement this system modularly and check the ability to install modules via pip and PyPi.

## Using Modules and Packages

### Your task:

- Create a module called library.py that includes the Library class. This class should have the following features:

- A list of books that stores the books.
- The add_book(title, author) method to add a book.
- The remove_book(title) method to remove a book.
- The search_book(title) method to search for a book.
- The show_books() method to show all books.

## Create a new file called main.py that uses library.py and implements the library management system.

```python
__name__ == "__main__"
```

### Your task:

Check in main.py whether this file has been executed directly or not.
If it has been executed directly, display a simple menu for adding, removing, and searching for books.

## Convert the module to an installation package (pip install)

### Your task:
- Prepare your package for local installation:

- Create a folder called mylibrary and put the file library.py in it.
- Create an __init__.py file inside mylibrary/.
- Create a setup.py file to install the package.
## Install the package:

- Run the command pip install . to install the package locally.
- Then import it into main.py and test it.