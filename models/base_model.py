#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class base_model the base model
"""
import uuid
import re
from datetime import date, datetime
import models


class BaseModel:
    """ class BaseModel """
    def __init__(self, *args, **kwargs):
        """ the instance is created """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ the function str to print """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id,
            self.__dict__)

    def save(self):
        """ updates attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ REturn new dict """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
