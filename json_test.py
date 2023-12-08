import json
import os

data_dict = {
  'name': 'River',
  'time': os.times().system,
  'number': 7,
}

data_str = json.dumps(data_dict)
print(data_str) # {"name": "River", "time": 0.015625, "number": 7}

# Transform to b-string (binary string)
data_encoded_str = data_str.encode()
print(data_encoded_str) # b'{"name": "River", "time": 0.015625, "number": 7}'

# Save it to somewhere (eg, database, file, and so on)
# ...

# Load from saved place
data_decoded_str = data_encoded_str.decode()
print(data_decoded_str) # {"name": "River", "time": 0.015625, "number": 7}

loaded_dict = json.loads(data_decoded_str)
print(loaded_dict) # {'name': 'River', 'time': 0.015625, 'number': 7}
print(loaded_dict['name']) # River
print(loaded_dict['time']) # 0.015625
print(loaded_dict['number']) # 7



# Serialization with Pickle - Example 1

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


# Serialization with Pickle - Example 2

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
