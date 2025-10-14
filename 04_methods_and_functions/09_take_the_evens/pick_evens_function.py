def pick_evens(*args):
    evens = []
    for i in args:
        if i % 2 == 0:
            evens.append(i)
        else:
            continue
    return evens


res = pick_evens(1, 3, 5, 7, 9)
res1 = pick_evens(1, 2, 3, 4, 5, 6, 7, 8)

print(res)
print(res1)
