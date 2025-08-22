'''
Point class
'''

from copy import copy

class Point:
  """Represents a point in 2-D space."""
  pass

blank   = Point() # Create a new empty Point instance
blank.x = 3.0
blank.y = 4.0

def print_point(p):
  print(p, '(%g, %g)' % (p.x, p.y))
print_point(blank) # <__main__.Point object at 0x0000029A9A9A74D0> (3, 4)

blank2 = copy(blank) # Create a copy of blank

print(blank is blank2) # False; blank and blank2 are different objects
print(blank == blank2) # False; they are different objects in memory, even if they have the same content; `==` has the same behavior as `is` for objects that don't implement `__eq__` method

blank2.x = 5.0
print_point(blank) # <__main__.Point object at 0x0000029A9A9A74D0> (3, 4)
print_point(blank2) # <__main__.Point object at 0x0000029A9AC256D0> (5, 4)



'''
Rectangle class
'''

from copy import deepcopy

class Rectangle:
  """Represents a rectangle.
  attributes: width, height, corner.
  """
  pass

def find_center(rect):
  p   = Point()
  p.x = rect.corner.x + rect.width/2
  p.y = rect.corner.y + rect.height/2
  return p

box          = Rectangle()
box.width    = 100.0
box.height   = 200.0
box.corner   = Point()
box.corner.x = 0.0
box.corner.y = 0.0
box_center   = find_center(box)

print(box.width, box.height, box.corner.x, box.corner.y, box_center.x, box_center.y) # 100.0 200.0 0.0 0.0 50.0 100.0

box3 = deepcopy(box) # Create a deep copy of box
# If you use copy instead of deepcopy, it will only copy the reference to the corner Point object, not its content.
# So Point remains as a reference to the same object in memory, not a new object.
# That's why deepcopy is used here to ensure that box3 has its own copy of the corner Point object.

print(box3 is box) # False; box and box3 are different objects
print(box3.corner is box.corner) # False; box3 has its own copy of the corner Point object
# box3 and box are completely independent objects in memory, even if they have the same content.

print(hasattr(box, 'width')) # True; box has an attribute named 'width'
print(hasattr(box, 'area')) # False; box does not have an attribute named 'area'
print(vars(box)) # {'width': 100.0, 'height': 200.0, 'corner': <__main__.Point object at 0x00000244D4E55950>}

# Iterate over the attributes
def print_attributes(obj):
  for attr in vars(obj):
    print(attr, getattr(obj, attr))
print_attributes(box) # width 100.0; height 200.0; corner <__main__.Point object at 0x00000244D4E55950>

try:
  box_x = box.width
  box_y = box.area
except AttributeError:
  box_x = 0
  box_y = 0
print(box_x, box_y) # 0 0; box.width is 100.0, but box.area does not exist, so it raises an AttributeError and sets box_x to 0 and box_y to 0



'''
Time class
'''

class Time:
  """Represents the time of day.
  attributes: hour, minute, second.
  """

  #def __str__(self):
  #  return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

time        = Time()
time.hour   = 11
time.minute = 59
time.second = 30


def time_to_str(time):
  return '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

def print_time(time):
  print(time_to_str(time))

Time.__str__ = time_to_str


def time_to_int(time):
  minutes = time.hour * 60 + time.minute
  seconds = minutes * 60 + time.second
  return seconds

def int_to_time(seconds):
  time                   = Time()
  minutes, time.second   = divmod(seconds, 60) # Same as `= (seconds // 60, seconds % 60)`
  time.hour, time.minute = divmod(minutes, 60) # Same as `= (minutes // 60, minutes % 60)`
  return time

def valid_time(time):
  if time.hour < 0 or time.minute < 0 or time.second < 0:
    return False
  if time.minute >= 60 or time.second >= 60:
    return False
  return True


'''
def add_time(t1, t2):
  sum        = Time()
  sum.hour   = t1.hour + t2.hour
  sum.minute = t1.minute + t2.minute
  sum.second = t1.second + t2.second

  if sum.second >= 60:
    minutes = sum.second // 60

    sum.second -= minutes * 60
    sum.minute += minutes

  if sum.minute >= 60:
    hours = sum.minute // 60

    sum.minute -= hours * 60
    sum.hour   += hours

  return sum
'''

def add_time(t1, t2):
  #if not valid_time(t1) or not valid_time(t2):
  #  raise ValueError("Invalid time values")

  # Raises AssertionError if not valid.
  # Assertions are used for debugging purposes and can be disabled in production.
  # You can also ignore assertions in production code by using `python -O` (optimize mode).
  assert valid_time(t1) and valid_time(t2), "Invalid time values"

  return int_to_time(time_to_int(t1) + time_to_int(t2))

Time.__add__ = add_time


'''
def increment(time, seconds):
  time.second += seconds
  if time.second >= 60:
    time.second -= 60
    time.minute += 1
  if time.minute >= 60:
    time.minute -= 60
    time.hour += 1
'''

def increment(time, seconds):
  return int_to_time(time_to_int(time) + seconds)


start           = Time()
start.hour      = 9
start.minute    = 45
start.second    = 0
duration        = Time()
duration.hour   = 1
duration.minute = 35
duration.second = 0
done            = add_time(start, duration)

print_time(done) # 11:20:00

'''
class Time:
  def print_time(self):
    print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
'''
# Or:
Time.print_time = print_time

Time.print_time(done) # 11:20:00
done.print_time() # 11:20:00
print(done) # 11:20:00; It uses the __str__ method defined in the Time class

time_to_add        = Time()
time_to_add.hour   = 1
time_to_add.minute = 30
time_to_add.second = 0
print(done + time_to_add) # 12:50:00; It uses the __add__ and __str__ methods defined in the Time class


class Time2:
  # Constructor
  def __init__(self, hour=0, minute=0, second=0):
    self.hour   = hour
    self.minute = minute
    self.second = second

  # Methods

  def is_valid(self):
    if self.hour < 0 or self.minute < 0 or self.second < 0:
      return False
    if self.minute >= 60 or self.second >= 60:
      return False
    return True

  def time_to_int(self):
    return (self.hour * 60 + self.minute) * 60 + self.second

  # Comparation

  def is_equal(self, other):
    return self.time_to_int() == other.time_to_int()

  def is_after(self, other):
    return self.time_to_int() > other.time_to_int()

  def is_before(self, other):
    return self.time_to_int() < other.time_to_int()

  # String

  def __str__(self):
    return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

  # Add

  def __add__(self, other): # self + other
    return int_to_time(self.time_to_int() + other.time_to_int() if isinstance(other, Time2) else other)

  def __radd__(self, other): # other + self
    return self.__add__(other)



'''
Card, Deck class
'''

import random

class Card:
  """Represents a standard playing card."""
  def __init__(self, suit=0, rank=2):
    self.suit = suit
    self.rank = rank

  suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

  def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

  '''
  def __lt__(self, other):
    # Check suit
    if self.suit < other.suit: return True
    if self.suit > other.suit: return False

    # Rank are the same; Check rank
    return self.rank < other.rank
  '''

  '''
  def __lt__(self, other):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return t1 < t2
  '''

  def __lt__(self, other):
    return (self.suit, self.rank) < (other.suit, other.rank)

class Deck:
  def __init__(self):
    self.cards = []

    for suit in range(4):
      for rank in range(1, 14):
        card = Card(suit, rank)
        self.cards.append(card)

  def __str__(self):
    res = []

    for card in self.cards:
      res.append(str(card))

    return '\n'.join(res)

  def pop_card(self):
    return self.cards.pop()

  def add_card(self, card):
    self.cards.append(card)

  def shuffle(self):
    random.shuffle(self.cards)

# deck = Deck()
# print(deck)

class Hand(Deck):
  """Represents a hand of playing cards."""
  def __init__(self, label=''):
    # super().__init__() # Ignore this line, so we can init an empty cards list
    self.cards = []
    self.label = label

  def move_cards(self, hand, num):
    for i in range(num):
      hand.add_card(self.pop_card())

# It inspects the MRO (Method Resolution Order) and finds the first class where a given method is defined
def find_defining_class(obj, meth_name):
  for ty in type(obj).mro(): # Iterate over the Method Resolution Order (MRO) of the object's type
    if meth_name in ty.__dict__: # Check if the method name exists in the current class dictionary (not inherited)
      return ty # Returns the class where the method was first found

hand = Hand()
print(find_defining_class(hand, 'shuffle')) # <class '__main__.Deck'>



class MyClass:
  # Constructor
  def __init__(self, list=[], private_list=[]):
    self.list           = list
    self.__private_list = private_list # private attribute

  def push(self, value):
    self.__private_list.append(value)

  def pop(self):
    value = self.__getlast()
    del self.__private_list[-1]
    return value

  def print_private_list(self):
    print(self.__private_list)

  def __getlast(self): # private method
    return self.__private_list[-1]

my_obj = MyClass()



# Read

# Public attribute
'''
# Append value to list
print(my_obj.list) # []
# my_obj.list.append(7)
print(my_obj.list) # [7]
'''

# Private attribute
# Uses "dunder" (double underscore) to make a attribute as private
'''
# Not allowed, since __private_list is private
# print(my_obj.__private_list)

# Append value to private list
my_obj.print_private_list() # []
my_obj.push(7)
my_obj.push(8)
my_obj.print_private_list() # [7, 8]
print(my_obj._MyClass__private_list) # [7, 8] # Not recommended, since __private_list is a private attribute
'''

# Public method
'''
my_obj.push(7)
my_obj.print_private_list() # [7]
'''

# Private method
'''
my_obj.push(7)

# Not allowed, since __getlast is private
# print(my_obj.__getlast()) # AttributeError: 'MyClass' object has no attribute '__getlast'
'''



# Class as function ()
# Functions are classes, that's how functions supports decorators (see Decorator in function.py).

'''
class foo_callback():
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    return 7

foo_callback_obj = foo_callback()

print(foo_callback_obj) # <__main__.foo_callback object at 0x0000020D14AA6BD0>
print(foo_callback_obj()) # 7
'''
