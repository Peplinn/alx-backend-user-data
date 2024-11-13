#!/usr/bin/env python3
""" Authentication Class
"""
from flask import request
from typing import List, TypeVar


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True

        checked_path = path.rstrip('/')
        checked_excl_path = [p.rstrip('/') for p in excluded_paths]

        if checked_path not in checked_excl_path:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        return None
