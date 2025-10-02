def sum_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum if sum > 0 else 0

res = sum_numbers(0, 0 , 0)

print(res)