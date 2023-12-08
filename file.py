file = open('data/assets/file.txt', 'r')

# Read the whole file
'''
print(file.read()) # Prints file content
print(file.read()) # Prints nothing (because you need to reopen the file again)
'''

# Print each line
'''
for line in file.readlines():
  print(line)
'''
'''
for line in file:
  print(line, end='') # Print without putting default new line, like os.write of Lua
'''

# Fast way to do something on each line of file
'''
lines = file.readlines()
print(lines) # ['Hello, world!\n', 'Hello!\n']
lines = [line.rstrip() for line in lines]
print(lines) # ['Hello, world!', 'Hello!']
'''

# Closes the file
file.close()



# Clean way to open file

# Print each line
'''
with open('data/assets/file.txt', 'r') as file:
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
