# imports.py
# Importing modules, submodules, specific names, aliases, and packages.
# Source: https://learnxinyminutes.com/python/  (CC BY-SA 3.0)
# Organization inspired by learnxinyminutes.com

# --- Standard import ---
import math
math.sqrt(16)   # => 4.0
math.pi         # => 3.141592653589793

# You must qualify names with the module prefix (math.sqrt, not sqrt).

# --- Import specific names into the current namespace ---
from math import ceil, floor
ceil(3.7)    # => 4  (no 'math.' prefix needed)
floor(3.7)   # => 3

# --- Import everything from a module (wildcard) ---
# from math import *
# Pollutes the namespace and makes it unclear where names come from.
# Avoid in production code; sometimes useful in interactive sessions.

# --- Import with an alias ---
import math as m
m.sqrt(9)    # => 3.0  (shorter alias)

# Common community conventions:
# import numpy as np
# import pandas as pd

from datetime import datetime as dt
dt.now()

# --- Inspecting a module ---
dir(math)           # list all names in the module
help(math.sqrt)     # full docstring

# --- Standard library highlights ---
import os               # OS interface: file paths, env vars, processes
import sys              # interpreter internals: argv, path, exit
import re               # regular expressions
import json             # JSON encode/decode
import datetime         # dates and times
import collections      # deque, Counter, defaultdict, OrderedDict, namedtuple
import itertools        # combinatoric and infinite iterators
import functools        # higher-order functions: reduce, lru_cache, partial, wraps
import pathlib          # object-oriented filesystem paths
import typing           # type hints: List, Dict, Optional, Union, etc.
import abc              # abstract base classes
import dataclasses      # @dataclass decorator
import contextlib       # context manager utilities
import logging          # structured logging

# --- Third-party packages (installed via pip) ---
# import requests       # HTTP library
# import flask          # lightweight web framework
# import sqlalchemy     # SQL ORM and toolkit
# import pytest         # testing framework

# --- Relative imports (inside a package) ---
# from . import sibling_module          # import from same package
# from .. import parent_package_module  # import from parent package
# from .utils import helper_func        # import specific name from sibling

# --- __name__ guard ---
# Code under this block only runs when the file is executed directly,
# not when it's imported as a module. Standard entry-point convention.
if __name__ == "__main__":
    print(f"pi is approximately {math.pi:.4f}")


# -----------------------------------------------------------------------
# ORIGINAL EXAMPLES (co-authored with Claude)
# -----------------------------------------------------------------------

# importlib.import_module() lets you import by string name — useful when
# the module name is only known at runtime (plugin systems, config-driven loading).
import importlib
mod_name = "json"
json = importlib.import_module(mod_name)
json.dumps({"key": "value"})   # => '{"key": "value"}'

# sys.path controls where Python searches for modules.
# Append to it at runtime to load code from a non-standard location
# (e.g. a plugins directory alongside your app).
import sys
sys.path.append("/path/to/custom/plugins")
# import my_plugin  # now discoverable
