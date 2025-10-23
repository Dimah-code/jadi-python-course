# Create an empty set
empty_set = set()
print("Empty set:", empty_set)

# Add elements to set
empty_set.add(2)
empty_set.add(4)
print("After adding 2 and 4:", empty_set)

# Create set with initial values
number_set = {1, 2, 3}
print("Initial number set:", number_set)

# Remove element from set
number_set.remove(2)
print("After removing 2:", number_set)

# Discard element (safe removal - no error if element doesn't exist)
number_set.discard(100)  # 100 doesn't exist, but no error thrown
print("After discarding 100:", number_set)

# Clear all elements from set
number_set.clear()
print("After clearing set:", number_set)

# =============================================================================
# SET REFERENCES VS COPIES
# =============================================================================

# Reference assignment (both variables point to same set)
original_set = {1, 2, 3}
set_reference = original_set
print("Original set:", original_set, "Reference:", set_reference)

# Modifying original affects both (same object in memory)
original_set.add(100)
print("After adding 100 to original:")
print("Original set:", original_set, "Reference:", set_reference)

# Creating an independent copy
set_a = {4, 5, 6}
set_b = set_a.copy()  # Creates a shallow copy
print("Set A:", set_a, "Set B (copy):", set_b)

# Modifying original doesn't affect the copy
set_a.add(99)
print("After adding 99 to Set A:")
print("Set A:", set_a, "Set B (copy):", set_b)

# =============================================================================
# SET OPERATIONS
# =============================================================================

# Difference: Elements in set_a but not in set_b
print("Difference (Set A - Set B):", set_a.difference(set_b))

# Union: All unique elements from both sets
print("Union of Set A and Set B:", set_a.union(set_b))

# Intersection: Common elements in both sets
print("Intersection of Set A and Set B:", set_a.intersection(set_b))
