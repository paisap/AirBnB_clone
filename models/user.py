#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class base_model the base model
of AirBnB who JSON's parent class of the rest and handling
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
