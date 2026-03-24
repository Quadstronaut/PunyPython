# basics.py
# Defining functions, parameters, return values, scope, and first-class use.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Basic definition ---
def add(x, y):
    print(f"x is {x} and y is {y}")
    return x + y

add(5, 6)           # => 11  (positional arguments)
add(y=6, x=5)       # => 11  (keyword arguments — order doesn't matter)

# --- Default parameter values ---
# Default values are evaluated ONCE at function definition time, not per call.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")                  # => "Hello, Alice!"
greet("Bob", "Hi")              # => "Hi, Bob!"
greet("Carol", greeting="Hey")  # keyword override

# --- Returning multiple values ---
# Python returns a tuple; unpack it at the call site.
def min_and_max(lst):
    return min(lst), max(lst)

lo, hi = min_and_max([3, 1, 4, 1, 5, 9])   # lo=1, hi=9

# A function with no explicit return statement returns None.
def nothing():
    pass

nothing() is None   # => True

# --- Variable scope ---
# Python looks up names in: Local → Enclosing → Global → Built-in (LEGB)
x = 5   # global

def show_local():
    x = 10          # local x; shadows the global inside this function
    print(x)        # => 10

def modify_global():
    global x        # explicitly reference the global
    x = 99

show_local()        # prints 10; global x is still 5
modify_global()     # now global x is 99

# --- Functions are first-class objects ---
# They can be stored in variables, passed as arguments, and returned.
def square(n):
    return n ** 2

operation = square      # no call — just a reference
operation(4)            # => 16

def apply(func, value):
    return func(value)

apply(square, 5)        # => 25
apply(abs, -7)          # => 7  (built-ins work too)

# --- map() and filter() ---
# map()   : applies a function to every element; returns an iterator
# filter(): keeps elements for which the function returns True
list(map(square, [1, 2, 3, 4]))               # => [1, 4, 9, 16]
list(filter(lambda n: n % 2 == 0, range(10))) # => [0, 2, 4, 6, 8]


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# functools.lru_cache memoizes expensive pure functions automatically.
# The first call for a given argument is computed; subsequent calls are O(1).
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(50)   # => 12586269025  (instant; without cache this would be ~2^50 calls)

# functools.partial() creates a new callable with some arguments pre-filled —
# a lightweight alternative to writing a wrapper function.
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube   = partial(power, exponent=3)
square(5)   # => 25
cube(3)     # => 27
