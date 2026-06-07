# remove_nth_char.py
# Remove the character at index n from a string (0-based).
# Strings are immutable in Python — slicing produces a new string.

def remove_nth_char(s, n):
    """Return s with the character at index n removed."""
    if n < 0 or n >= len(s):
        raise IndexError(f"Index {n} is out of range for string of length {len(s)}")
    return s[:n] + s[n + 1:]


# Examples
print(remove_nth_char("hello world", 4))   # => "hell world"  (removes 'o')
print(remove_nth_char("Python", 0))        # => "ython"       (removes first char)
print(remove_nth_char("Python", 5))        # => "Pytho"       (removes last char)
