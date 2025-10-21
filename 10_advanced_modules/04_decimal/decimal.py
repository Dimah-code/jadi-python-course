from decimal import Decimal, getcontext

# Set precision (number of decimal places)
getcontext().prec = 6

# Create Decimal numbers
a = Decimal("0.1")
b = Decimal("0.2")
c = a + b

print("Using Decimal:")
print("0.1 + 0.2 =", c)

# Compare with normal float
print("\nUsing float:")
print("0.1 + 0.2 =", 0.1 + 0.2)

# Perform some precise calculations
price = Decimal("19.99")
tax_rate = Decimal("0.075")
total = price + (price * tax_rate)
print("\nPrice with tax:", total)

# Rounding example
rounded_total = total.quantize(Decimal("0.01"))  # round to 2 decimal places
print("Rounded total:", rounded_total)
