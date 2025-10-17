n = int(input("Enter n: "))
x = int(input("Enter x: "))

for _ in range(n):
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 2 - 1
print(x)
