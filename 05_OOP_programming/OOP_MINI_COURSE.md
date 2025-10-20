# Mini OOP Course

## 1. Why OOP?

* Organizes code around *objects* (data + behavior).
* Helps model real-world entities, reuse code, and manage complexity.

**Exercise:** Think of 3 objects in a simple app (e.g., blog: Post, Author, Comment).

## 2. Class and instance — basic syntax

```python
class Dog:
    # class attribute (shared by all instances)
    species = 'Canis familiaris'

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} says: Woof!"

# usage
buddy = Dog('Buddy', 3)
print(buddy.species)   # Canis familiaris
print(buddy.speak())   # Buddy says: Woof!
```

**Exercise:** Create two `Dog` instances with different names and ages; print their ages.

---

## 3. `__init__`, `__repr__`, and helpful dunder methods

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)          # Point(1, 2)
print(p1 == p2)    # True
```

**Exercise:** Add `__add__` to `Point` so `p1 + p2` returns a new `Point`.

---

## 4. Methods: instance, classmethod, staticmethod

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    @classmethod
    def unit_circle(cls):
        return cls(1)

    @staticmethod
    def is_valid_radius(r):
        return r >= 0

c = Circle.unit_circle()
print(c.area())
print(Circle.is_valid_radius(-1))
```

**Note:** `classmethod` receives the class; `staticmethod` receives nothing special.

**Exercise:** Write a `from_diameter` classmethod that constructs a circle from a diameter.

---

## 5. Inheritance and polymorphism

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return 'Meow'

class Dog(Animal):
    def speak(self):
        return 'Woof'

animals = [Cat(), Dog()]
for a in animals:
    print(a.speak())  # polymorphic dispatch
```

**Exercise:** Add a `describe` method to `Animal` that returns the class name and the result of `speak()`.

---

## 6. Encapsulation: public, protected, private (conventions)

* In Python, `_name` is a convention for protected, `__name` triggers name mangling for privacy.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # convention: "protected"

    def deposit(self, amount):
        if amount <= 0: raise ValueError('amount must be positive')
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance: raise ValueError('insufficient funds')
        self._balance -= amount

acct = BankAccount('Alice', 100)
acct.deposit(50)
# avoid touching acct._balance directly in real code
print(acct._balance)
```

**Exercise:** Try adding a `__secret` attribute and inspect its actual name in `acct.__dict__`.

---

## 7. Properties: safe attribute access

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0: raise ValueError('width must be > 0')
        self._width = value

r = Rectangle(3, 4)
print(r.area)  # 12
r.width = 5
print(r.area)  # 20
```

**Exercise:** Add a `height` property with getter and setter.

---

## 8. Composition vs Inheritance

Prefer composition when you "have a" relationship.

```python
class Engine:
    def start(self):
        return 'vroom'

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

car = Car(Engine())
print(car.start())
```

**Exercise:** Why choose composition here instead of inheriting Engine in Car?

---

## 9. Abstract Base Classes (ABC) and interfaces

```python
from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

class JsonSerializer(Serializer):
    def serialize(self, obj):
        import json
        return json.dumps(obj)

js = JsonSerializer()
print(js.serialize({'a': 1}))
```

**Exercise:** Create an XML serializer that implements `Serializer` (simple string output is fine).

---

## 10. Magic methods & container protocols

Implementing `__len__`, `__iter__`, `__getitem__` makes your objects behave like containers.

```python
class SimpleList:
    def __init__(self, items=None):
        self._items = list(items or [])

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

sl = SimpleList([1,2,3])
print(len(sl))
for x in sl:
    print(x)
print(sl[1])
```

**Exercise:** Add `append` and `__repr__` to `SimpleList`.

---

## 11. Common OOP pitfalls & style tips

* Avoid deep inheritance trees; prefer composition and small classes.
* Keep methods short and focused (Single Responsibility Principle).
* Use `__repr__` for debugging-friendly output and `__str__` for user-facing strings.
* Don’t overuse `@property` to hide heavy computations.

---

## 12. Mini project: Contact Manager

**Description:** A simple in-memory contact manager with `Contact` and `ContactBook` classes.

```python
class Contact:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Contact(name={self.name!r}, email={self.email!r}, phone={self.phone!r})"

class ContactBook:
    def __init__(self):
        self._contacts = []

    def add(self, contact):
        if any(c.name == contact.name for c in self._contacts):
            raise ValueError('contact with this name already exists')
        self._contacts.append(contact)

    def find(self, name):
        return [c for c in self._contacts if name.lower() in c.name.lower()]

    def remove(self, name):
        before = len(self._contacts)
        self._contacts = [c for c in self._contacts if c.name.lower() != name.lower()]
        return before != len(self._contacts)

# demo
book = ContactBook()
book.add(Contact('Alice', 'alice@example.com'))
book.add(Contact('Bob', 'bob@example.com', '+123'))
print(book.find('ali'))
print(book.remove('Bob'))
```

**Extensions:** persist to JSON, add update method, prevent duplicates by email, add sorting, write unit tests.

---

## 13. Exercises (short)

1. Implement a `Stack` class with `push`, `pop`, `peek`, and `is_empty`.
2. Create a small `Shape` hierarchy (`Shape`, `Circle`, `Square`) and compute total area for a list of shapes.
3. Write unit tests (pytest or unittest) for the `ContactBook` add/find/remove behavior.

