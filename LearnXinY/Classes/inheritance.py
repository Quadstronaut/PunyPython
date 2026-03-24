# inheritance.py
# Single inheritance, multiple inheritance, super(), and the MRO.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Base class ---
class Human:
    species = "H. sapiens"

    def __init__(self, name):
        self.name = name

    def say(self, msg):
        print(f"{self.name}: {msg}")

    def sing(self):
        return "yo... yo... microphone check..."

    @classmethod
    def get_species(cls):
        return cls.species


# --- Single inheritance ---
class Superhero(Human):
    # Class attribute shadows Human.species for this class and its subclasses
    species = "Superhuman"

    def __init__(self, name, movie=False, superpowers=None):
        self.fictional = True
        self.movie = movie
        # Avoid the mutable-default-argument trap by defaulting to None
        self.superpowers = superpowers or ["super strength", "bulletproofness"]
        super().__init__(name)   # delegate to Human.__init__

    # Overriding an inherited method
    def sing(self):
        return "Dun, dun, DUN!"

    def boast(self):
        for power in self.superpowers:
            print(f"I wield the power of {power}!")


sup = Superhero(name="Tick")

isinstance(sup, Human)        # => True   (Superhero IS-A Human)
isinstance(sup, Superhero)    # => True
type(sup) is Human            # => False  (exact type check)
type(sup) is Superhero        # => True

sup.get_species()   # => "Superhuman"  (cls bound to Superhero)
sup.sing()          # => "Dun, dun, DUN!"  (overridden)
sup.say("Spoon!")   # => "Tick: Spoon!"    (inherited)
sup.boast()


# --- Multiple inheritance ---
class Bat:
    species = "Baty"

    def __init__(self, can_fly=True):
        self.fly = can_fly

    def say(self, msg):
        # Call the next class in the MRO chain via super()
        return super().say("... ... ...")

    def sonar(self):
        return "))) ... ((("


class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            superpowers=["Wealthy", "Prepared", "Determined"],
            **kwargs,
        )

    def sing(self):
        return "nan nan nan nan nan batman!"


bat = Batman(name="Sad Affleck")
bat.sing()               # => "nan nan nan nan nan batman!"
bat.sonar()              # => "))) ... ((("
bat.say("I am Batman")   # => "Sad Affleck: ... ... ..."
bat.fly                  # => True  (from Bat.__init__ via super() chain)

# --- Method Resolution Order (MRO) ---
# Python uses C3 linearization to determine the order in which base
# classes are searched. Check it with __mro__ or mro().
[c.__name__ for c in Batman.__mro__]
# => ['Batman', 'Superhero', 'Human', 'Bat', 'object']

# super() follows the MRO, not just the direct parent — this is what makes
# cooperative multiple inheritance work correctly.


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Abstract base classes (abc) enforce that subclasses implement required
# methods at instantiation time, not at the first method call.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self):
        return f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

# Shape()       # => TypeError: Can't instantiate abstract class Shape
Rectangle(3, 4).describe()   # => "area=12.00, perimeter=14.00"

# Mixin pattern — small classes that add a single, reusable behaviour.
# Combine freely via multiple inheritance without deep hierarchies.
class JsonMixin:
    """Adds .to_json() to any class that has a __dict__."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__, default=str)

class LogMixin:
    """Adds .log() that prints the repr of self."""
    def log(self):
        print(repr(self))

class User(JsonMixin, LogMixin):
    def __init__(self, name, email):
        self.name  = name
        self.email = email

    def __repr__(self):
        return f"User(name={self.name!r})"

u = User("Alice", "alice@example.com")
u.log()        # => User(name='Alice')
u.to_json()    # => '{"name": "Alice", "email": "alice@example.com"}'
