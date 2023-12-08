# Pipe
'''
Communication between threads.

TODO: Let's work more on this subject later. Maybe there is something about it on superfastpython.com
'''



import threading
import time
import os



# Anonymous
# Communication between threads created instantly, and destroyed on terminate the program execution.

'''
def child(pipeout):
  zzz = 0
  while True:
    time.sleep(zzz)
    os.write(pipeout, f'Spam {zzz:2d}'.encode()) # Write line as binary
    zzz = (zzz + 1) % 5 # 0, 1, 2, 3, 4, 0, 1, 2, ...

def parent(pipein):
  while True:
    line = os.read(pipein, 32)
    print(f'Parent {os.getpid()} received the message [{line}] at {time.time()}')

pipein, pipeout = os.pipe()
threading.Thread(target=child, args=(pipeout,)).start()
parent(pipein)
'''



# Named
# Communication between threads using a file.

'''
'''
