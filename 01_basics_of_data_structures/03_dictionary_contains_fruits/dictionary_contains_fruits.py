fruit_prices = {"apple": 1500, "banana": 1000, "orange": 1200}
print("Fruits before change: \n", fruit_prices)

fruit_prices["banana"] = 1100
print("The price of banana changed to 1100")
print(fruit_prices)


fruit_prices.pop("apple")
print("apple deleted from dictionary")
print(fruit_prices)
