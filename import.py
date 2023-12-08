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

# Import 'import_test' module
'''
import package_test.import_test
print(package_test.import_test.my_value)
import package_test.import_test as test
print(test.my_value)
'''
'''
from package_test import import_test
print(import_test.my_value)
from package_test import import_test as test
print(test.my_value)
'''
