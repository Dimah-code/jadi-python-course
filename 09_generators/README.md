## Python Generators

### What is a Generator?

A **generator** in Python is a special type of function that lets you **yield** values one at a time, instead of returning them all at once.
It’s a memory-efficient way to create iterators — great for handling large datasets or infinite sequences.

### How It Works

* You define a generator using the `yield` keyword (instead of `return`).
* Each time the generator’s `__next__()` method (or `next()`) is called, execution resumes right **after the last `yield`**.
* Once all `yield` statements are done, the generator raises a `StopIteration` exception automatically.

---

### Example Code

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


num = int(input("Enter a number: "))
counter = count_up_to(num)

for this_number in counter:
    print(this_number)
```

### Input / Output

**Input:**
User enter a number, For example: 9

**Output:**

```
1
2
3
4
5
6
7
8
9
```
