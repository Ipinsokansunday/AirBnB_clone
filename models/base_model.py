#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        timestamp_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    if kwargs:
        for k, v in kwargs.items():
            if k in ("created_at", "updated_at"):
                setattr(self, k, datetime.strptime(v, timestamp_format))
            else:
                setattr(self, k, v)
    else:
        models.storage.new(self)

def save(self):
    """Update updated_at with the current datetime and save to storage."""
    self.updated_at = datetime.today()
    models.storage.save()

def to_dict(self):
    """Return a dictionary representation of the BaseModel instance."""
    result_dict = self.__dict__.copy()
    result_dict["created_at"] = self.created_at.isoformat()
    result_dict["updated_at"] = self.updated_at.isoformat()
    result_dict["__class__"] = self.__class__.__name__
    return result_dict

def __str__(self):
    """Return a string representation of the BaseModel instance."""
    class_name = self.__class__.__name__
    return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
