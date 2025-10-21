# Exercise on Handling Exceptions in the Divide Function

## Examine the following code and troubleshoot it.

## Goal:
- This function should take two numbers and return the value of their division, but handle it properly if there is a problem.

```python
def divide(a, b):
result = a / b
return result

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

print("Result:", divide(num1, num2))
```

### Your tasks:

This code will throw a ZeroDivisionError if num2 = 0. Handle this error.
If the user enters a non-numeric value (for example, hello), a ValueError will be thrown. Handle this error.
After the function executes, display a message saying "The program ran successfully!", even if an error occurs.
The program should not crash! Instead, it should prompt the user for valid input.