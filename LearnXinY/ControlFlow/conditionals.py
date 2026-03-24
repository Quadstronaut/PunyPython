# conditionals.py
# if / elif / else and the ternary (inline conditional) expression.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Basic if / elif / else ---
some_var = 5

if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:            # elif = else if; can have as many as needed
    print("some_var is smaller than 10.")
else:                          # optional catch-all
    print("some_var is indeed 10.")

# --- Truthiness in conditions ---
# Python evaluates the condition with bool(); no explicit "== True" needed.
name = "Alice"
if name:            # truthy: non-empty string
    print(f"Hello, {name}")

items = []
if not items:       # falsy: empty list
    print("Nothing in the list")

# --- Ternary (inline conditional) expression ---
# value_if_true  if  condition  else  value_if_false
result = "even" if 4 % 2 == 0 else "odd"    # => "even"
"yay!" if 0 > 1 else "nay!"                  # => "nay!"

# Can be nested (keep it readable — one level max is a good rule of thumb)
n = 0
label = "positive" if n > 0 else ("negative" if n < 0 else "zero")

# --- match / case (Python 3.10+) ---
# Structural pattern matching — more powerful than a chain of elif.
# Especially useful when branching on type or shape of data.
command = "quit"

match command:
    case "quit":
        print("Quitting.")
    case "help":
        print("Showing help.")
    case _:              # _ is the wildcard / default case
        print(f"Unknown command: {command}")

# Pattern matching also works on data structures:
point = (1, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Somewhere at ({x}, {y})")


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# Guard clause pattern: handle edge cases early and return, keeping the
# "happy path" at the lowest indentation level. Avoids deeply nested ifs.
def process_order(order):
    if order is None:
        return "No order provided"
    if not order.get("items"):
        return "Order has no items"
    if order.get("total", 0) <= 0:
        return "Invalid total"
    # happy path — no nesting needed
    return f"Processing {len(order['items'])} items"

# dict.get() as a lightweight dispatch table replaces repetitive if/elif
# chains when mapping a key to a fixed value or callable.
status_messages = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
}
code = 404
message = status_messages.get(code, "Unknown status")   # => "Not Found"
