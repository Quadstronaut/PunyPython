# loops.py
# for loops, while loops, range, enumerate, zip, break, continue, else.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- for loop (iterates over any iterable) ---
for animal in ["dog", "cat", "mouse"]:
    print(f"{animal} is a mammal")

# --- range() ---
for i in range(4):          # 0, 1, 2, 3  (stop is exclusive)
    print(i)

for i in range(4, 8):       # 4, 5, 6, 7
    print(i)

for i in range(4, 10, 2):   # 4, 6, 8  (start, stop, step)
    print(i)

for i in range(10, 0, -1):  # 10, 9, ... 1  (counting down)
    print(i)

# --- enumerate() — gives (index, value) pairs ---
# Use this instead of manually tracking a counter variable.
for i, value in enumerate(["dog", "cat", "mouse"]):
    print(i, value)    # 0 dog, 1 cat, 2 mouse

for i, ch in enumerate("abc", start=1):  # start index at 1
    print(i, ch)       # 1 a, 2 b, 3 c

# --- zip() — iterate over multiple iterables in parallel ---
# Stops at the shortest iterable.
names  = ["Alice", "Bob", "Carol"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# --- while loop ---
x = 0
while x < 4:
    print(x)
    x += 1

# --- break and continue ---
for i in range(10):
    if i == 3:
        continue    # skip the rest of this iteration
    if i == 6:
        break       # exit the loop entirely
    print(i)        # prints 0, 1, 2, 4, 5

# --- for / while … else ---
# The else block runs ONLY if the loop completed without hitting a break.
# Useful for "search and report not found" patterns.
for i in range(5):
    if i == 9:
        break
else:
    print("9 was not found")   # this prints

for i in range(5):
    if i == 3:
        break
else:
    print("3 was not found")   # this does NOT print (break was hit)

# --- Iterators under the hood ---
# for loops call iter() on the iterable, then next() until StopIteration.
iterable = [1, 2, 3]
it = iter(iterable)
next(it)   # => 1
next(it)   # => 2
next(it)   # => 3
# next(it) # => StopIteration


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# itertools.chain() flattens multiple iterables into one loop without
# building an intermediate list — memory-friendly for large datasets.
import itertools
first_half  = [1, 2, 3]
second_half = [4, 5, 6]
for n in itertools.chain(first_half, second_half):
    print(n)   # 1 2 3 4 5 6

# Iterate over a copy when you need to mutate a list inside the loop.
# Mutating the list you're iterating over directly leads to skipped elements.
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers[:]:       # numbers[:] is a shallow copy
    if n % 2 == 0:
        numbers.remove(n)  # safe to remove from original while looping copy
# numbers => [1, 3, 5]
