# Python Sets 

This program demonstrates fundamental set operations and concepts in Python, including set creation, modification, and common set operations.

## Set Basics

### Creating Sets
- **Empty Set**: `set()` - Note: `{}` creates a dictionary, not a set
- **Initialized Set**: `{1, 2, 3}` - Create with initial values

### Modifying Sets
- **Add Elements**: `.add(element)` - Insert single element
- **Remove Elements**: 
  - `.remove(element)` - Raises KeyError if element not found
  - `.discard(element)` - Safe removal (no error if element missing)
- **Clear Set**: `.clear()` - Remove all elements

## Important Concepts

### Reference vs Copy
- **Reference Assignment**: `set_b = set_a` - Both variables point to same object
- **Independent Copy**: `set_b = set_a.copy()` - Creates separate set object
- **Memory Behavior**: Changes to referenced sets affect all variables pointing to it

## Set Operations

### Common Operations
- **Difference**: `set_a.difference(set_b)` - Elements in A but not in B
- **Union**: `set_a.union(set_b)` - All unique elements from both sets
- **Intersection**: `set_a.intersection(set_b)` - Common elements in both sets

## Key Properties
- **Unordered**: No guaranteed element order
- **Unique Elements**: No duplicates allowed
- **Mutable**: Can modify after creation
- **Mathematical Operations**: Supports set theory operations

## Usage Examples
Perfect for:
- Removing duplicates from lists
- Membership testing
- Mathematical set operations
- Finding unique elements in data


## Example Output:

```sh
Empty set: set()
After adding 2 and 4: {2, 4}
Initial number set: {1, 2, 3}
After removing 2: {1, 3}
After discarding 100: {1, 3}
After clearing set: set()
Original set: {1, 2, 3} Reference: {1, 2, 3}
After adding 100 to original:
Original set: {1, 2, 3, 100} Reference: {1, 2, 3, 100}
Set A: {4, 5, 6} Set B (copy): {4, 5, 6}
After adding 99 to Set A:
Set A: {99, 4, 5, 6} Set B (copy): {4, 5, 6}
Difference (Set A - Set B): {99}
Union of Set A and Set B: {99, 4, 5, 6}
Intersection of Set A and Set B: {4, 5, 6}
```