# Working with CSV files

## Goal:

This exercise helps you to understand how to use `CSV` files in Python

## Step-by-Step Explaination

### Import CSV module

```python
import csv
```

### Open a CSV file

```python
with open(path) as csvfile:
    csv_data = csv.reader(csvfile)
```
Return the data into `csv_data` variable

### Use the extracted data

```python
    for line in csv_data:
        print(f"Customer ID: {line[1]}, Company: {line[4]}")
```