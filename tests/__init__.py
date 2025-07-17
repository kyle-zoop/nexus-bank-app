"""
Test package for the fake bank application
Sets up import paths for IDE compatibility
"""

import sys
import os

# Set up the import path for all test modules
_current_dir = os.path.dirname(os.path.abspath(__file__))
_parent_dir = os.path.dirname(_current_dir)
_src_dir = os.path.join(_parent_dir, 'src')

if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)
