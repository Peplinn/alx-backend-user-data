#!/usr/bin/env python3
"""
UserSession model to store session data persistently
"""

from models.base import Base


class UserSession(Base):
    """
    UserSession model to represent a user's session.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
