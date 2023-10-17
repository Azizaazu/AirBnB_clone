#!/usr/bin/python3

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"show BaseModel {obj_id}")
                output = f.getvalue().strip()
                self.assertTrue(len(output) > 0)

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"update BaseModel {obj_id} name 'NewName'")
                HBNBCommand().onecmd(f"show BaseModel {obj_id}")
                output = f.getvalue().strip()
                self.assertTrue("NewName" in output)

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

if __name__ == '__main__':
    unittest.main()
