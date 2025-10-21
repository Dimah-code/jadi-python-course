# Working with the Decimal Module in Python

## Goal

This exercise teaches you how to use Python’s decimal module to perform precise arithmetic without floating-point errors.

## Step-by-Step Explanation

```python
from decimal import Decimal
```

- Imports the Decimal class, which represents precise decimal numbers.
- Unlike floats, it avoids tiny rounding errors.

### Setting precision

```python
getcontext().prec = 6
```
Sets the number of significant digits for calculations.

### Creating Decimal values

```python
a = Decimal("0.1")
b = Decimal("0.2")
```
Always pass numbers as strings to avoid inheriting float errors.

### Comparison with floats

```python
0.1 + 0.2 == 0.3   # False (because of float inaccuracy)
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # True
```

### Precise math

```python
price = Decimal("19.99")
tax_rate = Decimal("0.075")
total = price + (price * tax_rate)
```

### Rounding

```python
total.quantize(Decimal("0.01"))  # round to 2 decimal places
```

