import itertools as it

# =============================================================================
# CYCLE ITERATOR DEMONSTRATION
# =============================================================================

# Create a cycle iterator that infinitely repeats the sequence [1, 2, 3]
number_cycle = it.cycle([1, 2, 3])

# Uncomment the following code to see infinite cycling:
# print("Cycle iterator demonstration (infinite):")
# for num in number_cycle:
#     print(num)
# Output: 1, 2, 3, 1, 2, 3, 1, 2, 3, ... (infinite loop)

# =============================================================================
# COMBINATIONS DEMONSTRATION
# =============================================================================

# Define a sample list of numbers
numbers = [1, 2, 3, 4]

# Generate all possible combinations of 2 elements from the list
# combinations() returns unique pairs without repetition, order doesn't matter
combinations_result = list(it.combinations(numbers, 2))

print("All combinations of 2 elements from [1, 2, 3, 4]:")
for combination in combinations_result:
    print(combination)
# Output: (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)

# =============================================================================
# COMBINATIONS WITH REPLACEMENT DEMONSTRATION
# =============================================================================

# Generate combinations allowing the same element to be repeated
# combinations_with_replacement() allows elements to be chosen multiple times
combinations_with_repl = list(it.combinations_with_replacement(numbers, 2))

print("\nAll combinations with replacement of 2 elements from [1, 2, 3, 4]:")
for combination in combinations_with_repl:
    print(combination)
# Output: (1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)
