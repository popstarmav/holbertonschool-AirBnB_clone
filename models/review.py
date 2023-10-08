#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class to represent user reviews for places."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.text
        )
