# Special methods (__init__, __eq__, ...)
# Don't use __getattribute__ if __getattr__ is enough.

# Without __str__
'''
class Fruit:
  def __init__(self, kind: str = 'Apple') -> None:
    self.__kind = kind

apple = Fruit()
print(apple) # <__main__.Fruit object at 0x00000222A9276BD0>
'''

# With __str__
'''
class Fruit:
  def __init__(self, kind: str = 'Apple') -> None:
    self.__kind = kind

  def __str__(self):
    return f'{self.__kind}'

apple = Fruit()
print(apple) # Apple
'''

# Without __eq__
'''
class Position:
  def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
    self.x = x
    self.y = y
    self.z = z

pos1 = Position(7, 8, 9)
pos2 = Position(7, 8, 9)

print(pos1 == pos2) # False
'''

# With __eq__
'''
class Position:
  def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
    self.x = x
    self.y = y
    self.z = z

  def __eq__(self, object):
    return self.x == object.x and self.y == object.y and self.z == object.z

pos1 = Position(7, 8, 9)
pos2 = Position(7, 8, 9)

print(pos1 == pos2) # True
'''

# Note about __eq__
'''
l1 = [7, 8, 9]
l2 = [7, 8, 9]
print(l1 == l2) # True, because list compares with __eq__
print(l1 is l2) # False, because it compares their memory addresses
l2 = l1
print(l1 is l2) # True, because l2 now is assigned with the address of l1
'''

# Without __add__
'''
class Position:
  def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
    self.x = x
    self.y = y
    self.z = z

pos1 = Position(1, 2, 3)
pos2 = Position(70, 800, 9000)

pos1 += pos2 # TypeError: unsupported operand type(s) for +: 'Position' and 'Position'
'''

# With __add__
'''
class Position:
  def __init__(self, x: int = 0, y: int = 0, z: int = 0) -> None:
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, object):
    self.x += object.x
    self.y += object.y
    self.z += object.z
    return self

pos1 = Position(1, 2, 3)
pos2 = Position(70, 800, 9000)

pos1 += pos2
print(pos1.x) # 71
print(pos1.y) # 802
print(pos1.z) # 9003
'''
