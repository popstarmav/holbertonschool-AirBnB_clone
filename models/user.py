from models.base_model import BaseModel


class User(BaseModel):
    """User class to represent users."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        return "[{}] ({}) {} {}".format(
            self.__class__.__name__, self.id, self.first_name, self.last_name
        )
