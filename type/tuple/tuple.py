# Tuple

# Like a list, but an unmutable value.

# A tuple is a sequence of values.
# The values can be of any type and can be indexed by integers.
# So, in this sense, tuples are very similar to lists.
# The important difference is that tuples are immutable.

# Useful mainly for:
# 1. Return values of functions
# 2. Parameters of functions
# 3. Key of dictionaries (because they need to be immutable)

# You can manipulate between tuples, though.

# Empty tuple
'''
empty_tp_1 = tuple()
empty_tp_2 = ()
print(empty_tp_1, type(empty_tp_1)) # () <class 'tuple'>
print(empty_tp_2, type(empty_tp_2)) # () <class 'tuple'>

# No item assignment!
# empty_tp_1[0] = 1 # TypeError: 'tuple' object does not support item assignment
'''

# Tuple with a single value only
'''
tp = (7,) # Same as `tp = 7`, # Warning: This is NOT the same as `tp = (7)`, which makes tp be an `int`
print(tp) # (7,)
'''

# Tuple with multiple values
'''
tp = (7, 8, 9) # Same as `tp = 7, 8, 9`
print(tp) # (7, 8, 9)
print(*tp) # 7 8 9 (unpacking the tuple)

# tuple(param) # param must be a sequence (string, list or another tuple)
tp = tuple([7, 8, 9])
print(tp) # (7, 8, 9)
tp = tuple('hello')
print(tp) # ('h', 'e', 'l', 'l', 'o')
tp = tuple(tp) # Copy, but useless, since tuples are immutable
print(tp) # ('h', 'e', 'l', 'l', 'o')

print(tp[0], tp[1], tp[2], tp[3], tp[4]) # h e l l o
print(tp[-1], tp[-2], tp[-3], tp[-4], tp[-5]) # o l l e h
print(tp[:]) # ('h', 'e', 'l', 'l', 'o')
print(tp[1:4]) # ('e', 'l', 'l')

addr          = 'monty@python.org'
uname, domain = addr.split('@')
print(uname) # monty
print(domain) # python.org
'''

# Merge tuples
'''
tp = (1, 10, 100, 1000)
tp2 = (7, 8, 9)
print(tp + tp2) # (1, 10, 100, 1000, 7, 8, 9)
tp += tp2
print(tp) # (1, 10, 100, 1000, 7, 8, 9)
tp += tp
print(tp) # (1, 10, 100, 1000, 7, 8, 9, 1, 10, 100, 1000, 7, 8, 9)
'''

# Duplicate tuple
'''
tp = (1, 10, 100)
print(tp * 3) # (1, 10, 100, 1, 10, 100, 1, 10, 100)
'''

# Check value inside
'''
tp = (1, 10, 100)
print(10 in tp) # True
print(15 in tp) # False
print(15 not in tp) # True
print(10 not in tp) # False
'''

# Convert from list
'''
l = [7, 8, 9]
print(tp(l)) # (7, 8, 9)
'''

# As return value
'''
t = divmod(7, 3)
print(t) # (2, 1)

quot, rem = divmod(7, 3)
print(quot) # 2
print(rem) # 1

def min_max(t):
  return min(t), max(t)
print(min_max([7, 8, 9])) # (7, 9)
'''

# Filtering

# Relational operators work with tuples and other sequences.
# It starts by comparing the first element of each sequence.
# If they are equal, it moves on to the next element, and so on, until it finds elements that are different.
# Subsequent elements are ignored (even if they are very large).
'''
print((0, 1, 2) < (0, 3, 4)) # True
# This means:
# 0 < 0 --> Equal, then skip to the next
# 1 < 3 --> True

print((0, 1, 2000000) < (0, 3, 4)) # True
# This means:
# 0 < 0 --> Equal, then skip to the next
# 1 < 3 --> True

print((0, 2000000, 1) < (0, 4, 3)) # False
# This means:
# 0 < 0 --> Equal, then skip to the next
# 2000000 < 4 --> False

print((1, 2, 3) < (1, 2, 4)) # True
# This means:
# 1 < 1 --> Equal, then skip to the next
# 2 < 2 --> Equal, then skip to the next
# 3 < 4 --> True

print((1, 2, 3) < (1, 2, 3)) # False
# This means:
# 1 < 1 --> Equal, then skip to the next
# 2 < 2 --> Equal, then skip to the next
# 3 < 3 --> Equal, then skip to the next
# No more elements to compare, then return False

# This is the algorithm:
for i in range(len(A)):
  if A[i] < B[i]: # A is less than B
    return True
  elif A[i] > B[i]: # A is greater than B
    return False
  # if A[i] == B[i]: # Skips to the next element, but this code is not even needed
  #   continue
  return False # All elements were equal, so return False

# Usage

# Example 1

names = [("Ana", "Silva"), ("Ana", "Costa"), ("Bruno", "Alves")]
print(sorted(names)) # [('Ana', 'Costa'), ('Ana', 'Silva'), ('Bruno', 'Alves')]

# Example 2

# Function to order a simple list
def simple_sort(lst):
  for i in range(len(lst)):
    min_idx = i
    for j in range(i+1, len(lst)):
      if lst[j] < lst[min_idx]:
        min_idx = j
    lst[i], lst[min_idx] = lst[min_idx], lst[i]

t1 = [5, 3, 8, 1, 2]
simple_sort(t1)
print(t1) # [1, 2, 3, 5, 8]

t2 = [('a', 5), ('a', 3), ('b', 8), ('b', 1), ('b', 2)]
simple_sort(t2)
print(t2) # [('a', 3), ('a', 5), ('b', 1), ('b', 2), ('b', 8)]
'''

# Swap
'''
a = (1, 2, 3)
b = (4, 5, 6)
a, b = b, a # Swap

print(a) # (4, 5, 6)
print(b) # (1, 2, 3)
'''
