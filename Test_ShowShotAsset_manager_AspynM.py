import unittest
import os
import json
import time
import shutil
from ShowShotAsset_manager_AspynM import Base_for_Directory_and_Info, Show, Shot, Asset, Zip_to_Archieve

TEMP_DIR_PATH = "/Users/moon/Desktop/Aspyn/"
TEMP_NAME = "Show_Shot_Asset_DB" 
SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
SHOW_NAME = "ShowTitle"
SHOT_DIR_PATH = SHOW_DIR_PATH + SHOW_NAME + "/"
SHOT_NAME= "01_A"
ASSET_DIR_PATH  = SHOW_DIR_PATH + SHOW_NAME + "/"
ASSET_NAME= "AssetDB"

class TestBaseForDirectoryAndInfo(unittest.TestCase):

    def setUp(self):
        # Create a test directory for the unit tests
        self.test_dir = TEMP_DIR_PATH
        #self.test_dir_stas = "/Users/moon/Desktop/Test/ShowTitle"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Delete the test directory and its contents after the unit tests
        #shutil.rmtree(self.test_dir)
        pass

    def test_show_creation(self):
        # Create a show instance and check if the show folder is created
        show = Show("ShowTitle", 1000, "Done", self.test_dir)
        show.make_directory(show.path, show.name)
        print("=====+++++=====")
        print(show.path)
        print("=====+++++=====")
        self.assertTrue(os.path.exists(show.path + show.name))

    def test_shot_creation(self):
        # Create a shot instance and check if the shot folder is created
        shot = Shot("shot1", 100, "Done", SHOT_DIR_PATH)
        shot.path=SHOT_DIR_PATH
        shot.make_directory(shot.path, shot.name)
        self.assertTrue(os.path.exists(shot.path + shot.name))

    def test_asset_creation(self):
        # Create a shot instance and check if the shot folder is created
        asset = Asset("asset_DB", ASSET_DIR_PATH)
        asset.make_directory(asset.path, asset.name)
        self.assertTrue(os.path.exists(asset.path + asset.name))
        print("=====+++++=====")
        print(asset.path)
        print("=====+++++=====")

    # JSON file -----
    def test_show_creation_json(self):
        # Create a show instance and check if the show JSON file is created
        show = Show("ShowTitle", 1000, "Done", self.test_dir)
        show.create("Show1", 1000, "Done", show.path, "show_data.json")
        self.assertTrue(os.path.exists(show.path + "show_data.json"))

        # Check the content of the show JSON file
        with open(show.path+"show_data.json" ) as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "Show1")

    def test_shot_creation_json(self):
        # Create a shot instance and check if the shot JSON file is created
        shot = Shot("01_A", 100, "Done", SHOT_DIR_PATH)
        shot.path=SHOT_DIR_PATH
        shot.create("Shot1", 100, "Done", shot.path, "shot_data.json","Show1")
        self.assertTrue(os.path.exists(shot.path + "shot_data.json"))

        # Check the content of the shot JSON file
        with open(shot.path + "shot_data.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Name"], "Shot1")


    def test_asset_creation_json(self):
        # Create a shot instance and check if the shot JSON file is created
        asset = Asset("asset_DB", self.test_dir)
        asset.path=ASSET_DIR_PATH
        asset.create("Asset1", "Category1", asset.path, "asset_data.json")
        self.assertTrue(os.path.exists(asset.path + "asset_data.json"))

        # Check the content of the shot JSON file
        with open(asset.path + "asset_data.json") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["Category1"], ["Asset1"])

    # Add more unit tests for other functionalities

# Run the unit tests
#if __name__ == '__main__':
#    unittest.main()