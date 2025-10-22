# Reading PDF files in Python

## Goal:

This exercise help you to understand how to use `PyPDF2` or PDF file format in Python.

## Step-by-Step Explaination:

### Install PyPDF2

Install PyPDF2 with pip

```sh
pip install PyPDF2
```

### Import PyPDF2

Import PyPDF2 in your Python file

```python
import PyPDF2
# Or
from PyPDF2 import PdfReader
```

### Create a reader object

```python
path = "/path/to/your/pdf-file.pdf"
reader = PdfReader(path)
```

### Extract Data

```python
number_of_pages = len(reader.pages)  # Return the number of pages
page = reader.pages[0]  # Return the page 0 Data
text = page.extract_text()  # Retrun the text of page 0
```