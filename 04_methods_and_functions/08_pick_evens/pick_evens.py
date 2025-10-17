def pick_evens(*args):
    evens = []
    for i in args:
        if i % 2 == 0:
            evens.append(i)
        else:
            continue
    return evens


first_result = pick_evens(1, 2, 3, 4, 5, 6)
second_result = pick_evens(7, 13, 19, 21)

print(first_result)
print(second_result)
