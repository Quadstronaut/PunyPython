# closures_and_lambdas.py
# Nested functions, closures, the nonlocal keyword, and lambda expressions.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Closures ---
# A closure is an inner function that "closes over" variables from its
# enclosing scope. Those variables persist even after the outer function
# has returned — the inner function carries its own copy of the reference.

def create_adder(x):
    def adder(y):
        return x + y     # 'x' is free variable from the enclosing scope
    return adder          # returns the function itself, not its result

add_10 = create_adder(10)
add_10(3)    # => 13
add_10(7)    # => 17

add_5 = create_adder(5)
add_5(3)     # => 8

# Each call to create_adder produces a separate closure with its own x.
add_10.__closure__[0].cell_contents   # => 10

# --- nonlocal — mutate a variable in the enclosing (non-global) scope ---
def make_counter():
    count = 0
    def increment():
        nonlocal count   # without this, 'count = count + 1' raises UnboundLocalError
        count += 1
        return count
    return increment

counter = make_counter()
counter()   # => 1
counter()   # => 2
counter()   # => 3

# --- Lambda — anonymous, single-expression functions ---
# lambda args: expression
# Useful for short callbacks; prefer named functions for anything complex.
square = lambda x: x ** 2
square(5)   # => 25

add = lambda x, y: x + y
add(3, 4)   # => 7

# Common use: as a sort key
pairs = [(1, "b"), (3, "a"), (2, "c")]
sorted(pairs, key=lambda p: p[1])   # => [(3, 'a'), (1, 'b'), (2, 'c')]
sorted(pairs, key=lambda p: p[0])   # => [(1, 'b'), (2, 'c'), (3, 'a')]

# Immediately invoked
(lambda x: x > 2)(3)                      # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)      # => 5

# --- map() and filter() with lambdas ---
list(map(lambda x: x * 2, [1, 2, 3]))             # => [2, 4, 6]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))    # => [6, 7]

# List comprehensions are usually more readable than map/filter + lambda
[x * 2 for x in [1, 2, 3]]                 # equivalent to map above
[x for x in [3, 4, 5, 6, 7] if x > 5]      # equivalent to filter above


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Factory functions using closures let you parameterise behaviour without
# classes — a lightweight alternative when state is minimal.
def make_validator(min_val, max_val):
    def validate(n):
        if not (min_val <= n <= max_val):
            raise ValueError(f"{n} is outside [{min_val}, {max_val}]")
        return n
    return validate

check_percentage = make_validator(0, 100)
check_percentage(42)    # => 42
# check_percentage(150) # => ValueError

# operator module functions are drop-in lambda replacements for simple
# attribute / item access — faster and more readable than a lambda.
from operator import attrgetter, itemgetter
from collections import namedtuple

records = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted(records, key=itemgetter("age"))    # sort by 'age' key

Person = namedtuple("Person", ["name", "age"])
people = [Person("Alice", 30), Person("Bob", 25)]
sorted(people, key=attrgetter("age"))     # sort by .age attribute
