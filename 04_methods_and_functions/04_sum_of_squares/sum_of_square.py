def sum_of_squares(a, b):
    a = a**2
    b = b**2
    sum = a + b

    return sum


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

sum = sum_of_squares(a, b)

print(f"Sum of squares: {sum}")
