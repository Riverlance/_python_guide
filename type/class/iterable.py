# Iterable class

# Gets values according to SquareNumber1

'''
class SquareNumber1():
  def __getitem__(self, value):
    return value ** 2

square1_obj = SquareNumber1()

for v in range(5):
  print(square1_obj[v]) # 0 1 4 9 16

for v in square1_obj:
  if v > 16:
    break
  print(v) # 0 1 4 9 16

# Never stops because StopIteration never happens
# print([v for v in square1_obj if v <= 16])
'''

# With StopIteration
'''
class SquareNumber2():
  def __init__(self, len):
    self.len = len

  def __getitem__(self, value):
    if value > self.len:
      raise StopIteration # Or IndexError
    return value ** 2

square2_obj = SquareNumber2(4)

for v in square2_obj:
  print(v) # 0 1 4 9 16
print([v for v in square2_obj]) # [0, 1, 4, 9, 16]
print([v for v in SquareNumber2(5)]) # [0, 1, 4, 9, 16, 25]
'''

# With list
'''
class SquareNumber3():
  def __init__(self, *args):
    self.list = []
    for arg in args:
      self.list.append(arg)

  def __getitem__(self, value):
    return self.list[value] ** 2

square3_obj = SquareNumber3(0, 2, 4)

for v in square3_obj:
  print(v) # 0 4 16
print([v for v in square3_obj]) # [0, 4, 16]
'''

# Slice

'''
class SquareNumber4():
  def __getitem__(self, value):
    if isinstance(value, int):
      print('index', value)
    elif isinstance(value, slice):
      print('slice', value.start, value.stop, value.step)
    else:
      print('unknown')

SquareNumber4()[7] # index 7
SquareNumber4()[1:7:3] # slice 1 7 3
SquareNumber4()[1:7] # slice 1 7 None
SquareNumber4()[:7] # slice None 7 None
SquareNumber4()['Hello'] # unknown
'''

# __getitem__, __setitem__, __delitem__, __contains__, __len__
'''
class SquareNumber5():
  def __init__(self, *args):
    self.list = []
    for arg in args:
      self.list.append(arg)

  def __getitem__(self, value):
    return self.list[value] ** 2

  def __setitem__(self, index, value):
    self.list.insert(index, value)

  def __delitem__(self, index):
    del self.list[index]

  def __contains__(self, value):
    return value in self.list

  def __len__(self):
    return len(self.list)

  def __str__(self):
    return f'{self.__class__.__name__}({self.list}) = {[self.__getitem__(k) for k in range(len(self.list))]}'

square5_obj = SquareNumber5(0, 2, 4)
print(square5_obj) # SquareNumber5([0, 2, 4]) = [0, 4, 16]

square5_obj[1] = 5
print(square5_obj) # SquareNumber5([0, 5, 2, 4]) = [0, 25, 4, 16]

del square5_obj[2]
print(square5_obj) # SquareNumber5([0, 5, 4]) = [0, 25, 16]

print(5 in square5_obj) # True
print(2 not in square5_obj) # True

print(len(square5_obj)) # 3
'''
