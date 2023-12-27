# Decorator
# Attaches info to class, method or function without needing to edit itself.
# It's a way to make changes without editing the original name or parameters.



# Attribute encapsulation - Class

'''
class MyClass():
  pass
MyClass.decorated = 7 # Attaches 'decorated' to 'MyClass'
my_obj = MyClass()
print(MyClass.decorated, my_obj.decorated)
'''

# Attribute encapsulation - Method

'''
class MyClass():
  def foo():
    pass
MyClass.foo.decorated = 7 # Attaches 'decorated' to 'foo'
my_obj = MyClass()
print(MyClass.foo.decorated, my_obj.foo.decorated)
'''

# Attribute encapsulation - Function

'''
def foo(arg):
  return arg
foo.decorated = True # Attaches 'decorated' to 'foo'
print(foo.decorated) # True
'''



'''
def div_decorator(callback):
  def _callback(*args):
    return f'<div>{callback(*args)}</div>'
  return _callback

def p_decorator(callback):
  def _callback(*args):
    return f'<p>{callback(*args)}</p>'
  return _callback

def strong_decorator(callback):
  def _callback(*args):
    return f'<strong>{callback(*args)}</strong>'
  return _callback

def html_tag(tag_name):
  def decorator(callback):
    def _callback(*args):
      return f'<{tag_name}>{callback(*args)}</{tag_name}>'
    return _callback
  return decorator
'''
def div_decorator(callback):
  return lambda *args: f'<div>{callback(*args)}</div>'
def p_decorator(callback):
  return lambda *args: f'<p>{callback(*args)}</p>'
def strong_decorator(callback):
  return lambda *args: f'<strong>{callback(*args)}</strong>'
def html_tag(tag_name):
  return lambda callback: lambda *args: f'<{tag_name}>{callback(*args)}</{tag_name}>'

# Callback - Class

'''
def singleton(cls):
  new = cls.__new__
  instance = None

  def __new__(cls, *args, **kwargs):
    nonlocal instance
    if instance is None:
      instance = new(cls, *args, **kwargs)
    return instance

  cls.__new__ = __new__
  return cls

class Singleton():
  pass

@singleton
class SingletonClassA(Singleton):
  pass

@singleton
class SingletonClassB(Singleton):
  pass

foo1 = SingletonClassA()
foo2 = SingletonClassA()
foo3 = SingletonClassB()
print(foo1 == foo2, foo1 == foo3, foo2 == foo3) # True False False
'''
'''
class oncall():
  def __init__(self, callback):
    self.callback = callback
  def __call__(self, *args, **kwargs):
    print('Executed something before the callback execution.')
    ret = self.callback(*args, **kwargs)
    print('Executed something after the callback execution.')
    return ret

@oncall
def sum(x, y):
  print('Executed sum.')
  return x + y

print(sum(7, 8))
'''

# Callback - Method

# Newbie way
'''
class MyClass():
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def sum(self):
    return f'The sum of {self.__x} + {self.__y} is {self.__x + self.__y}.'

  def sum_p(self):
    sum_p = p_decorator(self.sum)
    return sum_p()

my_obj = MyClass(7, 8)
print(my_obj.sum()) # The sum of 7 + 8 is 15.
print(my_obj.sum_p()) # <p>The sum of 7 + 8 is 15.</p>
'''

# Correct way
'''
class MyClass():
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  @p_decorator
  def sum(self):
    return f'The sum of {self.__x} + {self.__y} is {self.__x + self.__y}.'

my_obj = MyClass(7, 8)
print(my_obj.sum()) # <p>The sum of 7 + 8 is 15.</p>
'''
'''
class MyClass():
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  @div_decorator
  @p_decorator
  @strong_decorator
  def sum(self):
    return f'The sum of {self.__x} + {self.__y} is {self.__x + self.__y}.'

my_obj = MyClass(7, 8)
print(my_obj.sum()) # <div><p><strong>The sum of 7 + 8 is 15.</strong></p></div>
'''

# Callback - Function
'''
Tip:
  You could create requirements in functions, eg, `@login_required` in logout() function.
  This way, you can execute the action of logout only if you are logged in already.
  You could add the same `@login_required` to other actions that requires the user to be logged in.
'''

# Newbie way
'''
def sum(x, y):
  return f'The sum of {x} + {y} is {x + y}.'

print(sum(7, 8)) # The sum of 7 + 8 is 15.

sum_p = p_decorator(sum)
print(sum_p(7, 8)) # <p>The sum of 7 + 8 is 15.</p>
'''

# Correct way
'''
@p_decorator
def sum(x, y):
  return f'The sum of {x} + {y} is {x + y}.'

print(sum(7, 8)) # <p>The sum of 7 + 8 is 15.</p>
'''
'''
@div_decorator
@p_decorator
@strong_decorator
def sum(x, y):
  return f'The sum of {x} + {y} is {x + y}.'

print(sum(7, 8)) # <div><p><strong>The sum of 7 + 8 is 15.</strong></p></div>
'''

# Callback - Tester of method/function example
'''
If you want to print the parameters of a function before use them,
just add `@print_parameters` to it temporarily.\n
After you finish the tests, simply remove the `@print_parameters`.
'''
'''
def print_parameters(callback):
  def _callback(*args):
    print(args)
    return callback(*args)
  return _callback

@print_parameters
def sum(x, y):
  return f'The sum of {x} + {y} is {x + y}.'

print(sum(7, 8)) # Print the parameters (7, 8) and then the result 15
'''



# Default decorators

# @property

'''
See property.py for it.
'''

# @staticmethod
# Static method is like an independent function, but attached to the class.
# It may not use anything related to the object or class.
# If something from class is needed, use @classmethod instead.

'''
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @staticmethod
  def isAdult(age):
    return age > 18

p1 = Person('River', 29)
p2 = Person('Lance', 7)

print(Person.isAdult(29)) # True
print(Person.isAdult(7)) # False
print(Person.isAdult(p1.age)) # True
print(Person.isAdult(p2.age)) # False
'''

# @classmethod
# `self` becomes the class on parameters, instead of the object.
# The only difference between @classmethod and @staticmethod is that,
# in the @classmethod, the class is bound to the method as the first argument (self).

'''
import datetime
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_birth_year(cls, name, year):
    return cls(name, datetime.date.today().year - year)

p1 = Person('River', 29)
p2 = Person.from_birth_year('Lance', 1994)

print(p1.name, p1.age) # River 29
print(p2.name, p2.age) # Lance 29
'''

# @abstractmethod

'''
import abc

class GetterSetter(metaclass=abc.ABCMeta):
    # __metaclass__ = abc.ABCMeta # Turn into abstract class

    @abc.abstractmethod
    def set_value(self, input):
        """Set a value in the instance."""
        return

    @abc.abstractmethod
    def get_value(self):
        """Get and return a value from the instance."""
        return

class MyClass(GetterSetter):
    def set_value(self, input): # Required method implementation from GetterSetter
        self.value = input

    def get_value(self): # Required method implementation from GetterSetter
        return self.value

# x = GetterSetter() # Error, because you cannot instantiate an abstract class

x = MyClass()
print(x)
'''



# Tag
# Tag are dynamic decorators.

# Method

'''
class MyClass():
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  @html_tag('div')
  @html_tag('p')
  @html_tag('strong')
  def sum(self):
    return f'The sum of {self.__x} + {self.__y} is {self.__x + self.__y}.'

my_obj = MyClass(7, 8)
print(my_obj.sum()) # <div><p><strong>The sum of 7 + 8 is 15.</strong></p></div>
'''

# Function

'''
@html_tag('div')
@html_tag('p')
@html_tag('strong')
def sum(x, y):
  return f'The sum of {x} + {y} is {x + y}.'

print(sum(7, 8)) # <div><p><strong>The sum of 7 + 8 is 15.</strong></p></div>
'''
