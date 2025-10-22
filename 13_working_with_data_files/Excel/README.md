# Writing to Excel files

## Goal:

This exercise helps you to understand how to write data to an Excel file.

## Step-by-Step Explaination

### Install `openpyxl`

```sh
pip install openpyxl
```

### Import openpyxl

Import openpyxl module to your file
```python
import openpyxl
```

### Open a workbook

```python
wb = Workbook()
```

### Grab the activate sheet

```python
ws = wb.activate
```

### Enter data to a cell

```python
ws['A1'] = 2
```

### Enter rows

```python
ws.append([2, 4, 6])
```

### Save the Excel file

```python
path = "path/where/you/want/file-name.xlsx"

# save the file
wb.save(path)