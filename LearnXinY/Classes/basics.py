# basics.py
# Class definition, __init__, instance attributes, and instance methods.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Defining a class ---
class Human:
    # Class attribute — shared by ALL instances.
    # Changing it via the class (Human.species = ...) affects all instances
    # that haven't shadowed it with their own instance attribute.
    species = "H. sapiens"

    # __init__ is called automatically when an instance is created.
    # 'self' is the new instance; by convention always the first parameter.
    def __init__(self, name):
        self.name = name    # instance attribute — unique to each object
        self._age = 0       # leading _ signals "private by convention"

    # Instance method — first argument is always self (the calling instance)
    def say(self, msg):
        print(f"{self.name}: {msg}")

    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

# --- Instantiation ---
ian  = Human(name="Ian")
joel = Human("Joel")      # positional arg works too

ian.say("hi")             # => "Ian: hi"
joel.say("hello")         # => "Joel: hello"

# --- Accessing attributes ---
ian.name       # => "Ian"
ian.species    # => "H. sapiens"  (falls back to class attribute)

# --- __str__ and __repr__ ---
# __str__  : human-readable; used by print() and str()
# __repr__ : unambiguous; used in the REPL, repr(), and as fallback for str()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

p = Point(3, 4)
print(p)    # => (3, 4)        — calls __str__
repr(p)     # => "Point(3, 4)" — calls __repr__

# --- dataclasses (Python 3.7+) ---
# @dataclass auto-generates __init__, __repr__, and __eq__ from field annotations.
# Use when your class is primarily a data container.
from dataclasses import dataclass

@dataclass
class Coordinate:
    lat: float
    lon: float
    label: str = ""                  # field with default value

    def distance_to_origin(self):
        return (self.lat**2 + self.lon**2) ** 0.5

c = Coordinate(lat=40.7128, lon=-74.0060, label="NYC")
print(c)    # => Coordinate(lat=40.7128, lon=-74.006, label='NYC')
c == Coordinate(40.7128, -74.0060, "NYC")  # => True  (__eq__ generated)


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# __slots__ restricts the set of valid instance attributes and reduces
# per-instance memory by replacing the default __dict__ with a fixed array.
# Valuable when you create millions of small objects (e.g. game entities).
class Vector:
    __slots__ = ("x", "y")   # only x and y are allowed as attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

v = Vector(1, 2)
# v.z = 3   # => AttributeError: 'Vector' object has no attribute 'z'

# __eq__ and __hash__ together allow custom objects to work correctly in
# sets and as dict keys. If you define __eq__, define __hash__ too;
# Python sets __hash__ = None if you define only __eq__.
@dataclass(frozen=True)   # frozen=True makes the dataclass hashable
class Color:
    r: int
    g: int
    b: int

palette = {Color(255, 0, 0), Color(0, 255, 0)}   # works because Color is hashable
Color(255, 0, 0) in palette   # => True
