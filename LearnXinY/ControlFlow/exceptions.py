# exceptions.py
# try / except / else / finally, raising exceptions, and context managers.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Basic try / except ---
try:
    raise IndexError("This is an index error")
except IndexError as e:
    print(f"Caught: {e}")   # Caught: This is an index error

# --- Catching multiple exception types ---
try:
    int("not a number")
except (TypeError, ValueError) as e:
    print(f"Conversion failed: {e}")

# --- try / except / else / finally ---
# else  : runs only if NO exception was raised in try
# finally: ALWAYS runs, exception or not — use for cleanup
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result is {result}")    # runs; no exception occurred
finally:
    print("This always runs")       # cleanup: close files, release locks, etc.

# --- Raising exceptions ---
# raise reraises the current exception inside an except block
# raise ExceptionType("message") raises a new one
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    set_age(-1)
except ValueError as e:
    print(e)

# --- Exception hierarchy (common built-ins) ---
# BaseException
#   SystemExit, KeyboardInterrupt, GeneratorExit
#   Exception
#     ArithmeticError: ZeroDivisionError, OverflowError
#     LookupError:     IndexError, KeyError
#     TypeError
#     ValueError
#     OSError:         FileNotFoundError, PermissionError, TimeoutError
#     RuntimeError:    RecursionError
# Catch the most specific type you can; avoid bare except: or except Exception:

# --- Context managers and the with statement ---
# The with statement calls __enter__ on entry and __exit__ on exit
# (even if an exception is raised), ensuring deterministic cleanup.
# Most common use: file I/O — guarantees the file is closed.
with open("myfile.txt", "w") as f:
    f.write("hello")
# f is closed here automatically, no need for f.close()

# --- Custom exceptions ---
# Subclass Exception (not BaseException) so that bare except Exception: catches them.
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Tried to withdraw {amount} but balance is {balance}")

try:
    raise InsufficientFundsError(100, 50)
except InsufficientFundsError as e:
    print(e)
    print(f"Short by {e.amount - e.balance}")


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# contextlib.suppress() is a concise way to swallow a specific exception
# when you genuinely don't care about it — cleaner than a try/except/pass.
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("file_that_may_not_exist.tmp")
# No error even if the file was never there

# Exception chaining with 'raise ... from ...' preserves the original cause
# in the __cause__ attribute, giving full context in tracebacks.
def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file not found: {path}") from e
# The traceback will show both the RuntimeError and the original FileNotFoundError.
