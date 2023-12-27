# Dictionary

def foo(): return
empty_dict_1 = dict()
empty_dict_2 = {}
translations = { 'cat': 'gato', 'dog': 'cachorro' }
numbers = { 'one': 1, 'two': 2, 'three': 3 }
numbers['four'] = 4
mixed = { 'cat': 'gato', 'one': 1, 'half': 0.5, 'true': True, 'false': False, 7: 7., 8.: 8, True: False, False: True, foo: 'func', 9: 'to be removed' }
if 9 in mixed:
  del mixed[9]

# Base
'''
# Empty
print(empty_dict_1, type(empty_dict_1)) # {} <class 'dict'>
print(empty_dict_2, type(empty_dict_2)) # {} <class 'dict'>

# Get value by key
print(numbers['one']) # 1
# But 'one' is not an attribute of numbers dict object (this is the same in Lua coding, but not in Python)
# If you want the syntax below, use namedtuple
# print(numbers.one) # AttributeError: 'dict' object has no attribute 'one'

# Get value using default if not found
print(numbers.get('five', 5)) # If cannot find 'five', returns 5

print(translations) # {'cat': 'gato', 'dog': 'cachorro'}
print(numbers) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
print(mixed) # {'cat': 'gato', 'one': 1, 'half': 0.5, 'true': True, 'false': False}
print('cat' in translations) # True
print('cat' in numbers) # False
print(len(translations)) # 2
'''

# Keys loop
'''
for k in mixed.keys():
  print(f"'{k}' = {mixed[k]}")
'''
'''
for k in mixed:
  print(f"'{k}' = {mixed[k]}")
'''

# Values loop
'''
for v in mixed.values():
  print(v)
'''

# Keys & values loop
'''
for i in mixed.items():
  print(f"'{i[0]}' = {i[1]}")
'''
'''
for (k, v) in mixed.items():
  print(f"'{k}' = {v}")
'''

# Constructor
'''
print(dict()) # {}

dict_keys = ['a', 'b', 'c']
dict_values = ['A', 'B', 'C']
my_dict = dict(zip(dict_keys, dict_values))
print(my_dict) # {'a': 'A', 'b': 'B', 'c': 'C'}
print(dict(zip(dict_values, dict_keys))) # {'A': 'a', 'B': 'b', 'C': 'c'}
print({v: k for k, v in my_dict.items()}) # {'A': 'a', 'B': 'b', 'C': 'c'}
'''



# Example of dictionary in Lua coding style
# Where dict.keyword is the same of dict['keyword']
# Where dict.keyword = value = value is the same of dict['keyword'] and
# You won't be able to use dict.get('keyword') anymore, not even make any class method of LuaDict

'''
class LuaDict:
  blocked_keywords = ['_LuaDict__dict'] # Private var name of __dict

  def __init__(self, dict):
    self.__dict = dict

  def __getitem__(self, index):
    return self.__dict[index]

  def __setitem__(self, index, value):
    self.__dict[index] = value

  def __getattr__(self, __name):
    if __name in self.blocked_keywords:
      return super().__getattr__(__name)
    return self.__dict[__name]

  def __setattr__(self, __name, __value):
    if __name in self.blocked_keywords:
      super().__setattr__(__name, __value)
      return
    self.__dict[__name] =__value

translations = LuaDict({ 'cat': 'gato', 'dog': 'cachorro' })
print(translations['cat']) # gato
translations['cat'] = 'GATO'
print(translations['cat']) # GATO

print(translations.cat) # GATO
translations.cat = 'gatinho'
print(translations.cat) # gatinho
'''
