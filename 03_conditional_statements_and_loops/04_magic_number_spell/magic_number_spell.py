n = int(input("Enter a number: "))

if n % 5 == 0 and n % 3 == 0:
    print(f"{n} is a legendary number")
elif n % 5 == 0:
    print(f"{n} is a cursed number")
elif n % 3 == 0:
    print(f"{n} is a magical number")
else:
    print(f"{n} is a normal number")
