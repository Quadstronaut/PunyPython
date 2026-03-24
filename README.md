# PunyPython
Possessing prodigious potential for producing pragmatic and proficient Python programs.

---

## About

PunyPython is a **Python-only** educational reference repository. Every file is a
runnable, heavily-commented script you can read, copy, paste, and experiment with.

The `LearnXinY/` section is a structured transcription of the canonical
[Learn X in Y Minutes — Python](https://learnxinyminutes.com/python/) guide
(© its contributors, Creative Commons Attribution-ShareAlike 3.0 Unported).
Each topic is expanded with up to two additional original examples per concept,
co-authored with [Claude](https://claude.ai) (Anthropic), also released under CC BY-SA 3.0.

All other folders contain algorithm implementations that demonstrate multiple
approaches to common problems.

---

## Repository Structure

```
PunyPython/
│
├── LearnXinY/                     ← Core language reference (learnxinyminutes transcription)
│   ├── Primitives/
│   │   ├── numbers.py             — integers, floats, arithmetic, operator precedence
│   │   ├── strings.py             — creation, slicing, methods, f-strings, translate
│   │   └── booleans_and_none.py   — bool ops, comparisons, short-circuit, truthiness
│   │
│   ├── Variables/
│   │   └── assignment.py          — basic assignment, unpacking, swap, augmented, annotations
│   │
│   ├── Collections/
│   │   ├── lists.py               — creation, indexing, slicing, mutation, methods
│   │   ├── tuples.py              — immutability, unpacking, namedtuple, memory
│   │   ├── dictionaries.py        — access, views, mutation, merge, Counter, defaultdict
│   │   └── sets.py                — operations, algebra, frozenset, deduplication
│   │
│   ├── ControlFlow/
│   │   ├── conditionals.py        — if/elif/else, ternary, match/case, guard clauses
│   │   ├── loops.py               — for, while, range, enumerate, zip, break/continue/else
│   │   ├── exceptions.py          — try/except/else/finally, raise, custom exceptions, with
│   │   └── comprehensions.py      — list, set, dict comprehensions; generator expressions
│   │
│   ├── Functions/
│   │   ├── basics.py              — def, return, scope, first-class, map/filter, lru_cache
│   │   ├── args_and_kwargs.py     — *args, **kwargs, keyword-only, positional-only, unpacking
│   │   ├── closures_and_lambdas.py — closures, nonlocal, lambda, operator module
│   │   ├── decorators.py          — @decorator, @wraps, arguments, stacking, class decorators
│   │   └── generators.py          — yield, generator expressions, yield from, send, pipelines
│   │
│   ├── Modules/
│   │   └── imports.py             — import, from/import, aliases, stdlib highlights, __name__
│   │
│   └── Classes/
│       ├── basics.py              — class, __init__, instance attrs, __str__/__repr__, dataclass
│       ├── properties_and_statics.py — @property, @classmethod, @staticmethod, cached_property
│       ├── inheritance.py         — single, multiple inheritance, super(), MRO, ABC, mixins
│       └── magic_methods.py       — arithmetic, comparison, container, context manager, __call__
│
├── Arrays/
│   ├── rotate/                    — 5 approaches to array rotation
│   ├── sum_of_array/              — 5 approaches to summing an array
│   └── largest_element/           — 6 approaches to finding the largest element
│
├── Lists/
│   └── swap_first_last/           — 4 approaches to swapping list ends
│
├── Textual/
│   ├── hello_world.py
│   ├── ascii_value_of_char.py
│   └── remove_nth_char.py
│
├── Mathmatical/
│   ├── Armstrong_number_check.py
│   ├── factorial/                 — 4 approaches
│   ├── maximum_of_2_numbers/      — 6 approaches
│   └── add_2_numbers/             — 6 approaches
│
└── venv_manager.py                — CLI tool for managing Python virtual environments
```

---

## How to Use

Each file in `LearnXinY/` is self-contained. Open any file and run it, or just read it —
all examples are written as expressions and print statements you can follow top to bottom.

```bash
python LearnXinY/Primitives/numbers.py
python LearnXinY/Collections/lists.py
python LearnXinY/Classes/inheritance.py
```

For the algorithm files, compare the approaches side by side to see the trade-offs
between readability, performance, and Python idiom.

---

## Commenting Philosophy

- **Rudimentary topics** (Primitives, Variables): comments label *what* each line does.
- **Intermediate topics** (Collections, ControlFlow): comments explain *why* a pattern is
  used or what pitfall it avoids (e.g. mutable default arguments, falsy-value traps).
- **Advanced topics** (Functions, Classes): comments focus on *when* to reach for a
  technique and what its trade-offs are (e.g. when generators beat list comprehensions,
  when `__slots__` saves memory, how MRO cooperates in multiple inheritance).

---

## Attribution & License

- Core examples transcribed from **[Learn X in Y Minutes — Python](https://learnxinyminutes.com/python/)**,
  © its contributors (Louie Dinh, Steven Basart, Andre Polykanine, and others).
  Licensed under [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/).

- Original supplemental examples (marked *co-authored with Claude* in each file)
  © quadstronaut & Claude (Anthropic), also released under CC BY-SA 3.0.

- Algorithm files in `Arrays/`, `Lists/`, `Textual/`, and `Mathmatical/` are original
  implementations by the repository contributors, released under CC BY-SA 3.0.

This repository will always remain Creative Commons. No proprietary content will be added.

---

## Contributing

This is a Python-only repository for educational purposes. Contributions that add new
Python examples, fix errors, or improve comments are welcome. Please keep the same
commenting style and CC BY-SA 3.0 license header in new files.
