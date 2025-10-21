import random

# Generate a random float between 0 and 1
print("Random float (0–1):", random.random())

# Generate a random integer between 1 and 10
print("Random integer (1–10):", random.randint(1, 10))

# Choose a random item from a list
colors = ["red", "green", "blue", "yellow"]
print("Random color:", random.choice(colors))

# Shuffle a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)

# Generate a random sample (unique items)
print("Sample of 3 numbers from 1–10:", random.sample(range(1, 11), 3))
