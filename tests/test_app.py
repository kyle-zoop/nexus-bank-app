"""
Test version of app.py to isolate import issues
"""
from flask import Flask

print("Creating Flask app...")
app = Flask(__name__)
print("Flask app created successfully:", app)

@app.route('/')
def test():
    return "Test works"

print("App definition complete")
