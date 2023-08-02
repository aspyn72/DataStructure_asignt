import unittest
import os
import json
from ShowShotAsset_manager_AspynM import Show, Shot, Asset
import shutil

# Define the unit tests
class TestShowShotAssetManagement(unittest.TestCase):

    def setUp(self):
        # Create a test directory for the unit tests
        self.test_dir = "/Users/moon/Desktop/" #"D:\TEST"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Delete the test directory and its contents after the unit tests
        pass
        #shutil.rmtree(self.test_dir)

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

    def test_asset_creation(self):
        # Create a shot instance and check if the shot folder is created
        asset = Asset("AssetDB", self.test_dir)
        asset.make_directory(asset.path, asset.name)
        self.assertTrue(os.path.exists(asset.path + asset.name))

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

'''# Run the unit tests
if __name__ == '__main__':
    unittest.main()'''


################======================###############
import unittest
import os
import json
import time
from ShowShotAsset_manager_AspynM import Base_for_Directory_and_Info, Show, Shot, Asset

class TestBaseForDirectoryAndInfo(unittest.TestCase):
    def test_make_directory(self):
        # Test the make_directory function
        base_dir = "test_directory"
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Make sure the directory doesn't exist before calling the function
        self.assertFalse(os.path.exists(base_dir))
        
        # Call the function to create the directory
        base_obj.make_directory()
        
        # Check if the directory has been created
        self.assertTrue(os.path.exists(base_dir))
        
        # Clean up: Remove the directory after the test
        os.rmdir(base_dir)

    def test_delete_directory(self):
        # Test the delete_directory function
        base_dir = "test_directory"
        
        # First, create the directory to be deleted
        os.mkdir(base_dir)
        
        # Make sure the directory exists before calling the function
        self.assertTrue(os.path.exists(base_dir))
        
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Call the function to delete the directory
        base_obj.delete_directory()
        
        # Check if the directory has been deleted
        self.assertFalse(os.path.exists(base_dir))

    def test_create(self):
        # Test the create function
        base_dir = "test_directory"
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Make sure the directory doesn't exist before calling the function
        self.assertFalse(os.path.exists(base_dir))
        
        # Call the create function
        base_obj.create()
        
        # Check if the directory has been created
        self.assertTrue(os.path.exists(base_dir))
        
        # Clean up: Remove the directory after the test
        os.rmdir(base_dir)

    def test_delete(self):
        # Test the delete function
        base_dir = "test_directory"
        
        # First, create the directory to be deleted
        os.mkdir(base_dir)
        
        # Make sure the directory exists before calling the function
        self.assertTrue(os.path.exists(base_dir))
        
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Call the delete function
        base_obj.delete()
        
        # Check if the directory has been deleted
        self.assertFalse(os.path.exists(base_dir))
        self.assertIsNone(base_obj._data)  # Make sure the data attribute is reset to None

    def test_get_all_info(self):
        # Test the get_all_info function
        base_dir = "test_directory"
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Call the function to get all info (assuming there's some data in the directory)
        all_info = base_obj.get_all_info()
        
        # Check if the returned value is a list (or any other expected data structure)
        self.assertIsInstance(all_info, list)

    def test_get_single_info(self):
        # Test the get_single_info function
        base_dir = "test_directory"
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Call the function to get info about a single item (assuming there's some data in the directory)
        item_id = "item123"  # Replace with an actual item ID that exists in the directory
        single_info = base_obj.get_single_info(item_id)
        
        # Check if the returned value is a dictionary (or any other expected data structure)
        self.assertIsInstance(single_info, dict)

    def test_edit_name(self):
        # Test the edit_name function
        base_dir = "test_directory"
        base_obj = Base_for_Directory_and_Info(base_dir)
        
        # Assuming there's some data in the directory, get the info of an item
        item_id = "item123"  # Replace with an actual item ID that exists in the directory
        original_info = base_obj.get_single_info(item_id)
        
        # Edit the name of the item (you can modify any other attributes as needed)
        new_name = "New Item Name"
        base_obj.edit_name(item_id, new_name)
        
        # Get the updated info of the item after the edit
        updated_info = base_obj.get_single_info(item_id)
        
        # Check if the name attribute has been updated as expected
        self.assertEqual(updated_info['name'], new_name)


class TestShow(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test function in this class.
        # You can perform any setup tasks here.
        self.show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        self.show = Show("show_test_directory", self.show_data)

    def tearDown(self):
        # This method will be called after each test function in this class.
        # You can perform any cleanup tasks here.
        self.show.delete_directory()

    def test_create(self):
        # Test the create function in the Show class
        show_dir = "show_test_directory"
        show_obj = Show(show_dir, self.show_data)

        # Make sure the directory doesn't exist before calling the function
        self.assertFalse(os.path.exists(show_dir))

        # Call the create function
        show_obj.create()

        # Check if the directory has been created
        self.assertTrue(os.path.exists(show_dir))

        # Clean up: Remove the directory after the test
        os.rmdir(show_dir)

    def test_delete(self):
        # Test the delete function in the Show class
        show_dir = "show_test_directory"

        # First, create the show directory to be deleted
        os.mkdir(show_dir)

        # Make sure the directory exists before calling the function
        self.assertTrue(os.path.exists(show_dir))

        show_obj = Show(show_dir, self.show_data)

        # Call the delete function
        show_obj.delete()

        # Check if the directory has been deleted
        self.assertFalse(os.path.exists(show_dir))
        self.assertIsNone(show_obj._data)  # Make sure the data attribute is reset to None

    def test_get_all_info(self):
        # Test the get_all_info function in the Show class
        show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        show_obj = Show("show_test_directory", show_data)

        # Assuming there's some data in the show directory
        all_info = show_obj.get_all_info()

        # Check if the returned value is a list (or any other expected data structure)
        self.assertIsInstance(all_info, list)

    def test_get_single_info(self):
        # Test the get_single_info function in the Show class
        show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        show_obj = Show("show_test_directory", show_data)

        # Assuming there's some data in the show directory, get the info of a single show
        show_id = "show123"  # Replace with an actual show ID that exists in the directory
        single_info = show_obj.get_single_info(show_id)

        # Check if the returned value is a dictionary (or any other expected data structure)
        self.assertIsInstance(single_info, dict)

    def test_edit_name(self):
        # Test the edit_name function in the Show class
        show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        show_obj = Show("show_test_directory", show_data)

        # Assuming there's some data in the show directory, get the info of a show
        show_id = "show123"  # Replace with an actual show ID that exists in the directory
        original_info = show_obj.get_single_info(show_id)

        # Edit the name of the show (you can modify any other attributes as needed)
        new_name = "New Show Name"
        show_obj.edit_name(show_id, new_name)

        # Get the updated info of the show after the edit
        updated_info = show_obj.get_single_info(show_id)

        # Check if the name attribute has been updated as expected
        self.assertEqual(updated_info['name'], new_name)

class TestShot(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test function in this class.
        # You can perform any setup tasks here.
        self.show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        self.show = Show("show_test_directory", self.show_data)

    def tearDown(self):
        # This method will be called after each test function in this class.
        # You can perform any cleanup tasks here.
        self.show.delete_directory()

    def test_create(self):
        # Test the create function in the Shot class
        shot_data = {
            "name": "Test Shot",
            "duration": "30 seconds",
            "status": "completed"
        }
        shot_obj = Shot("show_test_directory/shot_test_directory", shot_data)

        # Verify that the shot directory is created with the correct name
        self.assertTrue(os.path.exists("show_test_directory/shot_test_directory"))
        self.assertTrue(os.path.isdir("show_test_directory/shot_test_directory"))

        # Verify that the shot_info.json file is created and contains the correct data
        self.assertTrue(os.path.exists("show_test_directory/shot_test_directory/shot_info.json"))
        with open("show_test_directory/shot_test_directory/shot_info.json") as f:
            shot_info = json.load(f)
        self.assertEqual(shot_info, shot_data)

    def test_create_or_add_assets(self):
        # ... Previous test case ...
        pass

    def test_delete_asset(self):
        # ... Previous test case ...
        pass

    def test_find_assets_by_shot(self):
        # Test the find_assets_by_shot function in the Shot class
        shot_data = {
            "name": "Test Shot",
            "duration": "30 seconds",
            "status": "completed"
        }
        shot_obj = Shot("show_test_directory/shot_test_directory", shot_data)

        # Assuming there are some assets in the shot directory
        # You may also consider mocking this data or using other test techniques
        asset_data1 = {
            "name": "Asset 1",
            "type": "character",
            "description": "Asset 1 description"
        }
        asset_obj1 = Asset("show_test_directory/shot_test_directory/asset_1", asset_data1)

        asset_data2 = {
            "name": "Asset 2",
            "type": "prop",
            "description": "Asset 2 description"
        }
        asset_obj2 = Asset("show_test_directory/shot_test_directory/asset_2", asset_data2)

        # Add the assets to the shot (you can use the create_or_add_assets function here)
        shot_obj.create_or_add_assets(asset_obj1)
        shot_obj.create_or_add_assets(asset_obj2)

        # Call the find_assets_by_shot function
        assets_in_shot = shot_obj.find_assets_by_shot()

        # Verify that the list of assets returned matches the assets added
        self.assertIn(asset_obj1, assets_in_shot)
        self.assertIn(asset_obj2, assets_in_shot)

        # Verify that the number of assets returned is correct
        self.assertEqual(len(assets_in_shot), 2)

class TestAsset(unittest.TestCase):
    def setUp(self):
        # This method will be called before each test function in this class.
        # You can perform any setup tasks here.
        self.show_data = {
            "name": "Test Show",
            "duration": "2 hours",
            "status": "ongoing"
        }
        self.show = Show("show_test_directory", self.show_data)

    def tearDown(self):
        # This method will be called after each test function in this class.
        # You can perform any cleanup tasks here.
        self.show.delete_directory()

    def test_make_directory(self):
        # ... Previous test case ...
        pass

    def test_delete_directory(self):
        # ... Previous test case ...
        pass

    def test_create(self):
        # ... Previous test case ...
        pass

    def test_delete_whole_category(self):
        # Test the delete_whole_category function in the Asset class
        asset_data = {
            "name": "Test Asset",
            "type": "character",
            "description": "Test description"
        }
        asset_obj = Asset("show_test_directory/asset_test_directory", asset_data)

        # Assuming there are some assets in the asset directory
        # You may also consider mocking this data or using other test techniques

        # Call the delete_whole_category function
        asset_obj.delete_whole_category()

        # Verify that the asset directory has been deleted
        self.assertFalse(os.path.exists("show_test_directory/asset_test_directory"))

    def test_delete_single_asset(self):
        # ... Previous test case ...
        pass

    def test_get_single_asset_info(self):
        # Test the get_single_asset_info function in the Asset class
        asset_data = {
            "name": "Test Asset",
            "type": "character",
            "description": "Test description"
        }
        asset_obj = Asset("show_test_directory/asset_test_directory", asset_data)

        # Assuming there's some data in the asset directory
        # You may also consider mocking this data or using other test techniques

        # Call the get_single_asset_info function
        asset_info = asset_obj.get_single_asset_info()

        # Verify that the asset_info returned matches the asset_data
        self.assertEqual(asset_info, asset_data)

if __name__ == "__main__":
    unittest.main()