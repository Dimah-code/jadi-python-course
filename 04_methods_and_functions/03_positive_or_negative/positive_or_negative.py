def is_positive(num):
    if num >= 0:
        return True
    else:
        return False


inp = int(input("Enter a positive or negative number: "))

res = is_positive(inp)

print(res)
