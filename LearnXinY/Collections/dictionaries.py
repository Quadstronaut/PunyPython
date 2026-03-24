# dictionaries.py
# Dict creation, access, methods, iteration, and merging.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Creation ---
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}

# Keys must be hashable (strings, numbers, tuples of hashables).
# Values can be anything.
mixed_keys = {1: "int key", (0, 1): "tuple key", "str": "string key"}

# dict() constructor from keyword arguments
from_kwargs = dict(a=1, b=2, c=3)   # => {'a': 1, 'b': 2, 'c': 3}

# dict() constructor from iterable of (key, value) pairs
from_pairs = dict([("x", 10), ("y", 20)])

# --- Access ---
filled_dict["one"]    # => 1
# filled_dict["four"] # => KeyError: 'four'

# Safe access with .get() — returns None (or a default) instead of raising
filled_dict.get("one")          # => 1
filled_dict.get("four")         # => None
filled_dict.get("four", 0)      # => 0  (explicit default)

# --- Membership (checks keys, not values) ---
"one" in filled_dict    # => True
1 in filled_dict        # => False  (1 is a value, not a key here)

# --- Views ---
# .keys(), .values(), .items() return live views — they reflect mutations.
list(filled_dict.keys())    # => ["one", "two", "three"]
list(filled_dict.values())  # => [1, 2, 3]
list(filled_dict.items())   # => [("one", 1), ("two", 2), ("three", 3)]

# --- Mutation ---
filled_dict["four"] = 4          # add or overwrite a key
filled_dict.update({"five": 5})  # merge another dict in-place
filled_dict.setdefault("six", 6) # sets key only if it doesn't already exist
del filled_dict["one"]           # remove a key (KeyError if missing)
filled_dict.pop("two")           # remove and return value (KeyError if missing)
filled_dict.pop("missing", None) # safe pop with a default

# --- Iteration ---
for key in filled_dict:
    print(key)

for key, value in filled_dict.items():
    print(f"{key}: {value}")

# --- Merging (Python 3.9+) ---
defaults = {"color": "blue", "size": "medium"}
overrides = {"size": "large", "weight": "heavy"}
merged = defaults | overrides              # => new merged dict; overrides wins
defaults |= overrides                      # in-place merge

# Python 3.5-3.8 equivalent:
merged_old = {**defaults, **overrides}     # unpack both into a new dict literal

# --- Dict comprehension ---
squares = {x: x**2 for x in range(6)}     # => {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}
filtered = {k: v for k, v in squares.items() if v > 5}


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# collections.defaultdict removes the "check if key exists" boilerplate
# when grouping items. The factory function supplies a default value
# automatically on first access.
from collections import defaultdict

word_list = ["apple", "ant", "banana", "avocado", "blueberry"]
by_letter = defaultdict(list)
for word in word_list:
    by_letter[word[0]].append(word)
# => defaultdict(<class 'list'>, {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'blueberry']})

# collections.Counter counts hashable objects and supports set-like math.
# Much faster than a manual "if key in d: d[k] += 1 else: d[k] = 1" loop.
from collections import Counter
votes = ["alice", "bob", "alice", "carol", "bob", "alice"]
tally = Counter(votes)
tally.most_common(2)   # => [('alice', 3), ('bob', 2)]
tally["alice"]         # => 3
tally["nobody"]        # => 0  (no KeyError — missing keys default to 0)
