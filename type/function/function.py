# Function

# Function VS Method
# A function is not attached to any class
# A method is the same as function, but attached to a class

# Example
'''
def foo() -> None: # Return nothing
  pass # Do nothing (like a placeholder to do something later)

def foo2(x, y):
  if x < y:
    print('x is less than y')
  elif x > y:
    print('x is greater than y')
  else:
    print('x and y are equal')

def foo3(x):
  msg = 'x is a positive single-digit number.'

  if x > 0:
    if x < 10:
      print(msg)

  if 0 < x:
    if x < 10:
      print(msg)

  if 0 < x and x < 10:
    print(msg)

  if 0 < x < 10:
    print(msg)

def factorial (n):
  if not isinstance(n, int):
    print('Factorial is only defined for integers.')
    return None
  elif n < 0:
    print('Factorial is not defined for negative integers.')
    return None
  elif n == 0:
    return 1
  else:
    return n * factorial(n-1)

def factorial2(n):
  space = ' ' * (4 * n)
  print(space, 'factorial', n)
  if n == 0:
    print(space, 'returning 1')
    return 1
  else:
    recurse = factorial2(n-1)
    result = n * recurse
    print(space, 'returning', result)
    return result

  factorial(4) returns the following output:
                  factorial 4
              factorial 3
          factorial 2
      factorial 1
  factorial 0
  returning 1
      returning 1
          returning 2
              returning 6
                  returning 24

def is_reverse(word1, word2):
    length = len(word1)
    i      = 0
    j      = length - 1

    if length != len(word2):
        return False

    while i < length:
        # print(i, j) # 0 3; 1 2; 2 1; 3 0
        if word1[i] != word2[j]:
            return False

        i = i + 1
        j = j - 1

    return True

print(is_reverse('pots', 'stop')) # True
'''

'''
def foo_square(number: int = 2) -> int:
  #docstring
  #'#''Function description (use block comment here)'#''
  return number ** 2
print(foo_square(3)) # 9
print(foo_square()) # 4
'''

# Example of complex docstring (hover your mouse on foo_docstring())
# This is the docs of Scaffold.route.
def foo_docstring():
  """Decorate a view function to register it with the given URL
  rule and options. Calls :meth:`add_url_rule`, which has more
  details about the implementation.

  .. code-block:: python

      @app.route("/")
      def index():
          return "Hello, World!"

  See :ref:`url-route-registrations`.

  The endpoint name for the route defaults to the name of the view
  function if the ``endpoint`` parameter isn't passed.

  The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` and
  ``OPTIONS`` are added automatically.

  :param rule: The URL rule string.
  :param options: Extra options passed to the
      :class:`~werkzeug.routing.Rule` object.
  """
  pass

# Parameter

# Simple value parameters are passed by copy
'''
def foo(x):
  print(x)
  x += 1
  print(x)
value = 1
foo(value) # 1 2
print(value) # 1 (kept previous value)
'''

# Table and objects are passed by reference
'''
def foo(list):
  for i in range(len(list)):
    list[i] += 1
numbers = [2, 4, 7]
print(numbers) # [2, 4, 7]
foo(numbers)
print(numbers) # [3, 5, 8]
'''

# Callback

'''
def foo(x):
  print(x)
def call_another_func(callback, value):
  callback(value)
call_another_func(foo, 7) # 7
'''



# Scope

# Variables defined inside a function are local by default.

# Variables defined outside a function are global; or, if accessed inside a function using the `global` keyword, they are treated as global.

# Variables defined inside a function using the nonlocal keyword are nonlocal, which refers to the nearest enclosing function (`inner()` gets `x` (8) of `outer()` on the nonlocal scope example).
# This means they are not local to the inner function (`inner()` on the nonlocal scope example), nor global, but belong to the nearest enclosing function scope (`outer()` on the nonlocal scope example).

# Local scope
'''
# Reading local variable
def example1():
  verbose = True
  print(verbose) # True
example1()

# Modifying local variable (this is always allowed — no keyword needed)
def example2():
  been_called = False
  been_called = True # Reassigns the local variable
  print(been_called) # True
example2()

# Incrementing local variable
def example3():
  count = 0
  count += 1
  print(count) # 1
example3()

# Local variables referring to mutable values can be modified freely
def example4():
  known = {0: 0, 1: 1}
  known[2] = 1 # Modifies the local dictionary
  print(known) # {0: 0, 1: 1, 2: 1}
example4()

# Reassigning the local variable just changes its reference in the local scope
def example5():
  known = {0: 0, 1: 1}
  known = { } # Same as `known = dict()` # Reassignment
  print(known) # { }
example5()

# Practical example
def inner():
  x = 8
  print('a', x) # a 8
  x = 7
  print('b', x) # b 7
inner()
'''

# Global scope
'''
# Reading global variable
verbose = True
def example1():
  print(verbose) # True
example1()


# Wrong way of modifying global variable
been_called = False
def example2():
  been_called = True # This is a local variable, not the global variable
example2()
print(been_called) # False

# Right way of modifying global variable
been_called = False
def example3():
  global been_called # This is the global variable above
  been_called = True
example3()
print(been_called) # True


# Wrong way of modifying global variable
count = 0
def example4():
  count = count + 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
  # print(count) # Never executed, since the previous line raised an exception
example4()

# Right way of modifying global variable
count = 0
def example5():
  global count
  count += 1
  print(count) # 1
example5()


# If a global variable refers to a mutable value (list, deque, heap, dictionary, set, etc), you can change the value without declaring it `global`
known = { 0: 0, 1: 1 }
def example6():
  known[2] = 1 # Modifies the global variable, even without the `global` keyword
example6()
print(known) # {0: 0, 1: 1, 2: 1}

# If you want to reassign the variable, you need to declare it `global`, because the reference to the global variable is lost
known = { 0: 0, 1: 1 }
def example7():
  global known
  known = { } # Same as `known = dict()` # Reassignment
example7()
print(known) # { }


# Pratical example

x = 8
print('a', x) # a 8

def inner():
  global x # Gets the reference to the global variable `x`
  global y # Gets the reference to the global variable `y`

  print('c', x) # c 8
  x = 7
  print('d', x) # d 7

  print('e', y) # e 100
y = 100
print('b', x) # b 8
inner()
print('f', x) # f 7
'''

# Nonlocal scope
'''
# Reading variable from an enclosing (non-global) scope
def outer1():
  verbose = True
  def inner():
    print(verbose) # True
  inner()
outer1()


# Wrong way of modifying variable from enclosing scope
def outer2():
  been_called = False
  def inner():
    been_called = True # This is a new local variable, not the one from outer2
  inner()
  print(been_called) # False
outer2()

# Right way of modifying variable from enclosing scope
def outer3():
  been_called = False
  def inner():
    nonlocal been_called # Refers to the variable in outer3
    been_called = True
  inner()
  print(been_called) # True
outer3()


# Wrong way of modifying variable from enclosing scope
def outer4():
  count = 0
  def inner():
    count = count + 1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
    # print(count) # Never executed, since the previous line raised an exception
  inner()
outer4()

# Right way of modifying variable from enclosing scope
def outer5():
  count = 0
  def inner():
    nonlocal count
    count += 1
    print(count) # 1
  inner()
outer5()


# If a variable in an enclosing scope refers to a mutable value (list, deque, heap, dictionary, set, etc), you can change the value without declaring it `nonlocal`
def outer6():
  known = {0: 0, 1: 1}
  def inner():
    known[2] = 1 # Modifies the variable from outer6 without `nonlocal`
  inner()
  print(known) # {0: 0, 1: 1, 2: 1}
outer6()

# If you want to reassign the variable, you need to declare it `nonlocal`, because the reference to the variable from the outer scope is lost
def outer7():
  known = {0: 0, 1: 1}
  def inner():
    nonlocal known
    known = { } # Same as `known = dict()` # Reassignment
  inner()
  print(known) # { }
outer7()


# Pratical example

x = 100
def outest():
  x = 0 # Local scope, so this is not the `x` of the global scope

  def outer():
    x = 8
    print('b', x) # a 8

    def inner():
      nonlocal x # Gets the variable x defined in the nearest enclosing function (outer(), in this case), not the global (not declared, in this case) or local scope (also not declared, in this case).
      print('d', x) # c 8
      x = 7
      print('e', x) # d 7

    print('c', x) # b 8
    inner()
    print('f', x) # e 7

  print('a', x) # 0
  outer()
  print('g', x) # 0
outest()
print('h', x) # h 100 # `x` on global scope remains unchanged
'''



# Lambda

# Important: Lambdas are heavy.
# If you need to assign a lambda to a variable, you probably should use a function instead.
# func = lambda <args>: <expressions>

# Example
'''
# Worst way (you probably should use a function instead)
mysum = lambda x, y: x + y
print(mysum(2, 5)) # 7

# Best way
print((lambda x, y: x + y)(2, 5)) # 7
'''
'''
# *args here means "any amount of arguments"

# In this case, it's still useful to use a lambda when you are assigning it to a variable, because you are using it as a recursive function
mysum = lambda *args: args[0] if len(args) == 1 else args[0] + mysum(*args[1:])
print(mysum(2, 5, 100, 1000)) # 1107

# **kwargs here means "any amount of keyword arguments"
foo = lambda **kwargs: kwargs.get('x', 0) + kwargs.get('y', 0)
print(foo(x=2, y=3)) # 5

# With *args and **kwargs simultaneously
# *args captures all positional arguments as a `tuple` (2, 5, 100)
# **kwargs captures all named arguments as a `dictionary` {'a': 10, 'b': 20}
mysum = lambda *args, **kwargs: sum(args) + sum(kwargs.values())
print(mysum(2, 5, 100, a=10, b=20)) # 137
'''

# vararg expression (several amount of args)

'''
def printall(*args): # Any amount of arguments
  print(args)
printall(1, 2.0, '3') # (1, 2.0, '3')

t = (7, 3)
# print(divmod(t)) # TypeError: divmod expected 2 arguments, got 1
print(divmod(7, 3)) # (2, 1)
print(divmod(*t)) # (2, 1)

def printall2(*args, **kwargs):
  print(args, kwargs)

# `1`, `2.0` and `5.` are `args`
# `third` and `fourth` are `kwargs`
printall2(1, 2.0, 5., third='3', fourth='4') # (1, 2.0, 5.0) {'third': '3', 'fourth': '4'}



class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(%g, %g)' % (self.x, self.y)

# The `*` operator unpacks iterables like tuples, lists, or sets into individual elements.
coords = [3, 4]
point1 = Point(*coords) # Unpacks list into positional arguments
print(point1)  # (3, 4)

# The `**` unpacks mappings like dictionaries into key-value pairs.
data   = {'x': 5, 'y': 6}
point2 = Point(**data) # Unpacks dictionary into keyword arguments
print(point2)  # (5, 6)

# When working with functions with a large number of parameters,
# it is often useful to create dictionaries and pass them as arguments to specify the most frequently used options.



# Packing the arguments 1, 2, 3 into a tuple (1, 2, 3) (like Lua `pack` for tables)
print((1, 2, 3)) # (1, 2, 3)

# Unpacking elements of an iterable (`nums`) as arguments to `foo` (like Lua `unpack` for tables)
nums = [1, 2, 3]
print(*nums) # 1 2 3


# Packing keyword arguments into a dictionary
# Below, there are 2 ways of doing this for dictionary
print(dict([('a', 0), ('c', 2), ('b', 1)])) # {'a': 0, 'c': 2, 'b': 1}
t1 = ['a', 'b', 'c']
t2 = [1, 2, 3]
print(dict(zip(t1, t2))) # {'a': 1, 'b': 2, 'c': 3}

def show_kwargs(c, b, a):
  print(c, b, a) # 3 2 1
show_kwargs(**{'a': 1, 'b': 2, 'c': 3}) # Unpacking dictionary elements as keyword arguments
'''



# Tuple
'''
def foo(x, *args, y): # Only 1 vararg expression (*args) is allowed
  print(x, y, args)

foo('X', 1, 2, 3, y='Y') # X Y (1, 2, 3)
# Y needs to have the "y=" because is after a vararg expression
foo('X', y='Y') # X Y ()
'''

# Dictionary
'''
def foo(x, **kwargs): # Cannot have any parameters after the dictionary vararg expression (**kwargs)
  print(x, kwargs)

foo('X', y='Y', z='Z') # X {'y': 'Y', 'z': 'Z'}
foo('X') # X {}
'''



# Nested function

'''
def foo(string):
  inverted_string = ''.join(list(string)[::-1])

  def internal_foo(string): # Nested function
    print(' '.join([string] * 3))

  internal_foo(inverted_string)

print(foo) # <function foo at 0x000001BFCF278E00>
# print(internal_foo) # NameError: name 'internal_foo' is not defined

foo("dog") # god god god
foo("live") # evil evil evil
'''
