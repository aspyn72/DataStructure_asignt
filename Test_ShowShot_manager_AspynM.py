import unittest
import os
import shutil
from json import load
import json
from ShowShot_manager_AspynM import Show, Shot


class TemplateTest(unittest.TestCase):
    def setUp(self):
        self.show = Show("Mimic", 60, "InProgress", "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/")
        self.shot = Shot("01_B", 30, "Completed", "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/Show_Shot_DB/Mimic/")

    def tearDown(self):
        # Clean up the created directories and files
        self.show.delete_directory(self.show.path, self.show.name)
        self.shot.delete_directory(self.shot.path, self.shot.name)

    def test_make_directory(self):
        # Test creating a directory
        self.show.make_directory(self.show.path, self.show.name)
        self.assertTrue(os.path.exists(self.show.path))

    def test_create_and_get_all_info(self):
        # Test creating a show and getting all information
        self.show.make_directory(self.show.path, self.show.name)
        self.show.create(self.show.name, self.show.duration, self.show.status, self.show.path, "show_db.json")
        self.show.get_all_info(self.show.path, "show_db.json")

        with open(self.show.path + "show_db.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], self.show.name)
            self.assertEqual(data[0]["Time Duration"], self.show.duration)
            self.assertEqual(data[0]["Status"], self.show.status)

    def test_get_single_info(self):
        # Test getting information for a specific show
        self.show.make_directory(self.show.path, self.show.name)
        self.show.create(self.show.name, self.show.duration, self.show.status, self.show.path, "show_db.json")
        self.show.get_single_info(self.show.name, self.show.path, "show_db.json")

        with open(self.show.path + "show_db.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], self.show.name)
            self.assertEqual(data[0]["Time Duration"], self.show.duration)
            self.assertEqual(data[0]["Status"], self.show.status)

    def test_edit_name(self):
        # Test editing the name of a show
        self.show.make_directory(self.show.path, self.show.name)
        self.show.create(self.show.name, self.show.duration, self.show.status, self.show.path, "show_db.json")
        self.show.edit_name(self.show.path, "show_db.json", self.show.name, "New Name")

        with open(self.show.path + "show_db.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "New Name")

    def test_delete(self):
        # Test deleting a show
        self.show.make_directory(self.show.path, self.show.name)
        self.show.create(self.show.name, self.show.duration, self.show.status, self.show.path, "show_db.json")
        self.show.delete(self.show.name, self.show.path, "show_db.json")

        with open(self.show.path + "show_db.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 0)

class ShowTest(unittest.TestCase):
    def setUp(self):
        self.show = Show("Mimic", 60, "InProgress", "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/")

    def tearDown(self):
        self.show.delete_directory(self.show.path, self.show.name)

    def test_make_directory(self):
        self.show.make_directory(self.show.path, self.show.name)
        self.assertTrue(os.path.exists(self.show.path))

class ShotTest(unittest.TestCase):
    def setUp(self):
        self.shot = Shot("01_B", 30, "Completed", "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/Show_Shot_DB/Mimic/")

    def tearDown(self):
        self.shot.delete_directory(self.shot.path, self.shot.name)

    def test_make_directory(self):
        self.shot.make_directory(self.shot.path, self.shot.name)
        self.assertTrue(os.path.exists(self.shot.path))

if __name__ == '__main__':
    unittest.main()
