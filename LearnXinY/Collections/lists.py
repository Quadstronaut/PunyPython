# lists.py
# List creation, indexing, slicing, mutation, and common methods.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Creation ---
empty = []
numbers = [1, 2, 3]
mixed = [1, "two", 3.0, True]  # lists can hold any mix of types

# --- Appending and removing ---
li = []
li.append(1)    # li => [1]
li.append(2)    # li => [1, 2]
li.append(4)    # li => [1, 2, 4]
li.append(3)    # li => [1, 2, 4, 3]
li.pop()        # removes and returns last element => 3; li => [1, 2, 4]
li.append(3)    # li => [1, 2, 4, 3]

li.remove(2)        # removes first occurrence of 2; li => [1, 4, 3]
li.insert(1, 2)     # insert 2 at index 1; li => [1, 2, 4, 3]
del li[2]           # delete element at index 2; li => [1, 2, 3]

# --- Indexing ---
li[0]    # => 1   (first element)
li[-1]   # => 3   (last element; negative indices count from the end)
# li[5]  # => IndexError: list index out of range

# --- Slicing  [start:stop:step] ---
# start is inclusive, stop is exclusive
li[1:3]    # => [2, 3]   (index 1 up to but not including 3)
li[2:]     # => [3]      (index 2 to end)
li[:2]     # => [1, 2]   (start to index 2 exclusive)
li[::2]    # => [1, 3]   (every other element)
li[::-1]   # => [3, 2, 1] (reverse; step=-1 walks backwards)

# Slices never raise IndexError — out-of-range bounds are clamped
li[0:100]  # => [1, 2, 3] (safe even though 100 > len)

# --- Shallow copy via slice ---
li2 = li[:]    # new list object; changes to li2 don't affect li
li2 is li      # => False

# --- Searching ---
li.index(2)   # => 1  (first index of value 2; raises ValueError if missing)
2 in li       # => True  (membership test; O(n) for lists)
9 in li       # => False

# --- Combining lists ---
other = [4, 5, 6]
li + other          # => [1, 2, 3, 4, 5, 6]  (new list; neither modified)
li.extend(other)    # mutates li in-place; li => [1, 2, 3, 4, 5, 6]

# --- Other useful operations ---
len(li)          # => 6
li.count(1)      # => 1  (number of times 1 appears)
li.sort()        # sort in-place; li => [1, 2, 3, 4, 5, 6]
li.reverse()     # reverse in-place
sorted(li)       # returns a NEW sorted list without mutating li
reversed(li)     # returns an iterator (wrap in list() to materialise)
min(li)          # => 1
max(li)          # => 6
sum(li)          # => 21

# --- Nested lists ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2]     # => 6  (row 1, column 2)


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# list.sort() vs sorted() — knowing which mutates matters.
# Use sorted() when you need to keep the original order intact.
original = [3, 1, 4, 1, 5]
ordered = sorted(original)    # original unchanged
original.sort()               # original is now sorted (destructive)

# zip() pairs elements from multiple lists — stops at the shortest.
# Unzip the same way: zip(*zipped).
names = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
paired = list(zip(names, scores))           # => [('Alice', 95), ('Bob', 87), ('Carol', 92)]
back_names, back_scores = zip(*paired)      # unzip back to separate tuples
