# Datetime Basics in Python

## Goal:

### This exercise helps you understand how to use the datetime module to:

- get the current time
- format dates
- create specific dates
- calculate time differences
- and work with future or past dates

## Step-by-Step Explanation

### datetime.now():

- Returns the current date and time as a datetime object.

### strftime():

- Formats a datetime into a readable string.

### Example format codes:

- %Y → year (2025)

- %m → month (10)

- %d → day (21)

- %H:%M:%S → hour, minute, second

## Creating specific dates:

You can make a custom date/time:

```python
birthday = datetime(2005, 1, 20)
```