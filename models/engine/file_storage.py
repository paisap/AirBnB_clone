#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class base_model the base model
of AirBnB who JSON's parent class of the rest and handling
"""
import json
import os.path as path
from models.base_model import BaseModel
import models
from models.user import User


class FileStorage:
    """ class FileStorage where serializes
    instances to a JSON
    file and deserializes JSON file to instances: """
    def __init__(self):
        """ the init class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ new obj """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ save in file .json """
        aux = {}
        with open(self.__file_path, mode='w', encoding='UTF-8') as f:
            for key, value in self.__objects.items():
                aux[key] = value.to_dict()
            f.write(json.dumps(aux))

    def reload(self):
        """
        Deserializes the JSON objects in the JSON file
        to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing.)
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as FILE:
                JSON_objects = json.load(FILE)
                for key, value in sorted(JSON_objects.items()):
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
