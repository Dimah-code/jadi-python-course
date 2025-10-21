# Math Module Basics in Python

### Goal

- This exercise helps you practice how to use Python’s math module for:
- working with constants (pi, e)
- performing square roots and powers
- using trigonometric functions
- rounding numbers
- computing factorials and combinations

## Step-by-Step Explanation

### Constants:

```python
math.pi   # 3.141592653589793
math.e    # 2.718281828459045
```
#### These are the mathematical constants π and e.

### Square root and power

```python
math.sqrt(16)   # → 4.0
math.pow(2, 5)  # → 32.0
```

### Trigonometry
- The math module works in radians, not degrees.
- So, before using sin() or cos(), you convert:

```python
math.radians(45)
```

### Rounding

```python
math.floor(5.67)  # → 5
math.ceil(5.67)   # → 6
```

### Factorials and combinations

```python
math.factorial(5)  # → 120
math.comb(5, 2)    # → 10
```

# Random Module Basics in Python

## Goal:

- This exercise helps you understand how to use Python’s random module to:
- generate random numbers
- choose random items
- shuffle lists
- and create random samples

## Step-by-Step Explanation


### random.random()

```python
random.random()  # e.g., 0.7382
```
Returns a floating-point number between 0.0 and 1.0.

### random.randint(a, b)

```python
random.randint(1, 10)  # e.g., 7
```

### random.choice(sequence)

```python
random.choice(["red", "green", "blue"]) # e.g., green
```
Returns a random element from a list, tuple, or string.

### random.shuffle(list)

```python
numbers = [1, 2, 3]
random.shuffle(numbers)
```
Randomly reorders the items in place.

### random.sample(population, k)

```python
random.sample(range(1, 11), 3)
```
Returns a list of k unique elements chosen randomly.
