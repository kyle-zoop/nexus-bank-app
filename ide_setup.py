# IDE Configuration Helper
# This file helps IDEs understand the module structure

# If running in an IDE, add src to path
import sys
import os
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(current_dir, 'src')
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
except:
    pass
