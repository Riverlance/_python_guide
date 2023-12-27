# Assert

# Base
'''
def foo(boolean):
  assert boolean == True

foo(False) # AssertionError
'''

# With custom message
'''
def foo(boolean):
  assert boolean == True, 'Custom error message'

foo(False) # AssertionError: Custom error message
'''


# Exception

# Without finally keyword
'''
def foo():
  try:
    print(1)
  except:
    print(2)
  # Finally makes no sense since neither try or except returns anything
  # finally:
  #   print(3)
  print(4)
foo() # 1 4
'''

# With finally keyword
'''
def foo():
  try:
    print(1)
    return True
  except:
    print(2)
    return False
  finally:
    print(3)
  # print(4) # Unreachable code
foo() # 1 3
'''



# Raise

'''
def foo(raise_error):
  if raise_error:
    raise ValueError('This is a value error message')
'''

# Nothing happens
'''
foo(False)
'''

# Raise ValueError
'''
foo(True) # ValueError
'''

# Catch ValueError
'''
try:
  foo(True)
except ValueError:
  print('Catch ValueError') # Catch ValueError
'''

# Catch ValueError with message
'''
try:
  foo(True)
except ValueError as e:
  print(e) # This is a value error message
'''

# exec_info
# Gets a tuple of info about the last raised exception
# Useful for exceptions
'''
import sys
try:
  raise IndexError
except IndexError:
  print(sys.exc_info()) # (<class 'IndexError'>, IndexError(), <traceback object at 0x0000016E6F732800>)
'''

# Catch multiple exceptions
'''
import sys
try:
  raise IndexError
except IndexError:
  print(sys.exc_info()) # (<class 'IndexError'>, IndexError(), <traceback object at 0x0000016E6F732800>)
except ValueError:
  print(sys.exc_info()) # (<class 'ValueError'>, ValueError(), <traceback object at 0x000002032B233300>)
'''

# Catch multiple exceptions at once
'''
import sys
try:
  raise ValueError
except (IndexError, ValueError):
  print(sys.exc_info()) # (<class 'ValueError'>, ValueError(), <traceback object at 0x000002032B233300>)
'''



# Own class

class MyException(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
    size = len(self.args)
    self.__my_message = self.args[0] if size > 0 else 'This is the default error message'
    self.__my_value = self.args[1] if size > 1 else 0

  def __str__(self):
    return f'Message: {self.__my_message} | Custom value: {self.__my_value}'

# Default error message
'''
def foo():
  raise MyException()

try:
  foo()
except MyException as e:
  print(e) # Message: This is the default error message | Custom value: 0
'''

# Custom error message
'''
def foo():
  raise MyException('Custom error message', 7)

try:
  foo()
except MyException as e:
  print(e) # Message: Custom error message | Custom value: 7
'''
