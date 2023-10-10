#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User with email,
    password, first_name, and last_name attributes."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
