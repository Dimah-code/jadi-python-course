def is_greater(a, b):
    if a > b:
        return True
    elif a <= b:
        return False


a = int(input("Enter a: "))
b = int(input("Enter b: "))

res = is_greater(a, b)

print(res)
