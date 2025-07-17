#!/usr/bin/env python3
"""
Test script to verify the modular structure works correctly
"""

import sys
import os

# Add the src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.insert(0, src_dir)

#!/usr/bin/env python3
"""
Test script to verify the modular structure works correctly
"""

import sys
import os

# Add the src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.insert(0, src_dir)

#!/usr/bin/env python3
"""
Test script to verify the modular structure works correctly
"""

import sys
import os

# Add the src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
src_dir = os.path.join(parent_dir, 'src')
sys.path.insert(0, src_dir)

# Import modules - IDE warnings are expected but code works perfectly
try:
    from bank.user_data import FAKE_ACCOUNTS  # type: ignore
    from bank.auth import is_account_locked, trigger_account_lockout  # type: ignore
    from bank.config import BLACKLISTED_2FA_CODES  # type: ignore
    IMPORTS_SUCCESSFUL = True
except ImportError as e:
    print(f"❌ Import error: {e}")
    print(f"Python path: {sys.path}")
    IMPORTS_SUCCESSFUL = False

def test_structure():
    print("🧪 Testing Modular Structure")
    print("=" * 40)
    
    if not IMPORTS_SUCCESSFUL:
        print("❌ Failed to import modules - structure test failed!")
        return False
    
    print("✅ All imports successful!")
    
    # Test user data import
    print(f"✅ User accounts loaded: {len(FAKE_ACCOUNTS)} users")
    for username in FAKE_ACCOUNTS:
        print(f"   - {username}: {FAKE_ACCOUNTS[username]['name']}")
    
    # Test auth functions
    print(f"✅ Auth functions available")
    print(f"   - Lockout check for 'demo123': {is_account_locked('demo123')}")
    
    # Test config import
    print(f"✅ Config loaded: {len(BLACKLISTED_2FA_CODES)} blacklisted codes")
    
    print("\n🎯 Modular structure working correctly!")
    return True

if __name__ == '__main__':
    success = test_structure()
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Tests failed!")
        sys.exit(1)
