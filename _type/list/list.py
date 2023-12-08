# List

# Read values
'''
empty_list_1 = list()
empty_list_2 = []
print(empty_list_1, type(empty_list_1)) # [] <class 'list'>
print(empty_list_2, type(empty_list_2)) # [] <class 'list'>

numbers = [2, 4, 7, 9, 11]
print(numbers[0]) # 2
print(numbers[-1]) # 11
print(numbers[:]) # [2, 4, 7, 9, 11] (same as numbers.copy())
print(numbers[3:2]) # []
print(numbers[1:]) # [4, 7, 9, 11]
print(numbers[1:3]) # [4, 7]
print(numbers[:-2]) # [2, 4, 7]
print(numbers[0:len(numbers):2]) # [2, 7, 11] (range jumping each 2 values)
print(numbers[::-1]) # [11, 9, 7, 4, 2] (reverse list)
print(numbers[::-2]) # [11, 7, 2]

l1 = [1, 2, 3]
l2 = [7, 8]
print(l1 + l2) # [1, 2, 3, 7, 8]
print(l1 + []) # [1, 2, 3]
print(l1 * 2) # [1, 2, 3, 1, 2, 3]
print(l2 * 3) # [7, 8, 7, 8, 7, 8]

l3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(l3[3][0]) # 7

x, y = [7, 8]
print(x, y)

str = 'Hello'
print(list(str)) # ['H', 'e', 'l', 'l', 'o']
'''

# Loop on string
'''
for char in 'string':
  print(char) # s t r i n g
'''

# Negative indexes
'''
numbers = [2, 4, 7]
print(numbers[-1], numbers[-2], numbers[-3]) # 7 4 2
'''

# Range
'''
for i in range(5):
  print(i) # 0 to 4
for i in range(5, 10):
  print(i) # 5 to 9
for i in range(0, 11, 2):
  print(i) # 0, 2, 4, 6, 8, 10
for i in range(10, -1, -2):
  print(i) # 10 8 6 4 2 0
'''
'''
numbers = [2, 4, 7]
for i in range(len(numbers)):
  print(i, numbers[i])
'''
'''
for i in range(1, 16):
  if i % 2 == 1: # Jump odd values
    continue
  if i > 10: # Stops if i > 10
    break
  print(i) # 2 4 6 8 10
'''

# Arithmetic average for 'numbersCount'
'''
import statistics
numbersCount = int(input('Type how many numbers you want the arithmetic average to deal with: '))
numbers      = []
for _ in range(numbersCount):
  numbers.append(int(input('Type next number of list: ')))
print(f'The arithmetic average of {numbers} is {statistics.mean(numbers)}')
'''

# Update values of list
'''
numbers = [2, 4, 7]
# for v in numbers:
#   v *= 2
# print(numbers) # Still [2, 4, 7]
for i in range(len(numbers)):
  numbers[i] *= 2
print(numbers)
'''

# Remove number
'''
numbers = [2, 4, 7]
del numbers[1]
print(numbers) # [2, 7]
'''

# Add number
'''
numbers = [4]
numbers.append(7)
print(numbers) # [4, 7]
numbers.insert(0, 2)
print(numbers) # [2, 4, 7]
numbers.insert(2, 8)
print(numbers) # [2, 4, 8, 7]
'''

# Append & extend
'''
l = []
l.append(3)
print(l) # [3]
l.append([7, 8])
print(l) # [3, [7, 8]]
l.append('Hi')
print(l) # [3, [7, 8], 'Hi']
l.extend([9, 10])
print(l) # [3, [7, 8], 'Hi', 9, 10]
l.extend('Hi')
print(l) # [3, [7, 8], 'Hi', 9, 10, 'H', 'i']
'''

# all (checks if all elements are valid)
'''
print(all([1, 0, 0, 1, 1])) # False
print(all([1, 1, 1, 1])) # True
'''

# any (checks if any value are valid)
'''
print(any([1, 0, 0, 1, 1])) # True
print(any([0, 0, 0, 0])) # False
'''

# sum (sum all values in list, but all items needs to be numbers)
'''
print([9, 80, 700]) # 789
'''

# Filter
'''
l = [0, 1, 2, 3, 4, 5]
print(list(filter((lambda x: x % 2 == 0), l))) # [0, 2, 4]
'''

# Convert from map
'''
lmap = map(int, '0123')
print(list(lmap)) # [0, 1, 2, 3]

lmap = map(float, '0 10 21 32'.split())
print(list(lmap)) # [0.0, 10.0, 21.0, 32.0]

lmap = map((lambda x: x ** 2), range(4))
print(list(lmap)) # [0, 1, 4, 9]

lmap = map((lambda x, y: x + y), range(4), range(0, 31, 10)) # x is in range(4), y is in range(0, 31, 10)
print(list(lmap)) # [0, 11, 22, 33]

lmap = map((lambda x: x ** 2), filter(lambda x: x % 2 == 0, range(5)))
print(list(lmap)) # [0, 4, 16]
'''

# Convert from zip
'''
list_keys = ['a', 'b', 'c']
list_values = ['A', 'B', 'C']
print(list(zip(list_keys, list_values))) # [('a', 'A'), ('b', 'B'), ('c', 'C')]
print(list(zip(list_values, list_keys))) # [('A', 'a'), ('B', 'b'), ('C', 'c')]
'''

# See heapq.nlargest & heapq.nsmallest



# Comprehension expression

'''
l1 = [i + 10 for i in range(10)]
print(l1) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

l2 = [i * 10 for i in range(1, 11)]
print(l2) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

l3 = [i * 10 for i in range(10) if i%2 == 0]
print(l3) # [0, 20, 40, 60, 80]

l4 = [i * 10 if i % 2 == 0 else i + 2 for i in range(10)]
print(l4) # [0, 3, 20, 5, 40, 7, 60, 9, 80, 11]

l5 = [i for i in l4 if i % 2 == 0]
print(l5) # [0, 20, 40, 60, 80]

l6 = [i + j + k for i in 'ab' for j in 'lm' for k in 'xy']
print(l6) # ['alx', 'aly', 'amx', 'amy', 'blx', 'bly', 'bmx', 'bmy']
'''

# Generator
# Same as comprehension, but does not returns the values right-away.
# Instead, it creates a generator function to deal with the established expression only when it will be used.
# List stores all its values, generator reads all values one by one without needing to store all of them in memory.

'''
# Prints a list of values instantly, so its values are known right away because they are stored already in memory.
l = [i + 10 for i in range(5)]
print(l) # [10, 11, 12, 13, 14]
# Creates a generator object, so its values are not known because they are not stored in memory yet.
# If you don't mind to store the whole list of values, use 'list comprehension'. If you don't want to store them and just read them in a loop one by one, use generator.
gen_obj = (i + 10 for i in range(5))
print(gen_obj) # <generator object <genexpr> at 0x00000179134B5F20>
for i in gen_obj:
  print(i) # 10 11 12 13 14
'''



# Syntatic sugar

# Example
'''
squares = []
for i in range(1, 11): # Range: [1,11[ = 1~10
  if i % 2 == 0 and i != 10: # Only pairs
    squares.append(i ** 2)
print(squares) # [4, 16, 36, 64, 100]
'''
# Syntatic sugar (same code as above, but simplified)
'''
print([i ** 2 for i in range(1, 11) if i % 2 == 0 and i != 10]) # [4, 16, 36, 64]
print([i ** 2 for i in range(1, 11) if i % 2 == 0 if i != 10]) # [4, 16, 36, 64]
'''
