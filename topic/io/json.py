# json (JavaScript Object Notation)

'''
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
'''
