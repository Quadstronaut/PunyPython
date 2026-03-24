# numbers.py
# Integers, floats, and arithmetic operators in Python.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Integers ---
3        # => 3
1 + 1    # => 2
8 - 1    # => 7
10 * 2   # => 20

# Division always returns a float in Python 3
35 / 5   # => 7.0
5 / 3    # => 1.6666...

# Floor division (integer division — truncates toward negative infinity)
5 // 3    # => 1
-5 // 3   # => -2  (not -1; floors toward -inf, not toward 0)
5.0 // 3  # => 1.0 (stays float when either operand is float)

# Modulo
7 % 3     # => 1
-7 % 3    # => 2   (result takes the sign of the divisor in Python)

# Exponentiation
2 ** 8    # => 256

# Operator precedence follows standard math rules; use parens to be explicit
1 + 3 * 2    # => 7   (multiplication first)
(1 + 3) * 2  # => 8   (parens override)

# --- Floats ---
3.14
1.0 + 0.1   # => 1.1 (floating-point rounding can surprise you — see below)
0.1 + 0.2   # => 0.30000000000000004 (IEEE 754 representation artifact)

# Use round() or the decimal module when precision matters
round(0.1 + 0.2, 2)  # => 0.3

# --- Built-in numeric functions ---
abs(-5)        # => 5
int(4.9)       # => 4   (truncates toward zero, does NOT round)
float(4)       # => 4.0
divmod(7, 3)   # => (2, 1)  — (quotient, remainder) in one call
pow(2, 10)     # => 1024    — same as 2 ** 10


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Walrus operator (:=) assigns and evaluates in the same expression.
# Useful for avoiding a redundant calculation before a conditional.
import math
if (n := math.sqrt(144)) > 10:
    print(f"sqrt(144) = {n}")  # => sqrt(144) = 12.0

# Integer bit-length — handy when working with binary protocols or
# determining how many bits are needed to represent a value.
x = 255
x.bit_length()      # => 8   (255 needs 8 bits: 11111111)
(256).bit_length()  # => 9
