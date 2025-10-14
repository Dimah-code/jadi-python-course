def divide(a, b):

    result = a / b
    return result
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("Result:", divide(num1, num2))
except ValueError as e:
    print(f"Enter valid numbers! Error: {e}")
except ZeroDivisionError as e:
    print(f"Cannot division to 0! Error: {e}")
except Exception as e:
    print(f"Unexcepted error! Error: {e}")
