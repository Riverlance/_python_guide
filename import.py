# Warning:
#
# If you import a module that has already been imported, Python does nothing.
# It won't re-read the file, even if it has been modified.
# If you want to reload a module, you can use the built-in reload function.
# But this can cause problems, so the safest option is to restart the interpreter and import the module again.



# Import

# Imports math as its own namespace, so you always need to use, for example, math.pi (best way)
'''
import math
print(math.pi) # 3.1415...
'''

# Adds pi to your module's namespace (not really recommended)
'''
from math import pi
print(pi) # 3.1415...
pi = 3.14 # pi of my own module, which overwrites the pi of math
print(pi) # 3.14
'''

# Adds everything of math to your module's namespace (not recommended at all)
'''
from math import *
print(pi) # 3.1415...
pi = 3.14 # pi of my own module, which overwrites the pi of math
print(pi) # 3.14
'''



# Import 'module_example' module

# This is possible only if module/__init__.py has `from . import module_example`
'''
import module
print(module) # <module 'module' from 'D:\\River\\code\\Python\\_python_guide\\module\\__init__.py'>
print(module.module_example) # <module 'module.module_example' from 'D:\\River\\code\\Python\\_python_guide\\module\\module_example.py'>
print(module.module_example.my_value) # 7
print(module.module_example.my_foo()) # 8
'''

'''
import module.module_example
print(module.module_example.my_value) # 7

import module.module_example as my_module
print(my_module.my_value) # 7
'''

'''
from module import module_example
print(module_example.my_value) # 7

from module import module_example as my_module
print(my_module.my_value) # 7
'''
