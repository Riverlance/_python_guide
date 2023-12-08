# Class

class MyClass:
  def __init__(self):
    self.list = []
    self.__private_list = [] # private attribute

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
