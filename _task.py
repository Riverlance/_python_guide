# Task 1

'''
# x + y
x = int(input('Type x: '))
y = int(input('Type y: '))
print(f'The result of {x} + {y} is {x + y}')

# Circle area from radius
import math
r = int(input('Type radius: '))
print(f'The result of {math.pi} * {r} ** {2} = { math.pi * r ** 2 }')

# Arithmetic average
import statistics
x = int(input('Type x: '))
y = int(input('Type y: '))
z = int(input('Type z: '))
print(f'The arithmetic average of {x}, {y} and {z} is {statistics.mean([x, y, z])}')

# School exam grade
grade = int(input('Type grade: '))
def isStudentApproved(grade):
  if grade < 70:
    return False
  return True
print(f'The student is {'Approved' if isStudentApproved(grade) else 'Disapproved'}')

# Integer between interval
value = int(input("Type integer value: "))
print(f'The value is {'between' if 0 <= value <= 50 else 'not between'}')

# Integer between interval
value = int(input("Type integer value: "))
print(f'The value is {'less' if value < 50 else ('equal' if value == 50 else 'higher')}')
'''



# Task 2 - Sock merchant

'''
def sockMerchant(n, ar):
  # 1 <= n <= 100
  # 1 <= ar[i] <= 100 where 0 <= i < n

  # Count each value using a dictionary
  count = {}
  for v in ar:
    if v in count:
      count[v] += 1
    else:
      count[v] = 1

  # Sum each floor(count / 2) of dictionary
  result = 0
  for k in count:
    result += count[k] // 2

  return result

ar = [1, 2, 1, 2, 1, 3, 2] # list(map(int, input().rstrip().split()))
n = len(ar) # int(input())
print(sockMerchant(n, ar))
'''



# Task 3 - Jumping on the Clouds

'''
clouds = [0, 1, 0, 0, 0, 1, 0] # 0 - safe; 1 - danger; can jump 1 or 2 slots
# Note: It will never have two dangerous cloud in a row (..., 1, 1, ...)

# Examples
# [0, 1, 0, 1, 0] 2 jumps
# [0, 1, 0, 0, 1, 0] 3 jumps
# [0, 1, 0, 0, 0, 1, 0] 3 jumps
# [0, 1, 0, 0, 0, 0, 1, 0] 4 jumps
# [0, 1, 0, 0, 0, 0, 0, 1, 0] 4 jumps
# [0, 1, 0, 0, 0, 0, 0, 0, 1, 0] 5 jumps

def jumping_on_clouds(clouds : list) -> int:
  # Return the minimum jumps needed to win the game

  count = 0
  jumps = 0

  clouds_count = len(clouds)

  for i in range(clouds_count):
    v = clouds[i]

    # Is a dangerous cloud or is the last safe cloud
    if v == 1 or i == clouds_count - 1:
      jumps += (count // 2) + 1
      count = 0
    else:
      count += 1

  return jumps - 1

print(jumping_on_clouds(clouds))
'''



# Task 4 - Counting valleys

# Mountain is height is >= 0
# Valley is height < 0
# Step uphill adds 1 on height
# Step downhill removes 1 on height
# Return how many valleys on the path are there

'''
u = 1
d = -1
# path = [d, d, u, u, u, u, d, d] # Ret 1, since there are only one valley at the beginning (two first values)

# Examples
# path = [d, d, u, u, u, u, d, d] # -1 -2 -1 0 1 2 1 0 = 1 valley, since there are only one valley at the beginning (two first values)
path = [d, d, u, u, u, u, d, d, d, d, d] #  -1 -2 -1 0 1 2 1 0 -1 -2, -3 = 2 valleys, since there are two valleys, at the beginning (two first values) and at the end (three final values)

def count_valleys(path: list) -> int:
  level = 0
  valleys = 0
  add_valey = False
  path_size = len(path)

  for i in range(path_size):
    level += path[i]

    if not add_valey and level < 0:
      add_valey = True

    if add_valey and (level == 0 or i == path_size - 1):
      valleys += 1
      add_valey = False # Reset

  return valleys

print(count_valleys(path))
'''
