# yield
'''
The 'yield' statement produces a generator object and can return multiple values (as iterator) to the caller without terminating the program,
whereas a 'return' statement is used to return a value to the caller from within a function and it terminates the program.
'''

'''
def foo(n):
  for i in range(n):
    yield i ** 2

for i in foo(5):
  print(i) # 0 1 4 9 16

generator_object = foo(5)
print(list(generator_object)) # [0, 1, 4, 9, 16]

generator_object_2 = foo(5)
print(next(generator_object_2)) # 0
print(next(generator_object_2)) # 1
print(next(generator_object_2)) # 4
print(next(generator_object_2)) # 9
print(next(generator_object_2)) # 16
'''

# send

'''
# Instead of getting values, it can send a value to do something inside foo.
# If no value is sent, x is None.
def foo(n):
  for i in range(n):
    x = yield i ** 2 # Receives a value from 'send' function and also generates a value which is i ** 2
    if x != None:
      break
  print('Finished!')

generator = foo(5)
for i in generator:
  print(i) # 0 1 4

  # Custom condition to stop
  if i > 2:
    try:
      generator.send(True) # Send a flag to break the 'for' loop inside of 'foo'
    except StopIteration: # Raised because the 'x' flag forced 'foo' to stop
      print('Forced exit on i > 2')
'''
