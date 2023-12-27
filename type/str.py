# Change the charset of this whole file
# -*- coding utf-8 -*-
# -*- coding cp1252 -*-
# Charset 'Western (Windows 1252)' of VS Code is encoding 'cp1252' on Python

import sys



# String

string = 'ABC abc'

# Base
'''
print('a' 'b' 'c') # abc
print('a' + string) # aABC abc
print(str(7.89)) # 7.89

for char in string:
  print(char) # A B C   a b c

print(ord('A'), ord('B'), ord('C')) # 65 66 67
print(chr(65), chr(66), chr(67)) # A B C

print('A' < 'B') # True
'''

# Generic formatting
'''
print('x(%d) + y(%d) = z(%d)'%(5, 2, 5 + 2))
print('x(%f) + y(%f) = z(%f)'%(5.21, 2.11, 5.21 + 2.11))
print('x(%.1f) + y(%.1f) = z(%.2f)'%(5.21, 2.11, 5.21 + 2.11))
print()
print('x(%(x)d) + y(%(y)d) = z(%(z)d)'%{'x': 5, 'y': 2, 'z': 5 + 2})
print('x(%(x)f) + y(%(y)f) = z(%(z)f)'%{'x': 5.21, 'y': 2.11, 'z': 5.21 + 2.11})
print('x(%(x).1f) + y(%(y).1f) = z(%(z).2f)'%{'x': 5.21, 'y' :2.11, 'z': 5.21 + 2.11})
'''
'''
print('x({0}) + y({1}) = z({2})'.format(5, 2, 5 + 2))
print('x({0}) + y({1}) = z({2})'.format(5.21, 2.11, 5.21 + 2.11))
print('x({0}) + y({2}) = z({1})'.format(5.21, 5.21 + 2.11, 2.11))
print()
print('x({x}) + y({y}) = z({z})'.format(x = 5, y = 2, z = 5 + 2))
print('x({x}) + y({y}) = z({z})'.format(x = 5.21, y = 2.11, z = 5.21 + 2.11))
print('x({x}) + y({y}) = z({z})'.format(x = 5.21, z = 5.21 + 2.11, y = 2.11))
print()
print('x({x}) + y({y}) = z({0})'.format(5 + 2, x = 5, y = 2))
print()
print('x(%2s) + y(%2s) = z(%2s)'%(str(5), str(7), str(5 + 7)))
print('x(%4s) + y(%4s) = z(%4s)'%(str(5.1), str(7.2), str(5.1 + 7.2)))
print()
print('{0:.2f}, {1}, {2}'.format(7.1, 8.2, 9.3))
print('{0[0]}, {0[1]}, {0[2]}, {1}'.format((7, 8, 9), 10))
print('{0:10} = {1:10}'.format('spam', 987.6543))
print('{0:>10} = {1:<10}'.format('spam', 987.6543))
print('{0[kind]:>10} = {1.platform:<10}'.format(dict(kind='desktop'), sys))
'''

# f-string (format string) - Best formatting (except by the > or < )
'''
print(f'My var: {string}') # My var: ABC abc
print('My var: %s'%(string)) # My var: ABC abc

print(f'My var: {7}') # My var: 7
print('My var: %d'%(7)) # My var: 7

print(f'My var: {7.8:.2f}') # My var: 7.80
print('My var: %.2f'%(7.8)) # My var: 7.80

print(f'x({7}) + y({8}) = z({7+8})') # x(7) + y(8) = z(15)
print('x(%d) + y(%d) = z(%d)'%(7, 8, 7+8)) #  # x(7) + y(8) = z(15)
'''

# r-string (raw string)
# It ignores slash special characters.
'''
print('\\') # \
print(r'\\') # \\
'''

# b-string (binary string)
'''
ws = 'Word'
wb = b'Word'
wb2 = ws.encode()
print(ws[0], wb[0], wb2[0], wb2.decode()[0]) # W 87 87 W
'''

# u-string (ascii format)
'''
print(u'Ol\u00e1') # Olá
print(r'Ol\u00e1') # Ol\u00e1
print('Ol\u00e1'.encode('utf-8')) # b'Ol\xc3\xa1'
print('Ol\u00e1'.encode('latin-1')) # b'Ol\xe1'
'''

# repr
'''
print('a\tb') # a       b
print(repr('a\tb')) # 'a\tb'
'''

# Duplicate string
'''
print(string * 3) # ABC abcABC abcABC abc
print(string.capitalize()) # Abc abc
print(string.title()) # Abc Abc
print(string.lower()) # abc abc
print(string.upper()) # ABC ABC
print('{}, {}.'.format('Hello', 'world'))
print('HELLO'.islower()) # False
print('HELLO'.isupper()) # True
'''

# Edit string
'''
str_list = list(string)
print(str_list) # ['A', 'B', 'C', ' ', 'a', 'b', 'c']
str_list[0] = 'X'
print('-'.join(str_list)) # X-B-C- -a-b-c
str_list = ''.join(str_list)
print(str_list) # XBC abc
'''
