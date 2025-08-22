from collections import namedtuple



# Named tuples are subclasses of tuple with named fields.
# They allow accessing values ​​by name or index, keeping the normal tuple operations.

'''
class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(%g, %g)' % (self.x, self.y)

Point = namedtuple('Point', ['x', 'y']) # Same as above

point = Point(1, 2)
print(point) # Point(x=1, y=2)

# You can access the elements of the named tuple by name
print(point.x) # 1
print(point.y) # 2

# But you can also treat a named tuple as a tuple
print(point[0]) # 1
print(point[1]) # 2
point_x, point_y = point
print(point_x) # 1
print(point_y) # 2

# Named tuples provide a quick way to define simple classes.
# The problem is that simple classes don't always stay simple.
# Later on, you might decide you want to add methods to a named tuple.
# In this case, you can define a new class that inherits from the named tuple:
class Pointier(Point): # extends from Point
  pass # Add more methods in here
# Or you could switch to a conventional class definition.
'''
'''
nt_1 = namedtuple('Point', 'x y')
nt_2 = namedtuple('Point', 'x, y')
nt_3 = namedtuple('Point', ['x', 'y'])
print(nt_1, nt_2, nt_3) # <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

nt_1_instance_1 = nt_1(7, 8)
print(nt_1_instance_1) # Point(x=7, y=8)
nt_1_instance_2 = nt_1(x=7, y=8)
print(nt_1_instance_2) # Point(x=7, y=8)
nt_1_instance_3 = nt_1(y=8, x=7)
print(nt_1_instance_3) # Point(x=7, y=8)

print(nt_1_instance_1.x, nt_1_instance_1[0]) # 7 7
print(nt_1_instance_1.y, nt_1_instance_1[1]) # 8 8
'''



# Variable names cannot starts with underscore ('_') and cannot be a reserved keyword (like int, if, def, for...).
# You can avoid issues with the mentioned above if you set rename=True.

'''
nt_1 = namedtuple('Func', 'def', rename=True) # Def is reserved keyword
nt_1_instance = nt_1(7)
print(nt_1_instance[0]) # 7
# This is not recommended though, because you still cannot use like below:
# print(nt_1_instance.def) # SyntaxError: invalid syntax
'''
