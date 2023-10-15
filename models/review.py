#!/usr/bin/python3
"""Define the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
"""Represente un review
   Initialization:
        place_id (str): id of the place.
        user_id (str): Id of the user.
        text (str):text of the review.
"""


    place_id = ""
    user_id = ""
    text = ""
