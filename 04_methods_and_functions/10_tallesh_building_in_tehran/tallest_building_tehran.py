def skyline(*args):
    tallest = 0
    for i in args:
        if i > tallest:
            tallest = i
    return tallest

res = skyline(3, 7, 15, 2, 9)
res1 = skyline(1, 1, 1, 1, 1)

print(res)
print(res1)
