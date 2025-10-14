x = int(input("Enter x: "))
n = int(input("Enter n: "))

for _ in range(n):
    if x % 2 == 0:
        x //= 2
    else:
        x = x * 2 - 1
print(x)
