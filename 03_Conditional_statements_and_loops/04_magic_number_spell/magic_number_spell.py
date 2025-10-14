for n in range(1, 21):
    if n % 5 == 0 and n % 3 == 0:
        print(f"{n} is a legendary number")
        continue
    elif n % 5 == 0:
        print(f"{n} is a cursed number")
        continue
    elif n % 3 == 0:
        print(f"{n} is a magical number")
        continue
    else:
        print(f"{n} is a normal number")
