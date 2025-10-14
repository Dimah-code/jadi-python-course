def count_up():
    for i in range(3):
        yield i


gen = count_up()
print(list(gen))
