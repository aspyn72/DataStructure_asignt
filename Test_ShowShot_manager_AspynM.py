import unittest
import os
import shutil
from json import load
from ShowShot_manager_AspynM import *

TEST_TEMP_DIR_PATH = "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/Real_Test/"
TEST_TEMP_NAME = "Show_Shot_DB" 
    # need to put show folder name here to avoid putting the path manually
TEST_SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
TEST_SHOW_NAME = "Mimic"
    # need to put shot folder name here to avoid putting the path manually
TEST_SHOT_DIR_PATH = SHOW_DIR_PATH + SHOW_NAME + "/"
TEST_SHOT_NAME= "01_B"

class TestTemplate(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = Master_dir
        os.mkdir(self.temp_dir)

        # Create an instance of Show and Shot classes
        self.show = Show("FilmTitle",1000,"Done",self.temp_dir)
        self.shot = Shot("01_B", 30, "Completed", self.temp_dir)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

    def test_make_directory(self):
        # Test making a new directory
        new_dir = os.path.join(self.temp_dir, "NewDirectory")
        self.show.make_directory(self.temp_dir, "NewDirectory")
        self.assertTrue(os.path.exists(new_dir))

        # Test making a directory that already exists
        self.show.make_directory(self.temp_dir, "NewDirectory")
        self.assertTrue(os.path.exists(new_dir))

    def test_delete_directory(self):
        # Test deleting an existing directory
        self.show.make_directory(self.temp_dir, "ToDelete")
        self.show.delete_directory(self.temp_dir, "ToDelete")
        self.assertFalse(os.path.exists(os.path.join(self.temp_dir, "ToDelete")))

        # Test deleting a non-existing directory
        non_existing_dir = os.path.join(self.temp_dir, "NonExisting")
        self.show.delete_directory(self.temp_dir, "NonExisting")
        self.assertFalse(os.path.exists(non_existing_dir))

    def test_create_and_delete(self):
        # Test creating a new entry in .json file
        self.show.create("Mimic", 120, "In Progress", self.temp_dir, "show.json")
        with open(os.path.join(self.temp_dir, "show.json")) as file:
            data = load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "Mimic")

        # Test deleting an entry from .json file
        self.show.delete("Mimic", self.temp_dir, "show.json")
        with open(os.path.join(self.temp_dir, "show.json")) as file:
            data = load(file)
            self.assertEqual(len(data), 0)

    def test_edit_name(self):
        # Test editing the name of an entry in .json file
        self.show.create("Mimic", 120, "In Progress", self.temp_dir, "show.json")
        self.show.edit_name(self.temp_dir, "show.json", "Mimic", "New Name")
        with open(os.path.join(self.temp_dir, "show.json")) as file:
            data = load(file)
            self.assertEqual(data[0]["Name"], "New Name")

    # Add more tests for other methods as needed

if __name__ == "__main__":
    unittest.main()
