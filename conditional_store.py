price = int(input("Enter price: "))
if price > 50000:
    price = price - (price * (20 / 100))
    print(f"with 20% off {price}")
elif price > 20000:
    price = price - (price * (10 / 100))
    print(f'with 10% off {price}')
else:
    print(f"no off {price}")