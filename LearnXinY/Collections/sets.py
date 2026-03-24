# sets.py
# Set creation, membership, and mathematical set operations.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Creation ---
# Sets are unordered collections of UNIQUE, HASHABLE elements.
empty_set = set()                  # {} would create an empty dict, not a set
some_set = {1, 1, 2, 2, 3, 4}     # => {1, 2, 3, 4}  (duplicates silently dropped)

# From any iterable
from_list = set([1, 2, 2, 3])     # => {1, 2, 3}
from_str  = set("hello")          # => {'h', 'e', 'l', 'o'}  (unique chars)

# --- Mutation ---
some_set.add(5)       # => {1, 2, 3, 4, 5}
some_set.add(3)       # no-op; 3 is already in the set
some_set.discard(99)  # remove if present; no error if missing
some_set.remove(5)    # remove; raises KeyError if missing

# --- Membership (O(1) average — backed by a hash table) ---
2 in some_set    # => True
10 in some_set   # => False

# --- Set operations (operator syntax) ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a & b    # intersection   => {3, 4}         (elements in both)
a | b    # union          => {1, 2, 3, 4, 5, 6}
a - b    # difference     => {1, 2}         (in a but not b)
b - a    # difference     => {5, 6}         (in b but not a)
a ^ b    # symmetric diff => {1, 2, 5, 6}   (in one but not both)

# --- Set operations (method syntax — accepts any iterable, not just sets) ---
a.intersection(b)
a.union(b)
a.difference(b)
a.symmetric_difference(b)

# In-place variants (mutate a)
a &= b    # a becomes intersection
a |= b    # a becomes union
a -= b    # a becomes difference
a ^= b    # a becomes symmetric difference

# --- Subset / superset checks ---
{1, 2} <= {1, 2, 3}    # => True   ({1,2} is a subset of {1,2,3})
{1, 2} < {1, 2, 3}     # => True   (proper subset — strictly smaller)
{1, 2, 3} >= {1, 2}    # => True   (superset)
{1, 2} <= {1, 2}       # => True   (a set is a subset of itself)
{1, 2} < {1, 2}        # => False  (not a PROPER subset)

{1, 2}.isdisjoint({3, 4})  # => True  (no elements in common)

# --- Frozenset (immutable set — can be used as a dict key or set element) ---
fs = frozenset({1, 2, 3})
# fs.add(4)  # => AttributeError: frozenset has no add


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Fast deduplication: converting to a set and back removes duplicates in O(n).
# Order is NOT preserved (use dict.fromkeys() if you need order-preservation).
dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_unordered = list(set(dupes))             # order not guaranteed
unique_ordered   = list(dict.fromkeys(dupes))   # preserves first-seen order

# Set algebra for data reconciliation — finding what changed between two
# snapshots without writing nested loops.
yesterday = {"alice", "bob", "carol"}
today     = {"bob", "carol", "dave"}

joined  = today - yesterday    # => {'dave'}          (new arrivals)
left    = yesterday - today    # => {'alice'}         (departures)
stayed  = yesterday & today    # => {'bob', 'carol'}
