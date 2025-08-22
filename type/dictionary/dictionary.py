# Dictionary

def foo(): return
empty_dict      = { } # Same as `empty_dict = dict()`, but without calling the construct of dict; In short, the result is the same, returning an object of dict anyway
translations    = { 'cat': 'gato', 'dog': 'cachorro' }
numbers         = { 'one': 1, 'two': 2, 'three': 3 }
numbers['four'] = 4
mixed           = { 'cat': 'gato', 'one': 1, 'half': 0.5, 'true': True, 'false': False, 7: 7., 8.: 8, True: False, False: True, foo: 'func', 9: 'to be removed' }
if 9 in mixed:
  del mixed[9]

# Base
'''
# Empty
print(empty_dict, type(empty_dict)) # {} <class 'dict'>

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
print(len(translations)) # 2
print('cat' in translations) # True (`cat` found as key)
print('cat' in numbers) # False (`cat` not found as key)
translations_values = translations.values()
print('gato' in translations_values) # True (`gato` found as value)

def histogram(s):
  d = { } # Same as `d = dict()`
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d
print(histogram('brontosaurus')) # {'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}

print(dict([('a', 0), ('c', 2), ('b', 1)])) # {'a': 0, 'c': 2, 'b': 1}
t1 = [1, 2, 3]
t2 = ['Sword', 'Axe', 'Club']
zip_dict = dict(zip(t1, t2))
print(zip_dict) # {1: 'Sword', 2: 'Axe', 3: 'Club'})
zip_dict.update([(4, 'Spear')]) # Add a new key-value pair
print(zip_dict) # {1: 'Sword', 2: 'Axe', 3: 'Club', 4: 'Spear'}

first_name = ['Caio', 'Rebecca', 'Gabriel']
last_name  = ['Moraes', 'Moraes', 'Moraes']
names      = list(zip(first_name, last_name)) # [('Caio', 'Moraes'), ('Rebecca', 'Moraes'), ('Gabriel', 'Moraes')]
phones     = ['0077', '3660', '1310']
contacts   = dict(zip(names, phones))
print(contacts) # {('Caio', 'Moraes'): '0077', ('Rebecca', 'Moraes'): '3660', ('Gabriel', 'Moraes'): '1310'}
for first, last in contacts:
  print(first, last, contacts[first, last]) # Caio Moraes 0077; Rebecca Moraes 3660; Gabriel Moraes 1310
'''

# Keys loop
'''
for k in mixed: # Same as `for k in mixed.keys()`
  print(f"'{k}' = {mixed[k]}")
'''

# Values loop
'''
for v in mixed.values():
  print(v)
'''

# Items (as tuples) loop
'''
for t in mixed.items():
  print(f"'{t[0]}' = {t[1]}")
'''
'''
for (k, v) in mixed.items():
  print(f"'{k}' = {v}")
'''

# Filter
'''
for k in sorted(mixed):
  print(f"'{k}' = {mixed[k]}")
'''

# Constructor
'''
print({ }) # Same as dict()

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
