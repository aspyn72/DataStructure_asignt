# DataStructure_asignt
Data Structure Assignment for BCIT

##Show and Shot Database Management System

This project provides a database management system for organizing and managing show and shot data. It allows you to create, retrieve, update, and delete information about shows and shots, and stores the data in JSON files.

The system consists of the following classes:

- `Template`: An abstract class that provides common functionality for creating, deleting, and modifying data.
- `Show`: A subclass of `Template` that represents a show. It provides methods for managing show data, such as creating shows, retrieving information about shows, and editing show details.
- `Shot`: A subclass of `Template` that represents a shot. It provides methods for managing shot data, such as creating shots, retrieving information about shots, and editing shot details.

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

## 2. Set Variables to Call classes

Instantiate the `Show` and `Shot` classes with the appropriate parameters.
   ```python
   ShowFunc = Show("FilmTitle", 1000, "Done", SHOW_DIR_PATH)
   
   ShotFunc = Shot("ShotName", 100, "Done", SHOT_DIR_PATH)
   ```
   Lines above are already written on the main script, so you can use those.

## 3. Use the methods provided by the classes to manage show and shot data.

 Some of the available methods include:
   - `make_directory(path: str, name: str)`: Creates a directory with the given path and name.
   - `delete_directory(path: str, name: str)`: Deletes a directory with the given path and name.
   - `create(name: str, duration: int, status: str, path: str, file_json_name: str)`: Creates a show or shot with the specified details and adds it to the JSON file.
   - `delete(name: str, path: str, file_json_name: str)`: Deletes a show or shot with the given name from the JSON file.
   - `get_all_info(path: str, file_json_name: str)`: Prints all the information stored in the JSON file.
   - `get_single_info(name: str, path: str, file_json_name: str)`: Prints the information of a specific show or shot with the given name.
   - `edit_name(path: str, file_json_name: str, name: str, new_name: str)`: Updates the name of a show or shot with the given name to a new name.
   - `edit_duration(path: str, file_json_name: str, name: str, new_duration: int)`: Updates the duration of a show or shot with the given name to a new duration.
   - `edit_status(path: str, file_json_name: str, name: str, new_status: str)`: Updates the status of a show or shot with the given name to a new status.

**Example Usage:**

```python
# Create a show
ShowFunc.create("Mimic", 60, "InProgress", SHOW_DIR_PATH, "show_db.json")

# Get all show information
ShowFunc.get_all_info(SHOW_DIR_PATH, "show_db.json")

# Get information for a specific show
ShowFunc.get_single_info("Mimic", SHOW_DIR_PATH, "show_db.json")

# Update the name of a show
ShowFunc.edit_name(SHOW_DIR_PATH, "show_db.json", "Mimic", "New Name")

# Delete a show
ShowFunc.delete("Mimic", SHOW_DIR_PATH, "show_db.json")
```

**Project Structure:**

- `main.py`: Contains the implementation of the database management system.
- `README.md`: Provides information about the project and usage examples.
