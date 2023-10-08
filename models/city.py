#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """City class to represent cities."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""

    def __str__(self):
        return "[{}] ({}) {} - {}".format(
                self.__class__.__name__, self.id, self.name, self.state_id
        )
