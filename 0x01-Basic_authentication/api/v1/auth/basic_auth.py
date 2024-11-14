#!/usr/bin/env python3
""" Authentication Class
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """_summary_
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """_summary_

        Args:
                authorization_header (List[str]): _description_

        Returns:
                bool: _description_
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Return the part after "Basic " (i.e., after the space)
        return authorization_header.split(" ", 1)[1]
