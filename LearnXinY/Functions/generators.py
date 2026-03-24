# generators.py
# Generator functions, yield, generator expressions, and send/throw.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- What is a generator? ---
# A generator is a function that uses 'yield' instead of 'return'.
# It produces values one at a time and pauses between each — it never
# builds the whole sequence in memory. This makes generators ideal for
# large or infinite sequences.

def double_numbers(iterable):
    for i in iterable:
        yield i * 2    # execution suspends here until the next value is requested

# Only the current doubled value exists in memory at any time.
for n in double_numbers(range(1, 10)):
    print(n)   # 2 4 6 8 10 12 14 16 18

# --- Contrast with a list-based approach ---
def double_numbers_list(iterable):
    return [i * 2 for i in iterable]   # entire list in memory at once

# For range(1, 900_000_000) the list approach would exhaust RAM;
# the generator processes one element per loop iteration.
for n in double_numbers(range(1, 900_000_000)):
    if n > 30:
        break    # generator discarded; remaining values never computed

# --- Generator expressions ---
# Like list comprehensions but wrapped in () — lazy by default.
gen = (-x for x in [1, 2, 3, 4, 5])
next(gen)   # => -1
next(gen)   # => -2

list((-x for x in [1, 2, 3, 4, 5]))   # => [-1, -2, -3, -4, -5]

# Pass a generator expression directly to aggregate functions
sum(x**2 for x in range(10))                        # => 285
max(len(word) for word in ["hi", "hello", "hey"])   # => 5

# --- Infinite generators ---
def count_up(start=0, step=1):
    n = start
    while True:
        yield n
        n += step

counter = count_up(10, 2)
next(counter)   # => 10
next(counter)   # => 12
next(counter)   # => 14

# --- yield from — delegate to a sub-generator ---
def chain(*iterables):
    for it in iterables:
        yield from it    # flattens; equivalent to: for item in it: yield item

list(chain([1, 2], [3, 4], [5]))   # => [1, 2, 3, 4, 5]

# --- Two-way communication with .send() ---
# yield is also an expression — .send(value) resumes and injects a value.
def accumulator():
    total = 0
    while True:
        value = yield total   # yield current total; receive next addend
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)       # prime the generator (advance to first yield) => 0
acc.send(10)    # => 10
acc.send(5)     # => 15
acc.send(3)     # => 18


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Pipelined generators — chain transformations without intermediate lists.
# Each stage is lazy; memory usage is O(1) regardless of input size.
def read_lines(path):
    """Yield lines from a file one at a time."""
    with open(path) as f:
        yield from f

def grep(pattern, lines):
    """Yield only lines containing pattern."""
    for line in lines:
        if pattern in line:
            yield line

def strip_newlines(lines):
    """Yield lines with trailing whitespace removed."""
    for line in lines:
        yield line.rstrip()

# Usage (compose like Unix pipes):
# results = strip_newlines(grep("ERROR", read_lines("/var/log/app.log")))
# for line in results:
#     print(line)

# itertools.islice lets you take the first N items from any (even infinite)
# generator without exhausting it — replaces a manual counter + break.
import itertools

evens = (x for x in count_up(0, 2))
first_ten_evens = list(itertools.islice(evens, 10))
# => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
