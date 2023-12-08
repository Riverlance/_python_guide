# Metaclass
# Class is instance of 'type'
# 'type' is a metaclass.
# Metaclass is for build classes. If __metaclass__ is not defined, __metaclass__ will be 'type'.

# Create an empty class
'''
class Empty():
  pass
print(Empty, type(Empty)) # <class '__main__.Empty'> <class 'type'>
print(Empty(), type(Empty())) # <__main__.Empty object at 0x000001737B246BD0> <class '__main__.Empty'>
'''



# Create a class dinamically

# Base
'''
class Foo(): pass
foo = Foo()
print(foo.__class__) # <class '__main__.Foo'>
print(Foo.__class__) # <class 'type'>
print(type) # <class 'type'>
print(type(type)) # <class 'type'>
'''

# Class 'my_foo_type'
'''
m_foo = type('my_foo_type', (), {'color': 'gray', 'time': 7})
print(m_foo) # <class '__main__.my_foo_type'>
print(m_foo.__class__) # <class 'type'>
print(m_foo.color) # gray
print(m_foo.time) # 7
print(issubclass(m_foo, dict)) # False
'''

# Class 'my_foo_type' that inherits from 'dict'
'''
def instancefoo(**kwargs):
  return type('my_foo_type', (dict,), kwargs)

m_foo = instancefoo(color='gray', time=7)
print(m_foo) # <class '__main__.my_foo_type'>
print(m_foo.__class__) # <class 'type'>
print(m_foo.color) # gray
print(m_foo.time) # 7
print(issubclass(m_foo, dict)) # True
'''



# Create a metaclass

'''
class MetaFoo(type):
  # Executed before the class is created.
  # Often used to define bases or dict.
  # Returns instance of meta, which is a class.
  def __new__(meta, name, bases, _dict):
    print('\t__new__')
    print('\tMeta: ', meta)
    print('\tMeta name: ', name)
    print('\tMeta bases: ', bases) # superclasses
    print('\tMeta dict: ', _dict)
    return super().__new__(meta, name, bases, _dict)

  # Executed after the class is created.
  def __init__(self, name, bases, _dict):
    print('\t__init__')
    print('\tMeta name: ', name)
    print('\tMeta bases: ', bases) # superclasses
    print('\tMeta dict: ', _dict)
    super().__init__(name, bases, _dict)

print('>> Meta of Foo')
class Foo(metaclass=MetaFoo):
  att = 7
  def func(self, parameter):
    print(parameter)

print('>> Meta of SubclassFoo')
class SubclassFoo(Foo):
  attr = 8
  def funct(self, parameter):
    print(parameter, parameter)

a = Foo()
b = SubclassFoo()
print(a.att) # 7
print(b.att) # 7
print(b.attr) # 8
'''



# Singleton class
# Creates a single object for each class. If object exists already, returns this object.
# SingletonClassA can have only 1 object. SingletonClassB can have only 1 object.

# Using decorator (best way)
# You choose which classes or subclasses are singleton simply by placing @singleton above.

'''
See the singleton example in decorator.py.
'''

# Manually
# Each child is singleton themselves (SingletonClassA and SingletonClassB).

'''
from typing import Any

class SingletonMeta(type):
  __instances = {}

  def __call__(self, *args: Any, **kwargs: Any) -> Any:
    if self not in self.__instances:
      self.__instances[self] = super().__call__(*args, **kwargs)
    return self.__instances[self]

  def printinstanceslen():
    print(len(SingletonMeta.__instances), SingletonMeta.__instances)

class SingletonClassA(metaclass=SingletonMeta):
  pass

class SingletonClassB(metaclass=SingletonMeta):
  pass

foo1 = SingletonClassA()
foo2 = SingletonClassA()
foo3 = SingletonClassB()
print(foo1 == foo2, foo1 == foo3, foo2 == foo3) # True False False

# 2 because 1 is instance of A and 1 of B
SingletonMeta.printinstanceslen() # 2 {<class '__main__.SingletonClassA'>: <__main__.SingletonClassA object at 0x0000026BEA0ABE60>, <class '__main__.SingletonClassB'>: <__main__.SingletonClassB object at 0x0000026BEA306750>}
'''
