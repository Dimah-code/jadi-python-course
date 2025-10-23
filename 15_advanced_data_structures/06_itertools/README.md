# Python itertools Module

## Overview
This exercise demonstrates three fundamental functions from Python's `itertools` module: `cycle()`, `combinations()`, and `combinations_with_replacement()`.

## Functions Demonstrated

### 1. `itertools.cycle(iterable)`
- **Purpose**: Creates an infinite iterator that cycles through the elements of an iterable
- **Behavior**: Once it reaches the end, it starts over from the beginning
- **Use Case**: Generating repeating patterns, cycling through states
- **Warning**: Results in infinite loop if not controlled with break condition

### 2. `itertools.combinations(iterable, r)`
- **Purpose**: Generates all possible combinations of length `r` from the input iterable
- **Key Characteristics**:
  - Order doesn't matter (1,2) is same as (2,1)
  - No repetition of elements within a combination
  - Returns unique combinations only
- **Formula**: For n elements, returns n! / (r! * (n-r)!) combinations

### 3. `itertools.combinations_with_replacement(iterable, r)`
- **Purpose**: Generates combinations allowing the same element to be chosen multiple times
- **Key Characteristics**:
  - Order doesn't matter
  - Elements can be repeated within a combination
  - Includes combinations like (1,1), (2,2), etc.
- **Formula**: For n elements, returns (n+r-1)! / (r! * (n-1)!) combinations

## Output Examples

### Combinations of [1,2,3,4] choose 2:
```
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
```

### Combinations with Replacement of [1,2,3,4] choose 2:
```
(1, 1)
(1, 2)
(1, 3)
(1, 4)
(2, 2)
(2, 3)
(2, 4)
(3, 3)
(3, 4)
(4, 4)
```

## Key Differences
- **combinations()**: No repeated elements, smaller result set
- **combinations_with_replacement()**: Allows repeated elements, larger result set
- **cycle()**: Infinite iteration vs finite combinations
