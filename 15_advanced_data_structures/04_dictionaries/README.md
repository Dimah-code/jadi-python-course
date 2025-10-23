# Python Dictionaries

## Overview
This exercise demonstrates Python dictionary operations, from basic CRUD operations to advanced patterns and nested structures.

## Dictionary Fundamentals

### Creation & Basic Operations
- **Empty Dict**: `{}` or `dict()`
- **Initialization**: Key-value pairs in `{key: value}` format
- **Adding/Updating**: Direct assignment or `update()` method
- **Access**: Direct `dict[key]` or safe `dict.get(key, default)`

### Key Methods
- **Retrieval**: `keys()`, `values()`, `items()`
- **Modification**: `pop()`, `popitem()`, `clear()`
- **Membership**: `in` operator for key checking

## Advanced Features

### Dictionary Comprehensions
- Transform and filter dictionaries efficiently
- Syntax: `{key: value for key, value in dict.items() if condition}`

### Copying Behavior
- **Reference**: `dict2 = dict1` (shared object)
- **Shallow Copy**: `dict2 = dict1.copy()` (independent object)

### Specialized Dictionary Types
- **setdefault()**: Get or set default value safely
- **defaultdict**: Automatic default values for missing keys
- **Nested Dictionaries**: Multi-level data structures

## Common Use Cases

### Data Organization
- Structured data storage with fast lookups
- Configuration settings and key-value pairs
- JSON-like nested data structures

### Performance Patterns
- Counting occurrences with `defaultdict(int)`
- Grouping data with nested dictionaries
- Efficient data transformations with comprehensions

## Best Practices

1. **Use `.get()`** for safe key access with default values
2. **Leverage comprehensions** for clean data transformations
3. **Choose `defaultdict`** when you need automatic defaults
4. **Use `.copy()`** when you need independent dictionary copies
5. **Prefer `in` operator** for membership testing
