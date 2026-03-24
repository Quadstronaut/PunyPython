# tuples.py
# Tuples: immutable sequences and when/why to use them over lists.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Creation ---
tup = (1, 2, 3)
also_a_tuple = 1, 2, 3   # parens are optional; the comma makes it a tuple

# A single-element tuple REQUIRES a trailing comma — otherwise Python
# interprets the parens as grouping, not a tuple constructor.
not_a_tuple = (1)     # => int 1
is_a_tuple  = (1,)    # => tuple (1,)
type((1))             # => <class 'int'>
type((1,))            # => <class 'tuple'>

# Empty tuple
empty = ()

# --- Immutability ---
# Tuples cannot be modified after creation; this is intentional.
# Use a tuple when the data should not change (coordinates, RGB values,
# database rows, dictionary keys, function return bundles, etc.)
# tup[0] = 9  # => TypeError: 'tuple' object does not support item assignment

# --- Indexing and slicing (same as lists) ---
tup[0]     # => 1
tup[-1]    # => 3
tup[1:3]   # => (2, 3)
len(tup)   # => 3

# --- Concatenation (produces a new tuple) ---
tup + (4, 5, 6)   # => (1, 2, 3, 4, 5, 6)

# --- Membership ---
2 in tup   # => True

# --- Unpacking ---
# Assign each element to a name in one step — cleaner than indexing.
a, b, c = (1, 2, 3)
a  # => 1
b  # => 2
c  # => 3

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
first   # => 1
rest    # => [2, 3, 4, 5]  (note: * always gives a LIST, not a tuple)

# Swap without a temp variable — Python evaluates the right side first
d, e = 4, 5
d, e = e, d    # d => 5, e => 4

# --- Tuples as dictionary keys ---
# Lists are mutable (unhashable) so they cannot be dict keys.
# Tuples are hashable as long as all their elements are also hashable.
point_labels = {(0, 0): "origin", (1, 0): "unit x", (0, 1): "unit y"}
point_labels[(0, 0)]   # => "origin"

# --- Named tuples (stdlib) ---
# Give each position a name — self-documenting and still immutable.
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x    # => 3
p.y    # => 4
p[0]   # => 3  (index access still works)


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Returning multiple values from a function is a tuple under the hood.
# Explicit tuple syntax makes the intent clearer to readers.
def min_max(seq):
    return min(seq), max(seq)   # returns a tuple, no parens needed

lo, hi = min_max([3, 1, 4, 1, 5, 9])   # unpack directly at the call site
# lo => 1, hi => 9

# tuple() is slightly faster to iterate and uses less memory than list
# because Python can store it more compactly (no growth buffer).
# Prefer tuples for fixed-size data you'll only read, never mutate.
import sys
lst = [1, 2, 3, 4, 5]
tpl = (1, 2, 3, 4, 5)
sys.getsizeof(lst)   # typically 120 bytes
sys.getsizeof(tpl)   # typically 80 bytes  (varies by platform)
