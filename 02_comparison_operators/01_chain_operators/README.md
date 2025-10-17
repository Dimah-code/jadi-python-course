## Chaining operator Exercise

In Python, you can use comparison operators in a chained manner.
For example, the expression a < b <= c is equivalent to two separate comparisons:
```txt
 a < b and b <= c
```
This allows you to perform multiple comparisons in a single expression.

### Inputs:

Three integers named a, b, and c.

### Outputs:

If the condition a < b <= c is true, then display the output True.

Otherwise, display the output False.

### Sample input:
```txt
 5
 10
 15
```

### Sample output:
```txt
 True
```

### Tip:

To get input from the user, you can use the following command:
```python
 a = input()
```
Now if we want to convert this input to int at the same time, we have:
```python
 a = int(input())
```