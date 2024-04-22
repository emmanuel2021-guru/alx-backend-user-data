#!/usr/bin/env python3

"""
Template for authentication system
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Template for all authentication sytem to be implemented
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if auth is required
        """
        if type(path) is str and path[-1] != '/':
            path = path + '/'
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """ define the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns the current user
        """
        return None
