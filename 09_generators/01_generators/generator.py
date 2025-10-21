def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


num = int(input("Enter a number: "))
counter = count_up_to(num)

for this_number in counter:
    print(this_number)
