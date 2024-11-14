#!/usr/bin/env python3
"""
Module for session expiration-based authentication
"""

import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth class that manages session expiration.
    """
    def __init__(self):
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_info = {
            "user_id": user_id,
            "created_at": datetime.now().strftime(TIMESTAMP_FORMAT)
        }
        self.user_id_by_session_id[session_id] = session_info
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """_summary_

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if session_id is None or session_id not in self.user_id_by_session_id:
            return None

        session_data = self.user_id_by_session_id.get(session_id)
        if session_data is None:
            return None

        if self.session_duration <= 0:
            return session_data.get("user_id")

        created_at = session_data.get("created_at")
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if datetime.now() > expiration_time:
            return None

        return session_data.get("user_id")
