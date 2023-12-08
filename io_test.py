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
