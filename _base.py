# Todo
'''
Basic book:
https://penseallen.github.io/PensePython2e/
GitHub: https://github.com/PenseAllen/PensePython2e

Advanced book:
https://pythonfluente.com/2/
English edition: https://www.fluentpython.com/
Examples: https://github.com/fluentpython/example-code-2e

Docs:
https://docs.python.org/pt-br/3.13/tutorial/
Bitwise operators: http://wiki.python.org/moin/BitwiseOperators

MySql
https://www.youtube.com/playlist?list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-

PostgreSQL

Unit test - TestCase / Mock / Stubs
Multi thread



Later:

- cx_freeze (transforma um código python em executável): https://www.lfd.uci.edu/~gohlke/pythonlibs/

Aulas Python - 086 - Iteração VII: Próprios Objetos Iteráveis
https://www.youtube.com/watch?v=mBebI97CMLw&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=87

Aulas Python - 114 - Ferramentas de Sistema X: Módulo subprocess
https://www.youtube.com/watch?v=jgmIUa2_wSY&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=115

Aulas Python - 115 - Ferramentas de Sistema XI: Módulo argparse
https://www.youtube.com/watch?v=HBwMGVBLw_0&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=116

Readmore: https://docs.python.org/pt-br/3/tutorial/index.html
'''



# Use the code below to run the program for production.
# It will ignore the assertions, which are used for debugging purposes.
# It will also remove the docstrings, which are used for documentation purposes, to reduce the .pyc file size.
# python -O <program_name>.py (optimize mode)

# Use the code below to create a virtual environment.
# python -m venv .venv

# Run the server with the parameter below (Django example).
# python manage.py runserver
# python -O manage.py runserver # With optimizations (ignores assertions)



# PDB (debugger)

# Aulas Python - 073 - Debugando programas usando o pdb
# https://www.youtube.com/watch?v=XeEYs0KYzGE&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=74



# region Title of Folding Region
# ... add your code here ...
# endregion



# pprint

# For long values to be printed, use pprint instead of print.
'''
from pprint import pprint

d    = { 'cat': 'gato', 'dog': 'cachorro', False: 0, True: 1,  }
data = {'a': d, 'b': d, 'c': d, 'd': d}

print(data)
# {'a': {'cat': 'gato', 'dog': 'cachorro', False: 0, True: 1}, 'b': {'cat': 'gato', 'dog': 'cachorro', False: 0, True: 1}, 'c': {'cat': 'gato', 'dog': 'cachorro', False: 0, True: 1}, 'd': {'cat'
: 'gato', 'dog': 'cachorro', False: 0, True: 1}}

pprint(data)
# {'a': {False: 0, True: 1, 'cat': 'gato', 'dog': 'cachorro'},
#  'b': {False: 0, True: 1, 'cat': 'gato', 'dog': 'cachorro'},
#  'c': {False: 0, True: 1, 'cat': 'gato', 'dog': 'cachorro'},
#  'd': {False: 0, True: 1, 'cat': 'gato', 'dog': 'cachorro'}}
'''



# Value

# Right-click on file > Open in Integrated Terminal > Type "py .\test.py" > Enter
# You can use `python.exe`, `python` or `py` on terminal.
# You can open the terminal with the shortcut `Ctrl+"`.

'''
print(.7) # 0.7
print(1000000) # 1000000
print(1_000_000) # 1000000

print(5 and 7) # 7 (5 is truthy, so returns the second value)
print(False and 7 or 10) # 10 (False is falsy, so returns the third value)
print(None and 7 or 10) # 10 (None is falsy, so returns the third value)
print(False and 7) # False (False is falsy, so returns itself, since there is no third value)
print(None and 7) # None (None is falsy, so returns itself, since there is no third value)
print(0 and 7) # 0 (0 is falsy in Python!)

print("Hello, world.")

# string format
foo = 7
print(f"foo = {foo}")

# float division
print(5 / 2) # 2.5
# integer division (ignores value after `.`)
print(5 // 2) # 2 # Same as math.floor(5 / 2)
# same as above
import math
print(math.floor(5 / 2))
'''
'''
print(1 < 3 < 5) # True
print(1 < 3 < 2) # False
'''
'''
x = 7
print(x)
del x
# print(x) # NameError: name 'x' is not defined
'''
'''
# print(7) print(8) # Statements must be separated by newlines or semicolons
print(7); print(8) # 7 8
'''

# Comparing variables (by reference vs by value)
'''
x = [1, 2, 3]
y = [1, 2, 3]
z = x
a = 'banana'
b = 'banana'

print(x is y) # False # Even if the lists have the same content, it creates two separate list objects in memory, so `x` and `y` point (reference) to different objects
print(x is z) # True # `x` and `z` point (reference) to the same object

# Avoid using `is` when comparing strings!
print(a is b) # True # Small strings with the same value are stored in the same memory location (string interning), so `a` and `b` point (reference) to the exact same object; this may be `False` if the strings are too long or dynamic
print(a == b) # True # Comparing by value (safe comparation) - Checks if the values are the same, not the memory location (reference); since both strings contain 'banana', the result is True

# In short, use `is` to compare by reference and `==` to compare by value
'''



# Ternary conditional operator

'''
x = 7
print(10 if x < 10 else 20) # 10
print(10 if x > 10 else 20) # 20
y = 10 if x > 10 else 20
print(y) # 20

def factorial(n):
  return 1 if n == 0 else n * factorial(n-1)
'''



# List comprehensions
# List comprehensions are a concise way to create lists in Python.

'''
# List comprehensions are typically faster than their equivalent "for" loops, sometimes much faster.
# But they are harder to debug because you can't have print statements inside the loop.
# Use them only if the calculation is simple enough that you can get it right the first time.

def capitalize_all(t):
  res = []
  for s in t:
    res.append(s.capitalize())
  return res

def capitalize_all(t):
  return [s.capitalize() for s in t]

def only_upper(t):
  res = []
  for s in t:
    if s.isupper():
      res.append(s)
  return res

def only_upper(t):
  return [s for s in t if s.isupper()]
'''



# Generator expressions
# Generator expressions are like list comprehensions, but they return an iterator instead of a list.
# On the contrary to list comprehensions, they are not calculated all at once, but only when you iterate over them.
# A generator cannot be reset. To "go back to the beginning", you need to recreate the generator.
# Generator expressions are often used with functions such as sum(...), max(...) and min(...).

'''
gen = (x**2 for x in range(5))
print(gen) # <generator object <genexpr> at 0x000001E70D67B440>
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(next(gen)) # 16
# print(next(gen)) # StopIteration: no more items in the generator

for val in (x**2 for x in range(5)):
  print(val) # 0; 1; 4; 9; 16
'''



# any and all
# The `any()` function returns True if at least one element of the iterable is True, otherwise it returns False.
# The `all()` function returns True if all elements of the iterable are True, otherwise it returns False.

'''
any([False, False, True]) # True

any(letter == 't' for letter in 'monty') # True
# This example is not very useful because it does the same thing as the in operator:
't' in 'monty'

# Check if a word has no letters from a banned list
def avoids(word, forbidden):
  for letter in word:
    if letter in forbidden:
      return False
  return True
def avoids(word, forbidden):
  return not any(letter in forbidden for letter in word) # Here, `not any` ensures that no letter in the word is on the banned list
def avoids(word, forbidden):
  return all(letter not in forbidden for letter in word) # Here, `all` ensures that all letters in the word are not on the banned list
'''



# Input

'''
name = input('Type your name: ')
print(f'Hello, {name}')
'''
'''
x = y = z = 7
print(x, y, z)
'''



# Type

'''
# Checks if `n` is an instance of `int` or of any subclass that inherits from `int`
# isinstance(n, int)

# Checks if the type of `n` is exactly `int`, ignoring the inheritance hierarchy
# type(n) == int

a = 7
b = int(7)
c = 7.0
d = float(7)
e = '7'
f = (1, 2, 3)
g = (7,500) -- tuple in which g[0] is 7 and g[1] is 500
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g))

print(isinstance(a, int)) # True
print(isinstance(a, float)) # False
print(isinstance(a, bool)) # False
'''
'''
# print('Number: ' + 7) # TypeError: can only concatenate str (not "int") to str
print('Number: ' + str(7)) # Solution
'''
'''
from functools import singledispatch

@singledispatch
def sum(a, b):
  raise NotImplementedError("Tipo não suportado")

@sum.register
def _(a: int, b: int):
  return a + b

@sum.register
def _(a: float, b: float):
  return a + b

print(sum(2, 3))     # 5  -> int
print(sum(2.5, 3.5)) # 6.0 -> float
'''



# Random

'''
import random

print(random.random()) # Number between 0 and 1, including 0 but not 1
print(random.randint(3,7)) # Numbers between 3 to 7
print(random.randrange(3,7)) # Numbers between 3 to 6
print(random.randrange(3,9,2)) # Numbers between 3 to 6, only odd numbers (3, 5 and 7)
print(random.choice(['a', 'b', 'c', 'd'])) # Randomly chooses one of the values
'''



# Enum

'''
flags = ['red', 'blue', 'green']

print(list(enumerate(flags))) # [(0, 'red'), (1, 'blue'), (2, 'green')]
print(tuple(enumerate(flags))) # ((0, 'red'), (1, 'blue'), (2, 'green'))
flags_dict = dict(enumerate(flags))
print(flags_dict) # {0: 'red', 1: 'blue', 2: 'green'}
print({v: k for k, v in flags_dict.items()}) # {'red': 0, 'blue': 1, 'green': 2}
'''



# Bit

'''
# Binary
print(bin(7)) # 0b111
print(0b111) # 7
print(int('0b111', 2)) # 7

# Octal
print(oct(7007)) # 0o15537
print(0o15537) # 7007
print(int('0o15537', 8)) # 7007

# Hex
print(hex(7007)) # 0x1b5f
print(0x1b5f) # 7007
print(int('0x1b5f', 16)) # 7007

# Bitwise

print(bin(0b010 << 1)) # 0b100
print(bin(0b010 >> 1)) # 0b1
print(bin(0b00100010 << 1)) # 0b1000100
print(bin(0b00100010 >> 1)) # 0b10001
print(16 << 1) # 32
print(16 << 2) # 64
print(16 << 3) # 128
print(bin(0b1010 & 0b1100)) # 0b1000 (only if both are 1)
print(bin(0b1010 | 0b0100)) # 0b1110 (if any are 1)
print(bin(0b1010 ^ 0b0010)) # 0b1000 (if they are different - 1 and the other 0 or vice versa)
'''



# Time

'''
import time
print(time.time())
'''



# Main file execution

'''
def main():
  print('Main file')
if __name__ == '__main__': # Main file
  main()
'''
