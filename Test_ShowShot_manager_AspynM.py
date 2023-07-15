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
TEST_SHOT_NAME= "01_A"

class TestTemplate(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = TEST_TEMP_DIR_PATH
        os.mkdir(self.temp_dir)

        self.show_dir=TEST_SHOW_DIR_PATH
        self.shot_dir=TEST_SHOT_DIR_PATH

        # Create an instance of Show and Shot classes
        self.show = Show("FilmTitle",1000,"Done",self.show_dir)
        self.shot = Shot("01_B", 30, "Completed", self.shot_dir)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(TEST_TEMP_DIR_PATH+TEST_TEMP_NAME)

    def test_make_directory(self):
        # Test making a new directory
        new_dir = os.path.join(self.temp_dir, "NewDirectory")
        self.show.make_directory(TEST_SHOT_DIR_PATH, TEST_SHOT_NAME)
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
