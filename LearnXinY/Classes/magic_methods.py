# magic_methods.py
# Dunder (__double_underscore__) methods that Python calls implicitly.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# Magic methods (also called dunder methods or special methods) let your
# objects integrate with Python's syntax and built-in functions naturally.

class Vector:
    """2D vector — demonstrates the most commonly useful dunder methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # --- String representation ---
    def __str__(self):
        """Called by print() and str(). Aim for readability."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Called by repr() and in the REPL. Aim for unambiguity."""
        return f"Vector({self.x!r}, {self.y!r})"

    # --- Equality and hashing ---
    def __eq__(self, other):
        """Called by ==. Define __hash__ too if you define __eq__."""
        if not isinstance(other, Vector):
            return NotImplemented   # let the other side try
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """Required to use Vector in a set or as a dict key."""
        return hash((self.x, self.y))

    # --- Arithmetic operators ---
    def __add__(self, other):
        """Called by +."""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Called by -."""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Called by * when Vector is on the left: v * 3."""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Called by * when Vector is on the right: 3 * v."""
        return self.__mul__(scalar)

    def __neg__(self):
        """Called by unary -."""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """Called by abs(). Returns the magnitude."""
        return (self.x**2 + self.y**2) ** 0.5

    def __bool__(self):
        """Called in boolean contexts: if v, not v, etc."""
        return self.x != 0 or self.y != 0   # zero vector is falsy

    # --- Container protocol ---
    def __len__(self):
        """Called by len(). For a 2D vector, always 2."""
        return 2

    def __getitem__(self, index):
        """Called by v[0], v[1]. Enables tuple-style unpacking too."""
        return (self.x, self.y)[index]

    def __iter__(self):
        """Called by for loops and unpacking. Yields x then y."""
        yield self.x
        yield self.y

    def __contains__(self, value):
        """Called by 'in' operator."""
        return value in (self.x, self.y)


# --- Usage ---
v1 = Vector(1, 2)
v2 = Vector(3, 4)

str(v1)              # => "(1, 2)"
repr(v1)             # => "Vector(1, 2)"

v1 == Vector(1, 2)   # => True
v1 == v2             # => False
{v1, v2}             # works because __hash__ is defined

v1 + v2              # => Vector(4, 6)
v1 - v2              # => Vector(-2, -2)
v1 * 3               # => Vector(3, 6)
3 * v1               # => Vector(3, 6)  (__rmul__)
-v1                  # => Vector(-1, -2)
abs(v2)              # => 5.0

bool(Vector(0, 0))   # => False
bool(v1)             # => True

len(v1)              # => 2
v1[0]                # => 1
x, y = v1            # unpacking works via __iter__
1 in v1              # => True  (__contains__)


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Context manager protocol: __enter__ / __exit__
# Implement these to use your class with the 'with' statement.
# __exit__ receives exception info; return True to suppress the exception.
class ManagedFile:
    def __init__(self, path, mode="r"):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self._file = open(self.path, self.mode)
        return self._file      # value bound to 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        return False           # don't suppress exceptions

# with ManagedFile("data.txt", "w") as f:
#     f.write("hello")

# __call__ makes an instance behave like a function.
# Useful for callable objects that carry state (a step up from closures).
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)
double(5)                     # => 10
triple(5)                     # => 15
list(map(double, [1, 2, 3, 4]))   # => [2, 4, 6, 8]
