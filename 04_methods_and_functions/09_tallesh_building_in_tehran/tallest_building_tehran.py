def skyline(*args):
    tallest = 0
    for this_building in args:
        if this_building > tallest:
            tallest = this_building
    return tallest


first_result = skyline(3, 7, 15, 2, 9)
second_result = skyline(1, 1, 1, 1, 1)

print(first_result)
print(second_result)
