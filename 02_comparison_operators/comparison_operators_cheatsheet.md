```py
b = 10
a = 20

print(f"{a} == {b} →", a == b)
print(f"{a} != {b} →", a != b)
print(f"{a} > {b} →", a > b)
print(f"{a} < {b} →", a < b)
print(f"{a} >= {b} →", a >= b)
print(f"{a} <= {b} →", a <= b)

print("\n🔹 CHAINED COMPARISONS (Python feature!)")
x = 5
print("1 < x < 10 →", 1 < x < 10)
print("1 < x and x < 10 →", 1 < x and x < 10)
print("10 < x < 20 →", 10 < x < 20)
print("0 < x != 5 →", 0 < x != 5)

print("\n🔹 STRINGS COMPARISON (Lexicographic order)")
s1, s2 = "apple", "banana"
print(f"'{s1}' < '{s2}' →", s1 < s2)
print(f"'{s1}' == '{s2}' →", s1 == s2)
print("'Zebra' > 'apple' →", "Zebra" > "apple")

print("\n🔹 LIST AND TUPLE COMPARISON (Element-wise)")
print("[1, 2, 3] < [1, 2, 4] →", [1, 2, 3] < [1, 2, 4])
print("(1, 2, 3) == (1, 2, 3) →", (1, 2, 3) == (1, 2, 3))
print("[1, 2] > [1, 2, 0] →", [1, 2] > [1, 2, 0])  # False

print("\n🔹 IDENTITY OPERATORS: 'is' and 'is not'")
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a == b →", a == b)
print("a is b →", a is b)
print("a == c →", a == c)
print("a is not c →", a is not c)

print("\n🔹 MEMBERSHIP TESTS: 'in' and 'not in'")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits →", "apple" in fruits)
print("'grape' not in fruits →", "grape" not in fruits)
print("'an' in 'banana' →", "an" in "banana")

print("\n🔹 BOOLS AS INTS (True==1, False==0)")
print("True == 1 →", True == 1)
print("False == 0 →", False == 0)
print("True + True == 2 →", True + True == 2)
print("bool(5) == True →", bool(5) == True)
print("bool(0) == False →", bool(0) == False)

print("\n🔹 COMPARISON WITH NONE")
x = None
print("x is None →", x is None)
print("x == None →", x == None)
print("x is not None →", x is not None)

print("\n🔹 MIXED TYPE COMPARISONS (watch out!)")
try:
    print("[1, 2] > 'abc' →", [1, 2] > "abc")
except TypeError as e:
    print("TypeError:", e)

try:
    print("5 < '5' →", 5 < "5")
except TypeError as e:
    print("TypeError:", e)

print("\n🔹 OBJECT COMPARISONS WITH CUSTOM CLASSES")


class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1, p2, p3 = Person(25), Person(30), Person(25)
print("p1 == p2 →", p1 == p2)
print("p1 == p3 →", p1 == p3)
print("p1 < p2 →", p1 < p2)
print("p2 > p1 →", p2 > p1)

print("\n🔹 BONUS: Comparing Complex Numbers")
z1, z2 = 2 + 3j, 2 + 4j
print("z1 == z2 →", z1 == z2)
try:
    print("z1 < z2 →", z1 < z2)
except TypeError as e:
    print("TypeError:", e)

print("\nEND OF CHEATSHEET — EXPERIMENT FREELY!")
```