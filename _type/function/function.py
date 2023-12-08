# Function

# Function VS Method
# A function is not attached to any class
# A method is the same as function, but attached to a class

# Example
'''
def foo() -> None: # Return nothing
  pass # Do nothing
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



# Escope

# Local escope
'''
def foo():
  x = 7
  print(x) # 7
foo()
print(x) # Error: 'x' is not defined
'''

# Global escope
'''
def foo():
  print(x)
  print(y)
x = 7
print(x) # 7
foo() # Print x (7), but throws an error for y ('y' is not defined)
y = 8
'''

# Non local escope
# foo2 uses x as a "global" var, but just on previous escope (foo function)
# As soon as the foo execution ends, x resets to its default value
# So you don't need to have a global variable, reseting it every time you run foo()
'''
def foo():
  x = 7
  def foo2():
    nonlocal x
    print(x)
    x += 1
  foo2()
  foo2()
  foo2()
foo() # 7 8 9 7 8 9
'''
# This way, it will execute something and then return a list for you to keep adding to it later on
'''
def foo():
  l = []
  def add_new_value(item):
    nonlocal l
    l.append(item)
    print(l)
  return add_new_value
my_private_list = foo()
my_private_list(7) # 7
my_private_list(8) # 8
my_private_list(9) # 9
'''

# Overwriting variable with same name
'''
def foo():
  x = 8
  print(x)
x = 7
print(x) # 7
foo() # 8
print(x) # 7
'''

# Editing global variable with function
'''
def foo():
  global x
  x = 8
foo()
print(x) # 8
'''



# vararg expression (several amount of args)

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



# Lambda

# func = lambda <args>: <expressions>

# Example
'''
sum = lambda x, y: x + y
print(sum(2, 5)) # 7
'''
'''
sum = lambda *args: args[0] if len(args) == 1 else args[0] + sum(*args[1:])
# If list has 1 element, return args[0]
# Else, sum args[0] to a sum of the next values
# Note: args[1:] is tuple from args[1] to end, *args[1:] unpack the tuple elements as parameters of sum
# Important: Lambdas are heavy. If you need to assign a lambda to a variable, you should use def instead.
print(sum(2, 5, 100, 1000)) # 1107
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
