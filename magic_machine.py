n = int(input("Enter a number: "))

if 2 <= n <= 1000:
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        print(n)
print("END")
        
