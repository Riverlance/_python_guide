import os, sys, subprocess, hashlib



# os

# Process id
'''
print(os.getpid())
'''

# Actual work directory (cwd)
# print(os.getcwd()) # D:\River\code\Python\_projects\pytest

# Change directory
# print(os.getcwd()) # D:\River\code\Python\_projects\pytest
# os.chdir('..')
# print(os.getcwd()) # D:\River\code\Python\_projects

# Create directory
'''
os.mkdir('my_folder')
'''

# Remove directory
'''
os.rmdir('my_folder')
'''

# List directory and files in actual path
# Readmore: https://www.youtube.com/watch?v=j-8md7xIqWc&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=114
'''
print(os.listdir())

# "walks" through a directory, prints the names of all files, and calls itself recursively on all directories
def walk(dirname):
  for name in os.listdir(dirname):
    path = os.path.join(dirname, name)
    if os.path.isfile(path):
      print(path)
    else:
      walk(path)
'''

# Rename
# os.rename(src, dst)

# Remove
# os.remove(path)

# Random string
# Useful to use as key for encryption
'''
print(os.urandom(7)) # b'!.[\xd7\xf5\xd3\x11'
'''

# Constants
# Instead of '/my/file/path', use f'{os.sep}my{os.sep}file{os.sep}path'
# os.curdir is like '.' of a path
# os.pardir is like '..' of a path
'''
print((os.pathsep, os.sep, os.pardir, os.curdir, os.linesep)) # (';', '\\', '..', '.', '\r\n')
'''

# Environment variables
# print(os.environ)
# print(list(os.environ.keys()))
# print(list(os.environ.values()))
# OS, PATH, APPDATA, LOCALAPPDATA, COMPUTERNAME, USERNAME
# print(os.environ['PATH'])
# print(os.environ['OS']) # Windows_NT
# print(os.environ['APPDATA']) # C:\Users\River\AppData\Roaming
# print(os.environ['LOCALAPPDATA']) # C:\Users\River\AppData\Local
# print(os.environ['COMPUTERNAME']) # RIVER
# print(os.environ['USERNAME']) # River

# os.path

'''
# isdir
print(os.path.isdir('module')) # True
print(os.path.isdir('os_sys_test.py')) # False

# isfile
print(os.path.isfile('module')) # False
print(os.path.isfile('os_sys_test.py')) # True

# exists
print(os.path.exists('module')) # True
print(os.path.exists('os_sys_test.py')) # True

# getsize
print(os.path.getsize('os_sys_test.py')) # 2139 # (bytes)
'''

# split
# Split path and file.
# print(os.path.split(f'module{os.sep}module_example.py')) # ('module', 'module_example.py')

# join
# Join path and file.
# print(os.path.join('module', 'module_example.py')) # module\module_example.py

# dirname
# Get directory path of path.
# print(os.path.dirname(f'module{os.sep}module_example.py')) # module

# basename
# Get the final component of path.
# print(os.path.basename(f'module{os.sep}module_example.py')) # module_example.py

# splittext
# Split the extension from a pathname.
# print(os.path.splitext('myfilename.py')) # ('myfilename', '.py')

# normpath (relative path)
# Normalize path, eliminating double slashes, etc.
# print(os.path.normpath('')) # .
# print(os.path.normpath('.')) # .
# print(os.path.normpath('..')) # ..
# print(os.path.normpath('module/module_example.py')) # module\module_example.py
# print(os.path.normpath(r'module\\module_example.py')) # module\module_example.py

# abspath (absolute path)
# print(os.path.abspath('')) # D:\River\code\Python\_projects\pytest
# print(os.path.abspath('.')) # D:\River\code\Python\_projects\pytest
# print(os.path.abspath('..')) # D:\River\code\Python\_projects
# print(os.path.abspath('module/module_example.py')) # D:\River\code\Python\_projects\pytest\module\module_example.py
# print(os.path.abspath(r'module\\module_example.py')) # D:\River\code\Python\_projects\pytest\module\module_example.py

# Execute terminal command, returning error of execution (0 means no error)

'''
# Execute terminal command 'type', that reads the file 'file.txt'
os.system(r'type data\assets\file_1.txt')

# os.system('dir')
os.system('dir module')
'''

# Execute terminal command and stores its return.

'''
fp = os.popen('ls -l')
print(fp) # <os._wrap_close object at 0x77ae42d44b00>
print(fp.read())
# total 8
# -rwxr-xr-x 1 riverlance registered_users 232 Aug  5 17:56 README.txt
# -rw-rw-r-- 1 riverlance registered_users  62 Aug 12 20:50 hello.py
fp.close()

fp = os.popen('ls -l')
for line in fp.readlines():
  print(line, end='')
# total 8
# -rwxr-xr-x 1 riverlance registered_users 232 Aug  5 17:56 README.txt
# -rw-rw-r-- 1 riverlance registered_users  62 Aug 12 20:50 hello.py
fp.close()
'''
'''
command = os.popen(r'type data\assets\file_1.txt')
print(command.read())
command.close()

command = os.popen(r'type data\assets\file_1.txt')
print(command.readlines())
command.close()
'''



# sha1

'''
with open(r"data\assets\file_1.txt", "rb") as f:
  print(hashlib.sha1(f.read()).hexdigest())
'''

# sha256

'''
with open(r"data\assets\file_1.txt", "rb") as f:
  print(hashlib.sha256(f.read()).hexdigest())
'''

# sha512

'''
with open(r"data\assets\file_1.txt", "rb") as f:
  print(hashlib.sha512(f.read()).hexdigest())
'''

# md5
# Readmore: https://www.geeksforgeeks.org/python/md5-hash-python/

'''
with open(r"data\assets\file_1.txt", "rb") as f:
  print(hashlib.md5(f.read()).hexdigest())
'''



# sys

# Platform
'''
print(sys.platform) # win32
if sys.platform == 'win32':
  print('Windows')
'''

# Path

# Known paths of the application
'''
print(sys.path) # ['d:\\River\\code\\Python\\_projects\\pytest', 'D:\\Program Files\\Python312\\python312.zip', 'D:\\Program Files\\Python312\\DLLs', 'D:\\Program Files\\Python312\\Lib', 'D:\\Program Files\\Python312', 'D:\\Program Files\\Python312\\Lib\\site-packages']
'''

# Add a known folder
# Useful for add asset folders of images, audios and so on
# sys.path.append('folder_name')

# Exit the application

# sys.exit(0)

# Modules

'''
print(sys.modules) # Dictionary of loaded modules (imports) on application
'''

# Exception

# exec_info (see exception.py)

# argv
# Parameters used to execute this application.
# Readmore: https://www.youtube.com/watch?v=pZtPRnp2hAE&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=110

'''
print(sys.argv) # ['d:\\River\\code\\Python\\_projects\\pytest\\os_sys_test.py']
'''

# Stream - stdin, stdout, stderr
# Readmore: https://www.youtube.com/watch?v=3d0U_Rk49q0&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=111
# Readmore: https://www.youtube.com/watch?v=QO1AimzhKFk&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=112

# stdout
'''
print('Hello')
sys.stdout.write('Hello\n') # Also returns the chars count
'''

# stdin
'''
print(input()) # Prints what you have typed
print(sys.stdin.readline()) # Prints what you have typed, including LF (Line Feed)
print(sys.stdin.readline()[:-1]) # Prints what you have typed
'''
