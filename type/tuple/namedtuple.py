from collections import namedtuple

# Named tuple

# Base

'''
nt_1 = namedtuple('Point', 'x y')
nt_2 = namedtuple('Point', 'x, y')
nt_3 = namedtuple('Point', ['x', 'y'])
print(nt_1, nt_2, nt_3) # <class '__main__.Point'> <class '__main__.Point'> <class '__main__.Point'>

nt_1_instance_1 = nt_1(7, 8)
print(nt_1_instance_1) # Point(x=7, y=8)
nt_1_instance_2 = nt_1(x=7, y=8)
print(nt_1_instance_2) # Point(x=7, y=8)
nt_1_instance_3 = nt_1(y=8, x=7)
print(nt_1_instance_3) # Point(x=7, y=8)

print(nt_1_instance_1.x, nt_1_instance_1[0]) # 7 7
print(nt_1_instance_1.y, nt_1_instance_1[1]) # 8 8
'''



# Variable names cannot starts with underscore ('_') and cannot be a reserved keyword (like int, if, def, for...).
# You can avoid issues with the mentioned above if you set rename=True.

'''
nt_1 = namedtuple('Func', 'def', rename=True) # Def is reserved keyword
nt_1_instance = nt_1(7)
print(nt_1_instance[0]) # 7
# This is not recommended though, because you still cannot use like below:
# print(nt_1_instance.def) # SyntaxError: invalid syntax
'''
