import unittest
import os
import json
from ShowShot_manager_AspynM import Show, Shot
import shutil

# Define the unit tests
class TestShowShotManagement(unittest.TestCase):

    def setUp(self):
        # Create a test directory for the unit tests
        self.test_dir = "D:\TEST"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Delete the test directory and its contents after the unit tests
        shutil.rmtree(self.test_dir)

    def test_show_creation(self):
        # Create a show instance and check if the show folder is created
        show = Show("ShowTitle", 1000, "Done", self.test_dir)
        show.make_directory(show.path, show.name)
        self.assertTrue(os.path.exists(show.path + show.name))

    def test_shot_creation(self):
        # Create a shot instance and check if the shot folder is created
        shot = Shot("01_A", 100, "Done", self.test_dir)
        shot.make_directory(shot.path, shot.name)
        self.assertTrue(os.path.exists(shot.path + shot.name))

    def test_show_creation_json(self):
        # Create a show instance and check if the show JSON file is created
        show = Show("ShowTitle", 1000, "Done", self.test_dir)
        show.create("Show1", 1000, "Done", show.path, "show_data.json")
        self.assertTrue(os.path.exists(show.path + "show_data.json"))

        # Check the content of the show JSON file
        with open(show.path + "show_data.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "Show1")

    def test_shot_creation_json(self):
        # Create a shot instance and check if the shot JSON file is created
        shot = Shot("01_A", 100, "Done", self.test_dir)
        shot.create("Shot1", 100, "Done", shot.path, "shot_data.json")
        self.assertTrue(os.path.exists(shot.path + "shot_data.json"))

        # Check the content of the shot JSON file
        with open(shot.path + "shot_data.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "Shot1")

    # Add more unit tests for other functionalities

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
