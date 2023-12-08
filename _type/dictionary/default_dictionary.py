from collections import defaultdict



# defaultdict
# Assumes a default value in case the key is not found.
# My own opinion: Not worth it. It's better to use dict.get(key, default_value).

# Without default dict
'''
numbers = { 'one': 1, 'two': 2, 'three': 3 }
print(numbers.get('five', 5)) # If cannot find 'five', returns 5
'''

# With default dict

'''
ddict = defaultdict(int, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # 0 # Because it is int()

ddict = defaultdict(float, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['one']) # 1
print(ddict['five']) # 0.0

def on_not_found():
  return 'not found'
ddict = defaultdict(on_not_found, { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # not found

ddict = defaultdict(lambda: 'not found', { 'one': 1, 'two': 2, 'three': 3 })
print(ddict['five']) # not found
print(ddict.__missing__('one')) # not found # Shows what returns if 'one' is not found
'''

'''
# Example of usage
def count_words(text: str) -> int:
  counter = defaultdict(int)
  for word in text.split(' '):
    counter[word] += 1
  return counter

# Example above without defaultdict
def count_words_(text: str) -> int:
  counter = {}
  for word in text.split(' '):
    counter[word] = counter.get(word, 0) + 1
  return counter

print(count_words('apple apple apple pear orange orange')) # defaultdict(<class 'int'>, {'apple': 3, 'pear': 1, 'orange': 2})
print(count_words_('apple apple apple pear orange orange')) # {'apple': 3, 'pear': 1, 'orange': 2}
'''
