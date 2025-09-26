#!/usr/bin/env python3
"""
User Authentication Module
"""

class UserAuth:
    def __init__(self):
        self.users = {}
    
    def register_user(self, username, password):
        """Register a new user"""
        if username not in self.users:
            self.users[username] = password
            return True
        return False
    
    def authenticate(self, username, password):
        """Authenticate a user"""
        return self.users.get(username) == password
    
    def list_users(self):
        """List all registered users"""
        return list(self.users.keys())