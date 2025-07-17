#!/usr/bin/env python3
"""
Main entry point for the Fake Bank Application
Run this file to start the Flask server
"""

import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from bank.app import app

if __name__ == '__main__':
    app.run(debug=True, port=5000)
