# booleans_and_none.py
# Boolean values, logical operators, comparisons, and None.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Boolean literals ---
True
False

# --- Logical operators (keywords, lowercase) ---
not True        # => False
not False       # => True
True and False  # => False  (both must be True)
False or True   # => True   (at least one must be True)

# 'and' returns the first falsy value, or the last value if all are truthy
# 'or'  returns the first truthy value, or the last value if all are falsy
# This is called short-circuit evaluation.
0 and 1      # => 0   (0 is falsy; stops there)
1 and 2      # => 2   (1 is truthy; evaluates and returns 2)
0 or 1       # => 1   (0 is falsy; tries next)
False or []  # => []  (both falsy; returns the last one)

# --- Comparison operators ---
1 == 1   # => True   (equality)
2 == 1   # => False
1 != 1   # => False  (inequality)
2 != 1   # => True
1 < 10   # => True
1 > 10   # => False
2 <= 2   # => True
2 >= 2   # => True

# Comparisons can be chained — Python evaluates each pair left to right
1 < 2 < 3     # => True   (same as 1 < 2 and 2 < 3)
2 < 3 < 2     # => False
1 < 2 > 0     # => True

# --- Identity vs. equality ---
# 'is' checks if two names refer to the SAME object in memory
# '==' checks if two objects have the SAME VALUE
a = [1, 2, 3]
b = [1, 2, 3]
a == b        # => True   (same values)
a is b        # => False  (different objects)
a is a        # => True

# CPython caches small integers (-5 to 256) and interned strings,
# so 'is' may return True for those — but never rely on this behavior.

# --- None ---
# None is Python's null / absence-of-value sentinel.
# There is exactly one None object; always compare with 'is', not '=='.
x = None
x is None     # => True   (correct way)
x == None     # => True   (works but is bad practice — '==' can be overridden)

# Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy.
bool(0)    # => False
bool("")   # => False
bool([])   # => False
bool(1)    # => True
bool("hi") # => True
bool([0])  # => True   (a list with one item is truthy, even if the item is 0)

# --- Type of None ---
type(None)  # => <class 'NoneType'>


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# 'all()' and 'any()' are the iterable equivalents of 'and'/'or'.
# Use them instead of chaining comparisons across a collection.
scores = [85, 90, 78, 92]
all(s >= 70 for s in scores)  # => True  (every score passes)
any(s >= 90 for s in scores)  # => True  (at least one score passes)

# None as a default sentinel for mutable default arguments —
# mutable defaults (like lists) are shared across all calls if declared
# directly in the signature. None sidesteps this classic bug.
def append_to(item, target=None):
    if target is None:
        target = []          # fresh list each call
    target.append(item)
    return target

append_to(1)   # => [1]
append_to(2)   # => [2]  (not [1, 2] — each call gets its own list)
