# Serialization with Pickle
# Readmore: https://docs.python.org/3/library/pickle.html
# Readmore: https://www.youtube.com/watch?v=E-OVDyD7v8g&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=79

# It translates almost any object type into a convenient string for storing in a database, and then translates strings back into objects.
# You can use pickle to store non-string variables in a database (while you can use dbm to store strings or bytes).
# In fact, this combination (with dbm) is so common that it's been encapsulated in a module called shelve.

# pickle.dumps() - Serializes an object to a byte string
# pickle.loads() - Unserializes a byte string to an object
'''
import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
print(s) # b'\x80\x04\x95\x0b\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03e.'
t2 = pickle.loads(s)
print(t2) # [1, 2, 3]

# Although the new object has the same value as the old one, it is not (in general) the same object
# It has the same effect as copying the object
print(t1 == t2) # True
print(t1 is t2) # False
'''


# Example 1

'''
import pickle

this_int = 777
this_string = 'Hello, world.'
my_dict_of_lists = {
  'a': [1, 2, 3],
  'b': [4, 5, 6]
}

query_results = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]

with open('pickle_eg_1.txt', 'wb') as fh:  # Serializing
  pickle.dump((this_int, this_string, my_dict_of_lists, query_results), fh)

with open('pickle_eg_1.txt', 'rb') as fh:  # Unserializing
  tuple = pickle.load(fh)

print(tuple[0])  # this_int
print(tuple[1])  # this_string
print(tuple[2])  # my_dict_of_lists
print(tuple[3])  # query_results
'''

# Example 2

'''
import pickle

class MyClass(object):

  def __init__(self, init_value):
    self.value = init_value

  def increment(self):
    self.value += 1


obj = MyClass(5)
obj.increment()
obj.increment()

with open('pickle_eg_2.txt', 'wb') as fh:  # Serializing
  pickle.dump(obj, fh)

with open('pickle_eg_2.txt', 'rb') as fh:  # Unserializing
  # Note: the class MyClass should be visible in here
  # Otherwise, you will get the following error:
    # AttributeError: Can't get attribute 'MyClass' on
    # <module '__main__' from 'D:/River/PycharmProjects/untitled/test.py'>
  unserialized_obj = pickle.load(fh)

print(type(unserialized_obj))  # <class '__main__.MyClass'>
print(unserialized_obj)        # <__main__.MyClass object at 0x04D0E530>
print(unserialized_obj.value)  # 7
'''
