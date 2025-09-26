#!/usr/bin/env python3
"""
DevOps Demo Application with Authentication
"""

try:
    from auth import UserAuth
except ImportError:
    print("Error: auth module not found!")
    exit(1)

def main():
    print("=" * 50)
    print("DevOps Git Project - Version 1.1")
    print("Now with user authentication!")
    print("=" * 50)
    
    # Create authentication system
    auth = UserAuth()
    
    # Register some test users
    auth.register_user("admin", "password123")
    auth.register_user("user1", "mypassword")
    
    print(f"Registered users: {auth.list_users()}")
    
    # Test authentication
    test_cases = [
        ("admin", "password123"),
        ("admin", "wrongpassword"),
        ("user1", "mypassword"),
        ("nonexistent", "anypassword")
    ]
    
    for username, password in test_cases:
        if auth.authenticate(username, password):
            print(f"✅ Authentication successful for '{username}'")
        else:
            print(f"❌ Authentication failed for '{username}'")
    
    print("=" * 50)
    print("Feature demonstration complete!")

if __name__ == "__main__":
    main()