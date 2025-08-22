# dbm (local database file, key-value store)
# Readmore: https://docs.python.org/3/library/dbm.html
# Readmore: https://www.youtube.com/watch?v=pHIRd7u3YS0&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe&index=78

# One limitation of dbm is that keys and values must be strings or bytes.
# If you try to use any other type, you'll get an error.
# The pickle module can help.
# It translates almost any object type into a convenient string for storing in a database, and then translates strings back into objects.

'''
import dbm

db = dbm.open('../../data/assets/captions.db', 'c') # 'c' means create if not exists

db['cleese.png'] = 'Photo of John Cleese.' # Store a string and save it to the database file
print(db['cleese.png']) # b'Photo of John Cleese.' # Get the value of the key 'cleese.png'

db['cleese.png'] = 'Photo of John Cleese doing a silly walk.' # Update the value of the key 'cleese.png'
print(db['cleese.png']) # b'Photo of John Cleese doing a silly walk.'

for key in db: # Iterate through the keys in the database
  print(key, db[key])

db.close() # Close the database file
'''
