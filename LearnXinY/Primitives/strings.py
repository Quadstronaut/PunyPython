# strings.py
# String creation, indexing, slicing, methods, and formatting.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Creation ---
"This is a string"
'This is also a string'   # single or double quotes — no difference in Python

# Concatenation
"Hello " + "world!"          # => "Hello world!"
"Hello " "world!"            # => "Hello world!" (adjacent literals auto-join)

# Repetition
"ha" * 3                     # => "hahaha"

# --- Indexing and slicing ---
s = "Hello"
s[0]      # => 'H'  (zero-indexed)
s[-1]     # => 'o'  (negative index counts from the end)
s[1:3]    # => 'el' (start inclusive, end exclusive)
s[:3]     # => 'Hel'
s[2:]     # => 'llo'
s[::-1]   # => 'olleH' (reverse via step=-1)

# Strings are immutable — you cannot assign to an index
# s[0] = 'J'  # => TypeError

# --- Length ---
len("This is a string")  # => 16

# --- Common methods ---
"hello".upper()           # => "HELLO"
"HELLO".lower()           # => "hello"
"  hello  ".strip()       # => "hello"  (removes surrounding whitespace)
"hello world".split()     # => ['hello', 'world']  (splits on whitespace)
"a,b,c".split(",")        # => ['a', 'b', 'c']
",".join(["a", "b", "c"]) # => "a,b,c"  (inverse of split)
"hello".replace("l", "r") # => "herro"
"hello".startswith("he")  # => True
"hello".endswith("lo")    # => True
"ell" in "hello"          # => True  (substring membership check)

# --- Formatting ---
name = "Alice"
age = 30

# f-strings (Python 3.6+) — fastest and most readable
f"My name is {name} and I am {age} years old."

# Expressions work inside f-string braces
f"{name.upper()} has {len(name)} characters."
f"2 + 2 = {2 + 2}"

# .format() — compatible with older Python 3
"My name is {} and I am {} years old.".format(name, age)
"My name is {n} and I am {a} years old.".format(n=name, a=age)

# %-formatting (legacy, avoid in new code)
"My name is %s and I am %d years old." % (name, age)

# Multi-line strings use triple quotes
multiline = """Line one
Line two
Line three"""


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# f-string debug shorthand: {var=} prints both the name and value —
# saves time vs. writing f"name={name}" manually.
user = "bob"
score = 99
print(f"{user=}, {score=}")  # => user='bob', score=99

# str.translate() + str.maketrans() for bulk character substitution —
# faster than chained .replace() calls when remapping many characters.
rot13 = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
)
"Hello, World!".translate(rot13)  # => "Uryyb, Jbeyq!"
