import os
from cryptography.fernet import Fernet

root_path = f'www'
website_path = f'{root_path}\\website'



def singleton(cls):
  new = cls.__new__
  instance = None

  def __new__(cls, *args, **kwargs):
    nonlocal instance
    if instance is None:
      instance = new(cls, *args, **kwargs)
    return instance

  cls.__new__ = __new__
  return cls



# Encrypt

# This file shall have root-only access.
fernet_key_filepath = f'{website_path}\\secret.key'

# Generate a key every single time this lib file loads.
with open(fernet_key_filepath, 'wb') as file:
  file.write(Fernet.generate_key())

def get_fernet_key():
  '''
  Loads and returns the secret key.
  CAUTION: Don't store it in any place, only in local variables.
  '''
  return open(fernet_key_filepath, 'rb').read()

def encrypt(message: str) -> bytes:
  return Fernet(get_fernet_key()).encrypt(message.encode())

def decrypt(token: bytes) -> str:
  return Fernet(get_fernet_key()).decrypt(token).decode()
