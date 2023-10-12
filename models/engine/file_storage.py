from models.user import User
from models.base_model import BaseModel

class FileStorage:
    # ...
    def all(self, cls=None):
        """Return a dictionary of objects."""
        obj_dict = {}
        if cls:
            for key, value in self.__objects.items():
                if type(value) == cls:
                    obj_dict[key] = value
        else:
            obj_dict = self.__objects
        return obj_dict
