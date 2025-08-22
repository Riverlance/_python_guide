from collections import defaultdict



# defaultdict
# Assumes a default value in case the key is not found.
# My opinion: Not worth it for primitive types (int, float, etc), but worth it for complex types (list, dict, etc).
# It's better to use dict.get(key, default_value).



# Without default dict
'''
numbers = { 'one': 1, 'two': 2, 'three': 3 }
print(numbers.get('five', 5)) # If cannot find 'five', returns 5
'''



# With default dict

'''
ddict = defaultdict(int, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # 0 # Because it is int()
print(ddict) # defaultdict(<class 'int'>, {'one': 1, 'two': 2, 'three': 3, 'five': 0}) # It included the key 'five' automatically, once it was accessed

ddict = defaultdict(float, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['one']) # 1
print(ddict['five']) # 0.0

ddict = defaultdict(list)
ddict['one'].append(1)
ddict['one'].append(11)
ddict['two'].append(2)
ddict['two'].append(22)
ddict['two'].append(222)
print(ddict) # defaultdict(<class 'list'>, {'one': [1, 11], 'two': [2, 22, 222]})

def on_not_found():
  return 'not found'
ddict = defaultdict(on_not_found, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # not found

ddict = defaultdict(lambda: 'not found', { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # not found
print(ddict.__missing__('one')) # not found # Shows what returns if 'one' is not found
'''



# Examples

'''
# Example of below without defaultdict
def count_words_(text: str) -> int:
  counter = {}
  for word in text.split(' '):
    counter[word] = counter.get(word, 0) + 1
  return counter

# Example of usage
def count_words(text: str) -> int:
  counter = defaultdict(int)
  for word in text.split(' '):
    counter[word] += 1
  return counter

print(count_words('apple apple apple pear orange orange')) # defaultdict(<class 'int'>, {'apple': 3, 'pear': 1, 'orange': 2})
print(count_words_('apple apple apple pear orange orange')) # {'apple': 3, 'pear': 1, 'orange': 2}
'''

'''
# Simple algorithm
def all_anagrams(filename):
  d = { }
  for line in open(filename):
    word = line.strip().lower()
    t = signature(word)
    if t not in d:
      d[t] = [word]
    else:
      d[t].append(word)
  return d

# This can be simplified using setdefault.
# The problem with this solution is that it makes a new list every time, even if it's not necessary.
def all_anagrams(filename):
  d = {}
  for line in open(filename):
    word = line.strip().lower()
    t = signature(word)
    d.setdefault(t, []).append(word) # The parameter `[]` creates a new list; it will be used on the first time, but not on subsequent times (which is useless)
  return d

# We can avoid this problem and simplify the code by using a defaultdict.
def all_anagrams(filename):
  d = defaultdict(list)
  for line in open(filename):
    word = line.strip().lower()
    t = signature(word)
    d[t].append(word)
  return d
'''
