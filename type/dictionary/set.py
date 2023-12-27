# Set
# Are a list of values as a dictionary, because they are unique values.
# Its syntax remembers of dictionary, but has nothing to do with it.
# Its order does not matters.



# Base

'''
empty_set = set()
print(empty_set, type(empty_set)) # set() <class 'set'>

# Wrong way to initialize empty set
# empty_set = {}
# print(empty_set, type(empty_set)) # {} <class 'dict'>

setv = {7, 8, 9}
print(setv, type(setv)) # {8, 9, 7} <class 'set'>

print(set('mississippi')) # {'m', 'i', 'p', 's'}
'''

# Its order does not matters.
'''
# Example of dictionary just to compare with set
for i in dict(zip([7, 8, 9], ['a', 'b', 'c'])).items():
  print(f'k[{i[0]}] = v[{i[1]}]')

# Set
for i in set([7, 8, 9]):
  print(i) # 8 9 7
'''

# Update

'''
# Add
setv = {7, 8, 9}
print(setv) # {8, 9, 7}
setv.update([10])
print(setv) # {8, 9, 10, 7}
setv.update({11, 12})
print(setv) # {7, 8, 9, 10, 11, 12}

# Remove
setv.remove(10)
print(setv) # {7, 8, 9, 11, 12}
'''

# Operations

'''
s1 = {'A', 'B', 'C', 'D', 'E'}
s2 = {'B', 'D', 'F'}
s3 = {'A', 'B'}
print(s1 | s2) # {'C', 'A', 'B', 'E', 'D', 'F'} # All items from both (you can also use it as s1.union(s2))
print(s1 & s2) # {'D', 'B'} # Items that are inside both (you can also use it as s1.intersection(s2))
print(s1 - s2) # {'A', 'E', 'C'} # s1 - s2 (you can also use it as s1.difference(s2))
print(s1 ^ s2) # {'E', 'F', 'A', 'C'} # Unique items from both (you can also use it as s1.symmetric_difference(s2))
print(s3 < s1) # True - If s3 is inside s1 (you can also use it as s3.issubset(s1))
print(s1 > s3) # True - If s1 contains s3 (you can also use it as s1.issuperset(s3))
'''



# Comprehension expression
# Same as list comprehension, but returned values cannot repeat.

'''
s1 = {i + 10 for i in range(10)}
print(s1) # {10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

s2 = {i * 10 for i in range(1, 11)}
print(s2) # {100, 70, 40, 10, 80, 50, 20, 90, 60, 30}

s3 = {i * 10 for i in range(10) if i%2 == 0}
print(s3) # {0, 40, 80, 20, 60}

s4 = {i * 10 if i % 2 == 0 else i + 2 for i in range(10)}
print(s4) # {0, 3, 5, 7, 40, 9, 11, 80, 20, 60}

s5 = {i for i in s4 if i % 2 == 0}
print(s5) # {0, 40, 80, 20, 60}

s6 = {i + j + k for i in 'ab' for j in 'lm' for k in 'xy'}
print(s6) # {'blx', 'bmx', 'aly', 'bly', 'amy', 'amx', 'alx', 'bmy'}
'''
