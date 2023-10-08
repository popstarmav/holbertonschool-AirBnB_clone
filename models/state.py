#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """State class to represent states or regions."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.name
        )
