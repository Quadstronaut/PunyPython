# decorators.py
# Decorator syntax, preserving metadata with functools.wraps, and stacking.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

from functools import wraps

# --- What a decorator is ---
# A decorator is a callable that takes a function and returns a replacement
# function. The @syntax is just shorthand for:
#   func = decorator(func)

# --- A simple decorator ---
def beg(target_function):
    @wraps(target_function)       # copies __name__, __doc__, etc. from original
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return f"{msg} Please! I am poor :("
        return msg
    return wrapper

@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please

say()                  # => "Can you buy me a beer?"
say(say_please=True)   # => "Can you buy me a beer? Please! I am poor :("

# --- Why @wraps matters ---
# Without @wraps the wrapper's __name__ would be "wrapper" instead of "say",
# breaking introspection, logging, and tools that rely on function names.
say.__name__    # => "say"  (preserved by @wraps)

# --- Decorator with arguments ---
# Requires an extra layer of nesting: a factory that returns the decorator.
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # prints "Hello, Alice!" three times

# --- Stacking decorators ---
# Applied bottom-up: @uppercase is the outer wrapper, @exclaim is inner.
def exclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!"
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
@exclaim
def hello():
    return "hello"

hello()   # => "HELLO!"
# Equivalent to: uppercase(exclaim(hello))()

# --- Class-based decorator ---
# Use a class when the decorator needs to maintain state between calls.
class CountCalls:
    def __init__(self, func):
        wraps(func)(self)
        self.func  = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def add(a, b):
    return a + b

add(1, 2)   # Call #1 to add => 3
add(3, 4)   # Call #2 to add => 7


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Timing decorator — wraps any function and prints its execution time.
# A real-world pattern for quick profiling without a full profiler.
import time

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start   = time.perf_counter()
        result  = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timed
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)

# Retry decorator — re-attempts a flaky function up to n times before
# re-raising. Useful for network calls or transient I/O failures.
def retry(times=3, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == times:
                        raise
                    print(f"Attempt {attempt} failed: {e}. Retrying...")
        return wrapper
    return decorator

@retry(times=3, exceptions=(ConnectionError,))
def fetch_data(url):
    pass   # imagine a real HTTP call here
