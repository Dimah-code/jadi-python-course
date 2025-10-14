def sum_of_squares(a, b):
    a = a**2
    b = b**2

    return a + b


n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

sum = sum_of_squares(n1, n2)

print(f"Sum of squares: {sum}")
