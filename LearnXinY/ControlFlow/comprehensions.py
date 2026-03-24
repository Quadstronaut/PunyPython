# comprehensions.py
# List, dict, and set comprehensions, plus generator expressions.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- List comprehension ---
# [expression  for  item  in  iterable]
squares = [x**2 for x in range(6)]            # => [0, 1, 4, 9, 16, 25]

# With a filter condition
evens = [x for x in range(10) if x % 2 == 0]  # => [0, 2, 4, 6, 8]

# Equivalent for-loop (comprehension is shorter and typically faster)
evens_loop = []
for x in range(10):
    if x % 2 == 0:
        evens_loop.append(x)

# Calling a function on each element
def add_10(n):
    return n + 10

[add_10(i) for i in [1, 2, 3]]                # => [11, 12, 13]

# Nested comprehension — flattens a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]      # => [1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- Set comprehension ---
# {expression  for  item  in  iterable}
unique_chars = {c for c in "abracadabra" if c not in "aeiou"}  # => {'b','r','c','d'}

# --- Dict comprehension ---
# {key_expr: value_expr  for  item  in  iterable}
word_lengths = {word: len(word) for word in ["apple", "kiwi", "mango"]}
# => {'apple': 5, 'kiwi': 4, 'mango': 5}

# Invert a dict (assumes values are unique)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}  # => {1: 'a', 2: 'b', 3: 'c'}

# --- Generator expression ---
# (expression  for  item  in  iterable)
# Like a list comprehension but LAZY — produces values one at a time.
# Use when you only need to iterate once, or when the dataset is large.
gen = (x**2 for x in range(1_000_000))   # builds NO list in memory
next(gen)   # => 0
next(gen)   # => 1

# Passing a generator expression directly to a function (extra parens optional)
total = sum(x**2 for x in range(10))              # => 285
any_over_50 = any(x**2 > 50 for x in range(10))  # => True

# --- When to choose which form ---
# list comprehension  : need a list to index, pass to a function, etc.
# set comprehension   : need unique values and membership tests
# dict comprehension  : need key-value pairs
# generator expression: one-pass iteration, or memory is a concern


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Conditional expression inside the value slot — categorize in one pass
# without building two separate lists or writing a loop.
numbers = range(-5, 6)
labeled = [(n, "positive" if n > 0 else "negative" if n < 0 else "zero")
           for n in numbers]
# => [(-5, 'negative'), ..., (0, 'zero'), ..., (5, 'positive')]

# Chained .items() comprehension for deep key extraction — flattening a
# nested dict into a flat (outer, inner, value) list in a single expression.
nested = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
flat_pairs = [(outer, inner, val)
              for outer, sub in nested.items()
              for inner, val in sub.items()]
# => [('a', 'x', 1), ('a', 'y', 2), ('b', 'x', 3), ('b', 'y', 4)]
