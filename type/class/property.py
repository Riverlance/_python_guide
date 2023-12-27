# Property
'''
A property is created using a descriptor.
Don't use descriptors if property is enough.

You can use properties (managed attributes), when you need to modify
their internal implementation without changing the public API of the class.
Providing stable APIs can help you avoid breaking your users' code
when they rely on your classes and objects.
'''

# Generic
'''
class FooClass():
  def __init__(self, x):
    self.__x = x

  def getX(self):
    return self.__x

  def setX(self, value):
    self.__x = value

  def delX(self):
    del self.__x

  x = property(getX, setX, delX, 'Docs of FooClass.x property.')

# Get
foo = FooClass('Bob')
# print(foo.__x) # AttributeError: 'FooClass' object has no attribute '__x'
# print(foo._FooClass__x) # Not recommended, because it ignores the getter by getting the original value.
print(foo.x) # Bob

# Set
foo.x = 'John'
print(foo.x) # John

# Del
del foo.x
print(getattr(foo, 'x', None)) # None

# Docs
print(FooClass.x.__doc__) # Docs of FooClass.x property.
'''
# Best
'''
class FooClass():
  def __init__(self, x):
    self.__x = x

  @property
  def x(self):
    'Docs of FooClass.x property.'
    return self.__x

  # Not in use, this does the same as above
  # @x.getter
  # def x(self):
  #   return self.__x

  @x.setter
  def x(self, value):
    self.__x = value

  @x.deleter
  def x(self):
    del self.__x

# Get
foo = FooClass('Bob')
# print(foo.__x) # AttributeError: 'FooClass' object has no attribute '__x'
# print(foo._FooClass__x) # Not recommended, because it ignores the getter by getting the original value.
print(foo.x) # Bob

# Set
foo.x = 'John'
print(foo.x) # John

# Del
del foo.x
print(getattr(foo, 'x', None)) # None

# Docs
print(FooClass.x.__doc__) # Docs of FooClass.x property.
'''
'''
class Person():
  def __init__(self, first_name, last_name):
    self.__first_name = first_name
    self.__last_name = last_name

  @property
  def name(self):
    'Docs of FooClass.name property.'
    return f'{self.__first_name} {self.__last_name}'

  # Not in use, this does the same as above
  # @name.getter
  # def name(self):
  #   return f'{self.__first_name} {self.__last_name}'

  @name.setter
  def name(self, first_name):
    self.__first_name = first_name

  @name.deleter
  def name(self):
    del self.__first_name
    del self.__last_name

# Get
person = Person('River', 'Lance')
print(person.name) # River Lance

# Set
person.name = 'John'
print(person.name) # John Lance

# Del
del person.name
print(getattr(person, 'name', None)) # None

# Docs
print(Person.name.__doc__) # Docs of FooClass.name property.
'''



# Descriptor

'''
class FooClass():
  def __init__(self, x):
    self.__x = x

  # Descriptor of x property

  @property
  def x(self):
    "Docs of FooClass.x property."
    return self.__x

  # Not in use, this does the same as above
  # @x.getter
  # def x(self):
  #   return self.__x

  @x.setter
  def x(self, value):
    self.__x = value

  @x.deleter
  def x(self):
    del self.__x

foo = FooClass(7)

# Get
# print(foo.__x) # AttributeError: 'FooClass' object has no attribute '__x'
# print(foo._FooClass__x) # Not recommended, because it ignores the getter by getting the original value.
print(foo.x) # 7

# Set
foo.x = 8
print(foo.x) # 8

# Del
del foo.x
print(getattr(foo, 'x', None)) # None

# Docs
print(FooClass.x.__doc__) # Docs of FooClass.x property.
'''
