#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city with state_id and name attributes."""
    state_id = ""
    name = ""
