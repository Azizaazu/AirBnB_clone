#!/usr/bin/python3
""" Define the user class """
from models.base_model import BaseModel
""" represente un utilisateur
les attributs :
    email(str): l'email de user
    password(str): password de user
    first_name(str): le prénom de user
    last_name (str): le nom de user
"""

class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
