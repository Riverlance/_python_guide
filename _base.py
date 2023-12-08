# Todo
'''
MySql
https://www.youtube.com/playlist?list=PLzMcBGfZo4-l5kVSNVKGO60V6RkXAVtp-

PostgreSQL

Unit test - TestCase / Mock / Stubs
Multi thread



Later:

- cx_freeze (transforma um código python em executável): https://www.lfd.uci.edu/~gohlke/pythonlibs/

Aulas Python - 086 - Iteração VII: Próprios Objetos Iteráveis
https://www.youtube.com/watch?v=mBebI97CMLw&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=87

Aulas Python - 114 - Ferramentas de Sistema X: Módulo subprocess
https://www.youtube.com/watch?v=jgmIUa2_wSY&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=115

Aulas Python - 115 - Ferramentas de Sistema XI: Módulo argparse
https://www.youtube.com/watch?v=HBwMGVBLw_0&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=116

Readmore: https://docs.python.org/pt-br/3/tutorial/index.html
'''

# Useful imports
'''
import dbm # Local file database ( https://www.youtube.com/watch?v=pHIRd7u3YS0&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=78 )
import pickle # Semelhante ao json, porém armazena também objetos facilmente ( https://www.youtube.com/watch?v=E-OVDyD7v8g&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=79 )
import shelve # Usa o pickle e dbm para armazenar objetos facilmente ( https://www.youtube.com/watch?v=jZpjyeDbQxI&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=80 )
'''



# PDB (debugger)

# Aulas Python - 073 - Debugando programas usando o pdb
# https://www.youtube.com/watch?v=XeEYs0KYzGE&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=74



# Value

# Right-click on file > Open in Integrated Terminal > Type "py .\test.py" > Enter
# You can use `python.exe`, `python` or `py` on terminal.
# You can open the terminal with the shortcut `Ctrl+"`.

'''
print(.7) # 0.7
print(1000000) # 1000000
print(1_000_000) # 1000000

print("Hello, world.")

# string format
foo = 7
print(f"foo = {foo}")

# float division
print(5 / 2) # 2.5
# integer division (ignores value after `.`)
print(5 // 2) # 2
# same as above
import math
print(math.floor(5 / 2))
'''
'''
print(1 < 3 < 5) # True
print(1 < 3 < 2) # False
'''
'''
x = 7
print(x)
del x
# print(x) # NameError: name 'x' is not defined
'''
'''
# print(7) print(8) # Statements must be separated by newlines or semicolons
print(7); print(8) # 7 8
'''



# Input

'''
name = input('Type your name: ')
print(f'Hello, {name}')
'''
'''
x = y = z = 7
print(x, y, z)
'''



# Type

'''
a = 7
b = int(7)
c = 7.0
d = float(7)
e = '7'
print(type(a), type(b), type(c), type(d), type(e))
'''
'''
# print('Number: ' + 7) # TypeError: can only concatenate str (not "int") to str
print('Number: ' + str(7)) # Solution
'''



# Random

'''
import random
print(random.randint(3,7)) # Numbers between 3 to 7
'''



# Enum

'''
flags = ['red', 'blue', 'green']

print(list(enumerate(flags))) # [(0, 'red'), (1, 'blue'), (2, 'green')]
print(tuple(enumerate(flags))) # ((0, 'red'), (1, 'blue'), (2, 'green'))
flags_dict = dict(enumerate(flags))
print(flags_dict) # {0: 'red', 1: 'blue', 2: 'green'}
print({v: k for k, v in flags_dict.items()}) # {'red': 0, 'blue': 1, 'green': 2}
'''



# Bit

'''
# Binary
print(bin(7)) # 0b111
print(0b111) # 7
print(int('0b111', 2)) # 7

# Octal
print(oct(7007)) # 0o15537
print(0o15537) # 7007
print(int('0o15537', 8)) # 7007

# Hex
print(hex(7007)) # 0x1b5f
print(0x1b5f) # 7007
print(int('0x1b5f', 16)) # 7007

# Bitwise

print(bin(0b010 << 1)) # 0b100
print(bin(0b010 >> 1)) # 0b1
print(bin(0b00100010 << 1)) # 0b1000100
print(bin(0b00100010 >> 1)) # 0b10001
print(16 << 1) # 32
print(16 << 2) # 64
print(16 << 3) # 128
print(bin(0b1010 & 0b1100)) # 0b1000 (only if both are 1)
print(bin(0b1010 | 0b0100)) # 0b1110 (if any are 1)
print(bin(0b1010 ^ 0b0010)) # 0b1000 (if they are different - 1 and the other 0 or vice versa)
'''










# Main file execution

'''
def main():
  print('Main file')
if __name__ == '__main__': # Main file
  main()
'''
