# assignment.py
# Variable assignment, naming rules, multiple assignment, and swapping.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Basic assignment ---
# Python is dynamically typed; no type declaration needed.
some_var = 5
some_var      # => 5

# Naming convention: snake_case for variables and functions (PEP 8)
my_variable = 10
another_var = "hello"

# Accessing a name that was never assigned raises NameError
# some_other_var  # => NameError: name 'some_other_var' is not defined

# --- Type reassignment ---
# A variable can be rebound to any type at any time.
x = 5
x = "now a string"
x = [1, 2, 3]

# --- Ternary / inline conditional assignment ---
# value_if_true if condition else value_if_false
label = "positive" if 3 > 0 else "non-positive"   # => "positive"
"yay!" if 0 > 1 else "nay!"                         # => "nay!"

# --- Multiple assignment in one line ---
a = b = c = 0          # all three names point to the same 0

# Tuple unpacking — right side evaluated fully before assignment
a, b, c = 1, 2, 3
a  # => 1
b  # => 2
c  # => 3

# Extended unpacking with * collects remaining items into a list
first, *rest = [1, 2, 3, 4, 5]
first   # => 1
rest    # => [2, 3, 4, 5]

head, *middle, tail = [1, 2, 3, 4, 5]
head    # => 1
middle  # => [2, 3, 4]
tail    # => 5

# --- Swapping without a temporary variable ---
x = 1
y = 2
x, y = y, x    # Python evaluates the right side first as a tuple
x  # => 2
y  # => 1

# --- Augmented assignment ---
n = 10
n += 5    # n = 15
n -= 3    # n = 12
n *= 2    # n = 24
n //= 5   # n = 4
n **= 3   # n = 64

# --- Constants (convention only — Python has no true constants) ---
# Use ALL_CAPS to signal "don't change this"
MAX_CONNECTIONS = 100
PI = 3.14159


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Chained comparisons read like math and avoid redundant variable reads.
# Python checks each adjacent pair and short-circuits on the first False.
age = 25
is_working_age = 18 <= age < 65   # => True — cleaner than age >= 18 and age < 65

# Type annotations (PEP 526) document intent without enforcing it at runtime.
# Tools like mypy and IDEs use these for static analysis.
count: int = 0
greeting: str = "hello"
ratios: list[float] = [0.1, 0.5, 0.9]
# The annotation is stored in __annotations__ but does NOT restrict assignment.
