from .default import *

try:
    from .local import *
except ImportError:
    print("Warning: local settings file not found")
