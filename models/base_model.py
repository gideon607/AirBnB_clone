#!/usr/bin/python3
"""
BaseModel - Main Module
BaseModel Main parent class.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class main parent class for intial, 
    serialization and also deserialzation of several instances.
    """
    def __int__(self, *args, **kwargs):
        """ INtialization of BaseModel instance"""
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """String rep of a BaseModel instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Returns string rep of the BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates 'updated_at' instance with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary rep of the BaseModel class."""
        now_dit = dict(self.__dict__)
        now_dit['__class__'] = self.__class__.__name__
        now_dit['created_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        now_dit['updated_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (now_dit)



