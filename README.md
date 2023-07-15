# Show and Shot Database Management API

This project provides a database management system for organizing and managing show and shot data. It allows you to create, update, delete, and get information about shows and shots, and stores the data in JSON files.

The system consists of the following classes:

- **`Template`**: An abstract class that provides common functionality for creating, deleting, and modifying data.
- **`Show`**: A child class of **Template** that represents a show. It provides methods for managing show data, such as creating shows, getting information about shows, and editing show details.
- **`Shot`**: A child of **Template** that represents a shot. It provides methods for managing shot data, such as creating shots, getting information about shots, and editing shot details.

<br>

# Usage

## 1. Global variables for directories
Set the global variables
- `TEMP_DIR_PATH`
- `TEMP_NAME`
- `SHOW_DIR_PATH`
- `SHOW_NAME` 
- `SHOT_DIR_PATH` 
- `SHOT_NAME` 
>
   according to your desired directory structure.
   <br><font size="1">Check the strings that already provided as an example. Try to have a same structure with it.</font>

## 2. Set Variables to Call classes

Instantiate the `Show` and `Shot` classes with the appropriate parameters.
   ```python
   ShowFunc = Show("FilmTitle", 1000, "Done", SHOW_DIR_PATH)
   
   ShotFunc = Shot("ShotName", 100, "Done", SHOT_DIR_PATH)
   ```
  Codes above are already written on the main script, so you can use those.

## 3. Use the methods provided by the classes to manage show and shot data.

Belows are the functions you can use

   > `make_directory(path: str, name: str)`:  
   Creates a directory with the given path and name.
   <br><font size="1.8"> You should put **path** where the folders will be located and **name** of the folder. </font>

   > `delete_directory(path: str, name: str)`:
   <br>Deletes a directory with the given path and name.
   <br><font size="1.8"> You should put **path** where the folder is located and **name** of the folder you want to delete. </font>

   > `create(name: str, duration: int, status: str, path: str, file_json_name: str)`: 
   <br>Creates the data of show or shot with the specified details as a dictionary form and adds it to the JSON file.
   <br><font size="1.8"> You should put **name**, **duration**, and **status** of the show or shot. Then, put the **path** where you want to (did) save JSON file and **name of the JSON file(<font size="1.9">you must put '.json' at the end of the name)**. </font>

   >`delete(name: str, path: str, file_json_name: str)`:
   <br> Deletes a show or shot information with the given name from the JSON file.
   <br><font size="1.8"> You should put **name** of the show or shot. Then, put the **path** where you saved JSON file and **name of the JSON file(<font size="1.9">you must put '.json' at the end of the name)** . </font>

   > `get_all_info(path: str, file_json_name: str)`: <br>Prints all the information stored in the JSON file.
   <br><font size="1.8"> You should put the **path** where you saved JSON file and **name of the JSON file(<font size="1.9">you must put '.json' at the end of the name)**. </font>

   >`get_single_info(name: str, path: str, file_json_name: str)`: 
   <br>Prints the information of a specific show or shot with the given name.
   <br><font size="1.8"> You should put the **name** of the show or shot you want to get info of, **path** where you saved JSON file and **name of the JSON file (<font size="1.9">you must put '.json' at the end of the name)**. </font>

   > `edit_name(path: str, file_json_name: str, name: str, new_name: str)`: 
   <br>Updates the name of a show or shot with the given name to a new name.
   <br><font size="1.8"> You should put the **path** where you saved JSON file and **name of the JSON file (<font size="1.9">you must put '.json' at the end of the name)**. Then, put the **original name** of the show or shot, and the **new name** next to it. </font>

   > `edit_duration(path: str, file_json_name: str, name: str, new_duration: int)`:
   <br> Updates the duration of a show or shot with the given name to a new duration.
   <br><font size="1.8"> You should put the **path** where you saved JSON file and **name of the JSON file (<font size="1.9">you must put '.json' at the end of the name)**. Then, put the **name** of the show or shot, and the **new duration** next to it. </font>
   
   > `edit_status(path: str, file_json_name: str, name: str, new_status: str)`: 
   <br>Updates the status of a show or shot with the given name to a new status.
  <br><font size="1.8"> You should put the **path** where you saved JSON file and **name of the JSON file (<font size="1.9">you must put '.json' at the end of the name)**. Then, put the **name** of the show or shot, and the **new status** next to it. </font>

<br>

<font size="4.5">**Example Usage:**</font>

```python
# Create a show
ShowFunc.create("ShowTitle", 60, "InProgress", SHOW_DIR_PATH, "ShowDB.json")

# Get all show information
ShowFunc.get_all_info(SHOW_DIR_PATH, "ShowDB.json")

# Get information for a specific show
ShowFunc.get_single_info("ShowTitle", SHOW_DIR_PATH, "ShowDB.json")

# Update the name of a show
ShowFunc.edit_name(SHOW_DIR_PATH, "ShowDB.json", "Mimic", "New Name")

# Delete a show
ShowFunc.delete("ShowTitle", SHOW_DIR_PATH, "ShowDB.json")
```


## Project Structure

- `ShowShot_manager_AspynM.py`: Contains the implementation of the database management system.
- `README.md`: Provides information about the project and usage examples.
