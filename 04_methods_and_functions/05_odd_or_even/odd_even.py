def is_even(num):
    return True if num % 2 == 0 else False


number = int(input("Enter a number: "))

res = is_even(number)

print(res)
