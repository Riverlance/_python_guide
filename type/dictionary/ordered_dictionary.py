from collections import OrderedDict



# OrderedDict
# Order matters.
# Dictionary that remembers insertion order.

# Empty
'''
od_1 = OrderedDict()
print(od_1) # OrderedDict()
'''

# Editing
# Values are added to the final of the keys of the ordered dictionary
# You can pop them out from the end, or from a specific key
'''
od_2 = OrderedDict.fromkeys('abc')
print(od_2) # OrderedDict({'a': None, 'b': None, 'c': None})
od_2['a'] = 7
od_2['b'] = 8
od_2['c'] = 9
print(od_2) # OrderedDict({'a': 7, 'b': 8, 'c': 9})

od_3 = OrderedDict({7: '8'})
print(od_3) # OrderedDict({7: '8'})
od_3.update([(5, '5')])
print(od_3) # OrderedDict({7: '8', 5: '5'})
od_3.update([(1, '1'), (2, '2')])
print(od_3) # OrderedDict({7: '8', 5: '5', 1: '1', 2: '2'})
od_3[50] = '50'
print(od_3) # OrderedDict({7: '8', 5: '5', 1: '1', 2: '2', 50: '50'})
od_3[5] = '<5>'
print(od_3) # OrderedDict({7: '8', 5: '<5>', 1: '1', 2: '2', 50: '50'})

print(od_3.popitem()) # (50, '50')
print(od_3) # OrderedDict({7: '8', 5: '<5>', 1: '1', 2: '2'})
print(od_3.pop(5))
print(od_3) # OrderedDict({7: '8', 1: '1', 2: '2'})
'''

# Iterate like a normal dictionary
'''
for k in od_2.keys():
  print(k) # a b c
for v in od_2.values():
  print(v) # 7 8 9
for i in od_2.items():
  print(f'[{i[0]}] = [{i[1]}]') # [a] = [7] [b] = [8] [c] = [9]
'''

# Move to end
'''
od_3.move_to_end(5)
print(od_3) # OrderedDict({7: '8', 1: '1', 2: '2', 5: '5'})
# Move to beginning
od_3.move_to_end(1, False)
print(od_3) # OrderedDict({1: '1', 7: '8', 2: '2', 5: '5'})
'''

# Comprehension
'''
od_4 = OrderedDict((value, str(value)) for value in range(10) if value > 5)
print(od_4) # OrderedDict({6: '6', 7: '7', 8: '8', 9: '9'})
'''
