import os, sys, subprocess



# os

# Process id
'''
print(os.getpid())
'''

# Actual path (work path)
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
print(os.path.isdir('package_test')) # True
print(os.path.isdir('os_sys_test.py')) # False

# isfile
print(os.path.isfile('package_test')) # False
print(os.path.isfile('os_sys_test.py')) # True

# exists
print(os.path.exists('package_test')) # True
print(os.path.exists('os_sys_test.py')) # True

# getsize
print(os.path.getsize('os_sys_test.py')) # 2139 # (bytes)
'''

# split
# Split path and file.
# print(os.path.split(f'package_test{os.sep}import_test.py')) # ('package_test', 'import_test.py')

# join
# Join path and file.
# print(os.path.join('package_test', 'import_test.py')) # package_test\import_test.py

# dirname
# Get directory path of path.
# print(os.path.dirname(f'package_test{os.sep}import_test.py')) # package_test

# basename
# Get the final component of path.
# print(os.path.basename(f'package_test{os.sep}import_test.py')) # import_test.py

# splittext
# Split the extension from a pathname.
# print(os.path.splitext('myfilename.py')) # ('myfilename', '.py')

# normpath (relative path)
# Normalize path, eliminating double slashes, etc.
# print(os.path.normpath('')) # .
# print(os.path.normpath('.')) # .
# print(os.path.normpath('..')) # ..
# print(os.path.normpath('package_test/import_test.py')) # package_test\import_test.py
# print(os.path.normpath(r'package_test\\import_test.py')) # package_test\import_test.py

# abspath (absolute path)
# print(os.path.abspath('')) # D:\River\code\Python\_projects\pytest
# print(os.path.abspath('.')) # D:\River\code\Python\_projects\pytest
# print(os.path.abspath('..')) # D:\River\code\Python\_projects
# print(os.path.abspath('package_test/import_test.py')) # D:\River\code\Python\_projects\pytest\package_test\import_test.py
# print(os.path.abspath(r'package_test\\import_test.py')) # D:\River\code\Python\_projects\pytest\package_test\import_test.py

# Execute terminal command, returning error of execution (0 means no error)

'''
# Execute terminal command 'type', that reads the file 'file.txt'
os.system(r'type data\assets\file.txt')

# os.system('dir')
os.system('dir package_test')
'''

# Execute terminal command and stores its return.

'''
command = os.popen(r'type data\assets\file.txt')
print(command.read())

command = os.popen(r'type data\assets\file.txt')
print(command.readlines())
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
