# Tuple
# Same as list, but as a constant value
# You can manipulate between tuples, though

# Empty tuple
'''
empty_tp_1 = tuple()
empty_tp_2 = ()
print(empty_tp_1, type(empty_tp_1)) # () <class 'tuple'>
print(empty_tp_2, type(empty_tp_2)) # () <class 'tuple'>
'''

# Tuple with 1 value only
'''
tp = (7,)
print(tp) # (7,)
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
