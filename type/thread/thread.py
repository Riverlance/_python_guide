# Thread

# Important: The import _thread is deprecated in Python 3.x, which was a low-level thread module.
# You may want use threading instead, which is a higher-level thread module.

# Creating threads and executing them sequentially
# Note: That's not how you use threads, but it's just an example for understanding about it.

# Readmore: https://superfastpython.com/threading-in-python/

'''
Todo: https://superfastpython.com/asyncio-async-def/
'''

import threading
import time

safeprint_lock = threading.Lock()
def safeprint(*args):
  with safeprint_lock: print(*args)



# First example

# Old way
'''
import _thread

def child(thread_id):
  safeprint(f'Hello from thread id {thread_id}')

def parent():
  id = 0
  while True:
    id += 1
    _thread.start_new_thread(child, (id,))
    if input() in ('q', 'quit'):
      break

parent()
'''

# New way
'''
def child(thread_id):
  safeprint(f'Hello from thread id {thread_id}')

def parent():
  id = 0
  while True:
    id += 1
    t_n = threading.Thread(target=child, args=(id,))
    t_n.start() # Start executing this thread
    # t_n.join() # Wait for this thread to finish before continue the code execution
    if input() in ('q', 'quit'):
      break

parent()
'''



# Threads counting at the same time

'''
def counter(thread_id, count):
  for i in range(1, count + 1):
    safeprint(f'Thread id [{thread_id}] = {i}')
    time.sleep(1)

for thread_id in range(3):
  t_n = threading.Thread(target=counter, args=(thread_id, 7))
  t_n.start()

# Once all threads counts up to 7, on the 8th second it prints this
time.sleep(8)
safeprint('Leaving main thread.')
'''



# Lock (critical section)

'''
lock = threading.Lock()

def counter(thread_id, count):
  for i in range(1, count + 1):
    time.sleep(1)

    # Critical section
    with lock:
      # Only a single thread can execute this escope at a time
      print(f'Thread id [{thread_id}] = {i}')

for thread_id in range(3):
  threading.Thread(target=counter, args=(thread_id, 7)).start()

time.sleep(8)
print('Leaving main thread.')
'''

# Without sleeping
'''
finished = [False] * 10

def counter(thread_id, count):
  for i in range(1, count + 1):
    # Critical section
    with lock:
      # Only a single thread can execute this escope at a time
      print(f'Thread id [{thread_id}] = {i}')
  finished[thread_id] = True

lock = threading.Lock()
for thread_id in range(10):
  threading.Thread(target=counter, args=(thread_id, 100)).start()

# If there is one thread not finished, keep skipping out
while False in finished:
  pass

print('Leaving main thread.')
'''



# Base class model

'''
threads = []
lock = threading.Lock()

class ThreadClass(threading.Thread):
  def __init__(self, thread_id, count, lock):
    self.__id = thread_id
    self.__count = count
    self.__lock = lock
    super().__init__()

  # override the threading.Thread run function
  def run(self):
    for i in range(1, self.__count + 1):
      # Critical section
      with self.__lock:
        # Only a single thread can execute this escope at a time
        print(f'Thread id [{self.__id}] = {i}')

for i in range(10):
  thread = ThreadClass(i, 100, lock)
  thread.start() # Executes run()
  threads.append(thread)

# Wait until the threads terminates
for thread in threads:
  thread.join()

print('Leaving main thread.')
'''
