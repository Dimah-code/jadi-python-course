# Regular Expressions (RegEx) in Python

## Goal

- This exercise helps you understand how to use the re module in Python to:
- find patterns in text
- check if a string matches a pattern
- replace parts of text
- split text using a pattern

## Step-by-Step Explanation

### re.findall(pattern, text)

Finds all matches of a pattern and returns them as a list.
```python
re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
```
Finds all email addresses.

### re.match(pattern, text)

Checks if the pattern matches at the beginning of the string.
```python
re.match(r"^My", text)
```
^ means start of string.

### re.sub(pattern, replacement, text)

Replaces all occurrences of the pattern with another string.

```python
re.sub(r"\d", "#", "My number is 1234")  # → "My number is ####"
```

### re.split(pattern, text)

Splits the text using the pattern (like str.split(), but more flexible).
```python
re.split(r"\s+", "Split this   text")  # → ['Split', 'this', 'text']
```