def sum_numbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum if sum > 0 else 0


first_try = sum_numbers(5, 10, 15)
second_try = sum_numbers()
third_try = sum_numbers(10, 20, 30)

print(f"Sum of numbers(5, 10, 15) = {first_try}")
print(f"Sum of numbers() = {second_try}")
print(f"Sum of numbers(10, 20, 30) = {third_try}")
