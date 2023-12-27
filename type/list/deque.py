from collections import deque



# Deque
# Queue with 2 sides.

'''
dq = deque('ghi')
dq2 = dq.copy()
dq3 = deque(dq, maxlen=5)
'''

# Empty value
'''
empty_dq = deque()
print(empty_dq) # deque([])
'''

# Value
'''
print(dq) # deque(['g', 'h', 'i'])
print([item for item in dq]) # ['g', 'h', 'i']
print(list(item for item in dq)) # ['g', 'h', 'i']
print(dq[0]) # g
print(dq[-1]) # i
print(len(dq)) # 3
print('h' in dq) # True
print(dq.count('g')) # 1
'''

'''
# Append
dq.append('j')
print(dq) # deque(['g', 'h', 'i', 'j'])
dq.appendleft('k')
print(dq) # deque(['j', 'g', 'h', 'i', 'j'])

# Pop
dq.pop()
print(dq) # deque(['k', 'g', 'h', 'i']) # Poped out 'j'

# Pop left
dq.popleft()
print(dq) # deque(['g', 'h', 'i']) # Poped out 'k'
'''

'''
# Reverse
dq2.reverse()
print(dq2) # deque(['i', 'h', 'g'])

# Remove
dq2.remove('h')
print(dq2) # deque(['i', 'g'])

# Extend
dq2.extend('jk')
print(dq2) # deque(['i', 'g', 'j', 'k'])

# Extend left
dq2.extendleft('lm')
print(dq2) # deque(['m', 'l', 'i', 'g', 'j', 'k'])

# Rotate
dq2.rotate(1) # Items goes 1 slot to right (like it was counting from left to right starting at -1 pos, which is 'k')
print(dq2) # deque(['k', 'm', 'l', 'i', 'g', 'j'])
dq2.rotate(2) # Items goes 2 slots to right (like it was counting from left to right starting at -2 pos, which is 'g')
print(dq2) # deque(['g', 'j', 'k', 'm', 'l', 'i'])
dq2.rotate(-2) # Items goes 2 slots to left (like it was counting from left to right starting at 2 pos, which is 'k')
print(dq2) # deque(['k', 'm', 'l', 'i', 'g', 'j'])

# maxlen
print(dq2.maxlen) # None
print(dq3.maxlen) # 5
print(dq3) # deque(['g', 'h', 'i'])
dq3.extend('jkl')
print(dq3) # deque(['h', 'i', 'j', 'k', 'l'], maxlen=5) # Adds ['j', 'k', 'l'], overwriting 'g'
'''
