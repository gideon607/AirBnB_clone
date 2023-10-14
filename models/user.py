#!/usr/bin/python3
"""Module that creates the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing the users objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

