"""
Pytest configuration and fixtures for the fake bank tests
"""

import sys
import os

# Add the src directory to Python path for testing
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
