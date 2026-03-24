# args_and_kwargs.py
# *args, **kwargs, positional-only, keyword-only, and argument unpacking.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- *args — variable positional arguments ---
# Collects any extra positional args into a tuple named 'args'.
def varargs(*args):
    return args

varargs(1, 2, 3)    # => (1, 2, 3)
varargs("a", "b")   # => ('a', 'b')
varargs()           # => ()

# --- **kwargs — variable keyword arguments ---
# Collects any extra keyword args into a dict named 'kwargs'.
def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness")   # => {'big': 'foot', 'loch': 'ness'}
keyword_args()                          # => {}

# --- Combining both ---
def all_the_args(*args, **kwargs):
    print(f"args:   {args}")
    print(f"kwargs: {kwargs}")

all_the_args(1, 2, a=3, b=4)
# args:   (1, 2)
# kwargs: {'a': 3, 'b': 4}

# Ordering rule: positional, *args, keyword-only, **kwargs
def ordered(pos1, pos2, *args, kw_only, **kwargs):
    pass

# --- Argument unpacking at call sites ---
# * unpacks an iterable into positional arguments
# ** unpacks a dict into keyword arguments
nums = (1, 2, 3, 4)
opts = {"sep": "-", "end": "\n"}

print(*nums)           # same as print(1, 2, 3, 4)
print(*nums, **opts)   # same as print(1, 2, 3, 4, sep="-", end="\n")

def add(x, y):
    return x + y

pair = (3, 7)
add(*pair)             # => 10

params = {"x": 3, "y": 7}
add(**params)          # => 10

# --- Keyword-only parameters (after *) ---
# Must be supplied by name at the call site; cannot be passed positionally.
def create_tag(text, *, tag="p", cls=""):
    cls_attr = f' class="{cls}"' if cls else ""
    return f"<{tag}{cls_attr}>{text}</{tag}>"

create_tag("Hello")                          # => "<p>Hello</p>"
create_tag("Hello", tag="h1")               # => "<h1>Hello</h1>"
create_tag("Hello", tag="span", cls="bold") # => '<span class="bold">Hello</span>'
# create_tag("Hello", "h1")                 # => TypeError: unexpected positional arg

# --- Positional-only parameters (before /) — Python 3.8+ ---
# Must be supplied positionally; cannot be passed as keyword arguments.
def magnitude(x, y, /):
    return (x**2 + y**2) ** 0.5

magnitude(3, 4)        # => 5.0
# magnitude(x=3, y=4) # => TypeError


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# **kwargs lets you build flexible wrapper functions that forward arguments
# to an inner call transparently — common in decorators and adapter layers.
def log_call(func, *args, **kwargs):
    print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
    result = func(*args, **kwargs)
    print(f"  => {result}")
    return result

log_call(add, 3, 7)                    # positional
log_call(create_tag, "Hi", tag="h2")   # mixed

# Enforcing keyword-only for clarity in public APIs — if a function has
# more than two or three boolean flags, positional becomes ambiguous.
# Requiring keyword arguments makes call sites self-documenting.
def export(data, *, format="csv", include_header=True, compress=False):
    pass

export(data=[], format="json", compress=True)   # readable at the call site
