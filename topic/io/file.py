import io



# Write and read content

'''
# Instance buffer
buffer = io.StringIO()

# Write on buffer
buffer.write('Hello, world!\n')
buffer.write('Hello!\n')

# Get buffer value
print(repr(buffer.getvalue())) # 'Hello, world!\nHello!\n'
'''

# Instance buffer with content

'''
# Instance buffer with content
buffer = io.StringIO('Hello, world!\nHello!\n')
# Get buffer value
print(repr(buffer.getvalue())) # 'Hello, world!\nHello!\n'
'''

# Read lines

'''
# Read lines
buffer = io.StringIO(buffer.getvalue())
for line in buffer.readlines():
  print(repr(line)) # 'Hello, world!\n' 'Hello!\n'
'''



# Writing to a buffer as text
# It can creates a text file.

'''
import sys
buffer = io.StringIO()

stdout = sys.stdout # temp
sys.stdout = buffer # swap
print('Hello, world!') # <Send this value to the buffer>
print('Hello!', 'World!') # <Send these values to the buffer>
sys.stdout = stdout # swap back
print(repr(buffer.getvalue())) # 'Hello, world!\nHello! World!\n'
'''

# Writing to a buffer as binary
# It can creates a binary file.

'''
import sys
stream = io.BytesIO()

stream.write(b'Hello, world!')
print(stream.getvalue()) # b'Hello, world!'
'''



# Writing to a file
'''
file = open('../../data/assets/file_1.txt', 'w')
file.write("This here's the wattle,\n")
file.write("the emblem of our land.\n")
file.close()
'''

# Read the whole file
'''
file = open('../../data/assets/file_2.txt', 'r')
print(file.read()) # Prints file content
print(file.read()) # Prints nothing (because you need to reopen the file again)
file.close()
'''

# Print each line
'''
file = open('../../data/assets/file_2.txt', 'r')
for line in file.readlines():
  print(line)
file.close()
'''
'''
file = open('../../data/assets/file_2.txt', 'r')
for line in file:
  print(line, end='') # Print without putting default new line, like os.write of Lua
file.close()
'''

# Fast way to do something on each line of file
'''
file = open('../../data/assets/file_2.txt', 'r')
lines = file.readlines()
print(lines) # ['Hello, world!\n', 'Hello!\n']
lines = [line.rstrip() for line in lines]
print(lines) # ['Hello, world!', 'Hello!']
file.close()
'''



# Clean way to open file

# Print each line
'''
with open('../../data/assets/file_2.txt', 'r') as file:
  for line in file:
    print(line, end='')
'''

# 'with' keyword
# Useful when the special method '__exit__' is implemented
'''
class MyClass(object):
  def __enter__(self):
    print('Entered')
    return self

  def __exit__(self, __exc_type, __exc_val, __exc_tb):
    print('Exited')

with MyClass() as obj:
  print(7) # Entered 7 Exited

def my_open():
  return MyClass()

with my_open() as my_opened_obj:
  print(8) # Entered 8 Exited
'''



# Struct

# https://www.youtube.com/watch?v=eTOw-Cw_VkI&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=76
