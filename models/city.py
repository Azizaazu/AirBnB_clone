#!/usr/bin/python3
"""Define the City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a city

    Attributs:
        state_id (str): Id of the state.
        name (str): The city's name.
    """

    state_id = ""
    name = ""
