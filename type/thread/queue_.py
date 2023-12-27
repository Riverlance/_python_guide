# Queue
'''
Like a list, but as FIFO (first in, first out)
Uses a thread-lock, so you can use multi-threading with it safely

To use lists as thread-safe, you need to use threading.Condition object (which is already implemented in queue.Queue).

Queue does not support peek.
A peek operation allows a consumer to check what the next retrieved value will be without removing it.
'''



import queue
import threading
import time
import random

safeprint_lock = threading.Lock()



# Limitless queue size (stops as soon as queue is empty)
'''
Base example.
'''

'''
count_producers = 4
count_messages = 2
count_clients = 2

task_items_queue = queue.Queue(maxsize=0) # Limitless queue

# Each producer will create count_messages
# count_producers * count_messages = total created messages (tasks to do)
def producer_act(thread_id):
  # with safeprint_lock: print(f'Producer {thread_id} started')

  for msg_id in range(count_messages):
    # Simulates a random small time required for the message to be created
    time.sleep(random.random())

    # Push item
    task_items_queue.put(f'[Message id {msg_id} created by producer id {thread_id}]')

  # with safeprint_lock: print(f'Producer {thread_id} done')

# Each client will consume each created message
def client_act(thread_id):
  # with safeprint_lock: print(f'Client {thread_id} started')

  while True:
    # Pop item
    item = task_items_queue.get()

    with safeprint_lock: print(f'[Client id {thread_id}] received: {item}')

    # Once complete, the thread may then call the task_done() method on the queue
    # to indicate that the item that was just retrieved has been completely processed.
    task_items_queue.task_done() # Mark the task as completed

    with safeprint_lock: print(f'Client {thread_id} done')

# Create the threads
# Thread.daemon=True is to finish the thread execution when the main thread terminates.
client_threads = [threading.Thread(target=client_act, args=(thread_id,), daemon=True) for thread_id in range(count_clients)]
producer_threads = [threading.Thread(target=producer_act, args=(thread_id,)) for thread_id in range(count_producers)]

# Start clients
for thread in client_threads:
  thread.start()

# Start producers
for thread in producer_threads:
  thread.start()

# Wait for producers to finish
for thread in producer_threads:
  thread.join()

# Wait for all clients to consume all items (tasks on the queue to be marked as done)
# If it is called after all tasks have been marked done, then the function will return immediately (not this case).
# Note: Producer threads terminates by themselves, but client threads terminates only if main thread terminates (daemon = True).
task_items_queue.join()

# The Python process will exit once all non-daemon threads have terminated,
# including the producer threads and the main thread, but not the client threads.
# It means, once the producer threads and the main thread are done, the client threads are abrupt terminated.
with safeprint_lock: print('Leaving main thread.')
'''



# Without blocking (if empty, throw queue.Empty and wait a bit to try again)
'''
This might be useful if we wish:
- To use busy waiting in the client task to check other states; or
- To perform other tasks in the client while waiting for data to arrive on the queue.

Busy waiting, also called spinning, refers to a thread that "waits" (sleep) while repeatedly checking for a condition in a loop.
'''

'''
count_producers = 4
count_messages = 2
count_clients = 2

task_items_queue = queue.Queue(maxsize=0) # Limitless queue

# Each producer will create count_messages
# count_producers * count_messages = total created messages (tasks to do)
def producer_act(thread_id):
  # with safeprint_lock: print(f'Producer {thread_id} started')

  for msg_id in range(count_messages):
    # Simulates a random small time required for the message to be created
    time.sleep(random.random())

    # Push item
    task_items_queue.put(f'[Message id {msg_id} created by producer id {thread_id}]')

  # with safeprint_lock: print(f'Producer {thread_id} done')

# Each client will consume each created message
def client_act(thread_id):
  # with safeprint_lock: print(f'Client {thread_id} started')

  while True:
    try:
      # Pop item
      item = task_items_queue.get(block=False)
    except queue.Empty:
      with safeprint_lock: print(f'[Client id {thread_id}]: Queue is empty. Waiting a while to try again...')
      time.sleep(0.5)
      continue

    with safeprint_lock: print(f'[Client id {thread_id}] received: {item}')

    # Once complete, the thread may then call the task_done() method on the queue
    # to indicate that the item that was just retrieved has been completely processed.
    task_items_queue.task_done() # Mark the task as completed

    with safeprint_lock: print(f'Client {thread_id} done')

# Create the threads
# Thread.daemon=True is to finish the thread execution when the main thread terminates.
client_threads = [threading.Thread(target=client_act, args=(thread_id,), daemon=True) for thread_id in range(count_clients)]
producer_threads = [threading.Thread(target=producer_act, args=(thread_id,)) for thread_id in range(count_producers)]

# Start clients
for thread in client_threads:
  thread.start()

# Start producers
for thread in producer_threads:
  thread.start()

# Wait for producers to finish
for thread in producer_threads:
  thread.join()

# Wait for all clients to consume all items (tasks on the queue to be marked as done)
# If it is called after all tasks have been marked done, then the function will return immediately (not this case).
# Note: Producer threads terminates by themselves, but client threads terminates only if main thread terminates (daemon = True).
task_items_queue.join()

# The Python process will exit once all non-daemon threads have terminated,
# including the producer threads and the main thread, but not the client threads.
# It means, once the producer threads and the main thread are done, the client threads are abrupt terminated.
with safeprint_lock: print('Leaving main thread.')
'''



# With a timeout (if empty, wait a bit; if still empty, throw queue.Empty and try again)
'''
Similar to example of 'Without blocking'.
In the previous example, if no item is found, then a queue.Empty exception is thrown right away.

In this example, if no item is found, it will wait a time expecting an item to arrive.
Only if the time ends up, then a queue.Empty exception is thrown.
'''

'''
count_producers = 2
count_messages = 2
count_clients = 4

task_items_queue = queue.Queue(maxsize=0) # Limitless queue

# Each producer will create count_messages
# count_producers * count_messages = total created messages (tasks to do)
def producer_act(thread_id):
  # with safeprint_lock: print(f'Producer {thread_id} started')

  for msg_id in range(count_messages):
    # Simulates a random small time required for the message to be created
    time.sleep(random.random())

    # Push item
    task_items_queue.put(f'[Message id {msg_id} created by producer id {thread_id}]')

  # with safeprint_lock: print(f'Producer {thread_id} done')

# Each client will consume each created message
def client_act(thread_id):
  # with safeprint_lock: print(f'Client {thread_id} started')

  while True:
    try:
      # Pop item
      item = task_items_queue.get(timeout=0.5)
    except queue.Empty:
      with safeprint_lock: print(f'[Client id {thread_id}]: Queue is empty for some time. Trying again...')
      continue

    with safeprint_lock: print(f'[Client id {thread_id}] received: {item}')

    # Once complete, the thread may then call the task_done() method on the queue
    # to indicate that the item that was just retrieved has been completely processed.
    task_items_queue.task_done() # Mark the task as completed

    with safeprint_lock: print(f'Client {thread_id} done')

# Create the threads
# Thread.daemon=True is to finish the thread execution when the main thread terminates.
client_threads = [threading.Thread(target=client_act, args=(thread_id,), daemon=True) for thread_id in range(count_clients)]
producer_threads = [threading.Thread(target=producer_act, args=(thread_id,)) for thread_id in range(count_producers)]

# Start clients
for thread in client_threads:
  thread.start()

# Start producers
for thread in producer_threads:
  thread.start()

# Wait for producers to finish
for thread in producer_threads:
  thread.join()

# Wait for all clients to consume all items (tasks on the queue to be marked as done)
# If it is called after all tasks have been marked done, then the function will return immediately (not this case).
# Note: Producer threads terminates by themselves, but client threads terminates only if main thread terminates (daemon = True).
task_items_queue.join()

# The Python process will exit once all non-daemon threads have terminated,
# including the producer threads and the main thread, but not the client threads.
# It means, once the producer threads and the main thread are done, the client threads are abrupt terminated.
with safeprint_lock: print('Leaving main thread.')
'''



# Limited sized (calls to put() will block if full, until a position becomes available)
'''
This can be helpful if we have a large number of producers or slow consumers.
It allows us to limit the number of tasks that may be in memory at any one time,
limiting overall memory usage of the application.
'''

'''
count_producers = 4
count_messages = 2
count_clients = 1

task_items_queue = queue.Queue(maxsize=3)

# Each producer will create count_messages
# count_producers * count_messages = total created messages (tasks to do)
def producer_act(thread_id):
  # with safeprint_lock: print(f'Producer {thread_id} started')

  for msg_id in range(count_messages):
    if task_items_queue.qsize() == task_items_queue.maxsize:
      with safeprint_lock: print(f"Queue is full! Then 'put()' is blocked until a client consumes at least one.")

    # Push item
    task_items_queue.put(f'[Message id {msg_id} created by producer id {thread_id}]')

  # with safeprint_lock: print(f'Producer {thread_id} done')

# Each client will consume each created message
def client_act(thread_id):
  # with safeprint_lock: print(f'Client {thread_id} started')

  while True:
    # Pop item
    item = task_items_queue.get()

    with safeprint_lock: print(f'[Client id {thread_id}] received: {item}')

    # Once complete, the thread may then call the task_done() method on the queue
    # to indicate that the item that was just retrieved has been completely processed.
    task_items_queue.task_done() # Mark the task as completed

    # with safeprint_lock: print(f'Client {thread_id} done')

# Create the threads
# Thread.daemon=True is to finish the thread execution when the main thread terminates.
client_threads = [threading.Thread(target=client_act, args=(thread_id,), daemon=True) for thread_id in range(count_clients)]
producer_threads = [threading.Thread(target=producer_act, args=(thread_id,)) for thread_id in range(count_producers)]

# Start clients
for thread in client_threads:
  thread.start()

# Start producers
for thread in producer_threads:
  thread.start()

# Wait for producers to finish
for thread in producer_threads:
  thread.join()

# Wait for all clients to consume all items (tasks on the queue to be marked as done)
# If it is called after all tasks have been marked done, then the function will return immediately (not this case).
# Note: Producer threads terminates by themselves, but client threads terminates only if main thread terminates (daemon = True).
task_items_queue.join()

# The Python process will exit once all non-daemon threads have terminated,
# including the producer threads and the main thread, but not the client threads.
# It means, once the producer threads and the main thread are done, the client threads are abrupt terminated.
with safeprint_lock: print('Leaving main thread.')
'''
