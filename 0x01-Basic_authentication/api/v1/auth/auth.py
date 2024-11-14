#!/usr/bin/env python3
""" Authentication Class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """_summary_
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
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

        return True

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
                request (_type_, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return None
