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
    # For production deployment, use environment variables
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
