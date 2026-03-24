# properties_and_statics.py
# @property, @classmethod, @staticmethod — controlling attribute access
# and attaching utility functions to a class without needing an instance.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name
        self._age = 0    # backing attribute; accessed via the property below

    # --- @property — computed or validated attribute access ---
    # Lets you use attribute syntax (obj.age) while running getter logic.
    @property
    def age(self):
        return self._age

    # @<name>.setter — runs when you do obj.age = value
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # @<name>.deleter — runs when you do del obj.age
    @age.deleter
    def age(self):
        del self._age

    # --- @classmethod — receives the CLASS as its first argument (cls) ---
    # Use for alternative constructors or factory methods that don't need
    # a specific instance but do need to create or reference the class.
    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor: create a Human from a birth year."""
        import datetime
        age = datetime.date.today().year - birth_year
        obj = cls(name)
        obj.age = age
        return obj

    # --- @staticmethod — no implicit first argument ---
    # Logically belongs to the class but doesn't need self or cls.
    # Use when the function is a pure utility related to the class concept.
    @staticmethod
    def grunt():
        return "*grunt*"

    @staticmethod
    def is_adult(age):
        return age >= 18


# --- Usage ---
ian = Human("Ian")

ian.age           # => 0      (getter)
ian.age = 30      # (setter)
ian.age           # => 30
del ian.age       # (deleter)

Human.get_species()        # => "H. sapiens"  (classmethod via class)
ian.get_species()          # => "H. sapiens"  (classmethod via instance — also fine)

Human.grunt()              # => "*grunt*"     (staticmethod via class)
ian.grunt()                # => "*grunt*"     (staticmethod via instance — also fine)

bob = Human.from_birth_year("Bob", 1995)   # alternative constructor
Human.is_adult(20)   # => True
Human.is_adult(15)   # => False

# --- Mutating a class attribute affects all instances ---
Human.species = "H. neanderthalensis"
ian.get_species()   # => "H. neanderthalensis"


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Cached property (Python 3.8+) — computes once and stores the result as
# an instance attribute, bypassing the property on subsequent accesses.
# Use for expensive read-only computed attributes.
from functools import cached_property
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("computing...")    # only prints on the first access
        return math.pi * self.radius ** 2

c = Circle(5)
c.area   # => computing...  78.539...
c.area   # => 78.539...     (no "computing..." — returned from cache)

# Read-only property: define a getter but no setter.
# Attempting to set raises AttributeError, making the attribute effectively
# immutable from outside the class without using __slots__.
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(100)
t.fahrenheit          # => 212.0
# t.fahrenheit = 99   # => AttributeError: can't set attribute
