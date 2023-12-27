# Inheritance

import random
from typing import Any

class Animal:
  def __init__(self, sound: str = 'Wolf!') -> None:
    self.__sound = sound

  def make_sound(self) -> None:
    print(f'The {self.__class__.__name__.lower()} made a sound: "{' '.join([self.__sound for i in range(random.randint(1, 3))])}"')

# Generic animal

# Cat
'''
cat = Animal('Meow!')
cat.make_sound()
'''

# Dog
'''
dog = Animal()
dog.make_sound()
'''

# Inheritance animal

# Single
'''
# Cat
class Cat(Animal):
  def __init__(self, sound: str = 'Wolf!') -> None:
    super().__init__(sound)
    self.flexible_body = True

# Dog
class Dog(Animal):
  def __init__(self, sound: str = 'Wolf!') -> None:
    super().__init__(sound)
    self.sense_of_smell = True

  def make_sound(self) -> None:
    print('Before make sound')
    super().make_sound()
    print('After made sound')

cat = Cat('Meow!')
cat.make_sound()
print(cat.flexible_body) # True

dog = Dog()
dog.make_sound()
print(dog.sense_of_smell) # True
'''

# Multiple
# In multiple inheritance, use ParentClassName.method_name instead of super().method_name.
'''
class ParentOne():
  def __init__(self) -> None:
    print(1, f'Init of parent of {self.__class__.__name__.lower()}')

class ParentTwo():
  def __init__(self) -> None:
    print(2, f'Init of parent of {self.__class__.__name__.lower()}')

class Child(ParentOne, ParentTwo):
  def __init__(self) -> None:
    print('Do something before call parent init')

    # super is ParentOne
    # super().__init__() # 1 Init of parent of child # Same as below
    ParentOne.__init__(self) # 1 Init of parent of child

    # To call init of ParentTwo, it needs to be explicity
    ParentTwo.__init__(self) # 2 Init of parent of child
    print('Do something after call parent init')

c = Child()
'''
