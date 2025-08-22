# Make module_example.py availble for importing directly from the module package
# (you can use `import module`, instead of something like `import module.module_example` or `from module import module_example`)
from . import module_example

# Make all submodules availble for importing them directly from the module package
'''
import importlib, pkgutil

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
  globals()[name] = importlib.import_module(f".{name}", __name__)
'''

print("Loading package 'lib'...")
