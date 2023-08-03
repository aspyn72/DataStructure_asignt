# Show, Shot, Asset Database Management API

<br>

# Index
- Introduction
- Class Structure
- Usage
- JSON File Example
- Project Structure

<br>

# Introduction

This project provides a database management system for organizing and managing show, shot, and asset data. It allows you to create, update, delete, and get information about shows, shots, and assets. Then it stores all the data in JSON files.

The system consists of the following classes:

- **`Base_for_Directory_and_Info`**: A parent class that provides common functionalities which are "create directory" and "get information".
- **`Show`**: A child class of **Base_for_Directory_and_Info** that represents a show. It provides methods for managing show data, such as creating shows, getting information about shows, editing show details, and etc.
- **`Shot`**: A child of **Base_for_Directory_and_Info** that represents a shot. It provides methods for managing shot data, such as creating shots, getting information about shots, editing shot details, and etc.
- **`Asset`**: A child of **Base_for_Directory_and_Info** that represents a asset. It provides methods for managing asset data, such as creating assets, getting information about assets, and etc.
- **`Zip_to_Archive`**: Independent class that represents zip file. It provides methods for managing shot data, such as archiving data, and getting information in the zipped file

<br>

# Class Structure

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+-----------------------------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+----------------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Base_for_Director_and_Info |
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Zip_to_Archive |
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+-----------------------------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+----------------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;V
<br> &nbsp;&nbsp; +------+
&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;+------+
&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;+------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;| Show |
&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;| Shot |
&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;| Asset |
<br>  &nbsp;&nbsp; +------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;+------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|___ <font size=1>interact</font> ___| &nbsp;&nbsp;| ___<font size=1>interact</font> ___|


<br>
<br>

# Usage


## 1. Global variables for directories
Set the global variables according to your desired directory structure.
- `TEMP_DIR_PATH`
- `TEMP_NAME`
- `SHOW_DIR_PATH`
- `SHOW_NAME` 
- `SHOT_DIR_PATH` 
- `SHOT_NAME` 
- `ASSET_DIR_PATH` 
- `ASSET_NAME` 

<br>

## 2. Set Variables to Call classes

Instantiate the `Show`, `Shot`, `Asset`, and `ZIP_TO_ARCHIVE` classes with appropriate parameters.
   ```python
   ShowFunc=Show("FilmTitle",1000,"Done",SHOW_DIR_PATH)
   ShotFunc=Shot("ShotName",100,"Done",SHOT_DIR_PATH)
   AssetFunc=Asset("AssetName",ASSET_DIR_PATH)
   ArchiveFunc=Zip_to_Archive(TEMP_DIR_PATH,TEMP_NAME)
   ```
  Codes above are already written on the main script, so you can use those.

<br>

## 3. Use the methods provided by the classes 

###  `Base_for_Directory_and_Info` (Common Functions)

Belows are the functions you can use

   > `make_directory(path: str, name: str)`:  
    - Creates a directory with the given path and name.
   <br>
    - You should put **path** where the folders will be located and the **name** of the folder.  
    - This function is used for **Show, Shot**, and **Asset** classes

   > `delete_directory(path: str, name: str)`:
   <br> - Deletes a directory with the given path and name.
   <br>
    - You should put **path** where the folder is located and the **name** of the folder you want to delete.
      <br>
    - This function is used for **Show, Shot**, and **Asset** classes

   > `get_all_info(path: str, file_json_name: str)`: <br> - Prints all the information stored in the JSON file.
   <br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). 
   <br> - This function is used for **Show, Shot**, and **Asset** classes

   >`get_single_info(name: str, path: str, file_json_name: str)`: 
   <br> - Prints the information of a specific show or shot with the given name.
   <br> - You should put the **name** of the show or shot you want to get info of, **path** where you saved JSON file and **name of the JSON file** ( you must put '**.json**' at the end of the name ).
   <br> - This function is used for **Show** and **Shot** classes 


## `Show`

Belows are the functions (that are only used for Show class) you can use

> `create(name: str, duration: int, status: str, path: str, file_json_name: str)`: 
   <br> - Creates the data of show with the specified details as a dictionary form and adds it to the JSON file.
   <br> - You should put **name**, **duration**, and **status** of the show or shot. Then, put the **path** where you want to (did) save JSON file and **name of the JSON file** ( you must put '**.json**' at the end of the name ).

> `delete(name: str, path: str, file_json_name: str)`:
   <br>  - Deletes a show information with the given name from the JSON file.
   <br> - You should put **name** of the show or shot. Then, put the **path** where you saved JSON file and **name of the JSON file** ( you must put '**.json**' at the end of the name ).

> `edit_name(path: str, file_json_name: str, name: str, new_name: str)`: 
   <br> - Updates the name of a show with the given name to a new name.
   <br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **original name** of the show, and the **new name** next to it.

   > `edit_duration(path: str, file_json_name: str, name: str, new_duration: int)`:
   <br> - Updates the duration of a show with the given name to a new duration.
   <br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the show, and the **new duration** next to it.
   
   > `edit_status(path: str, file_json_name: str, name: str, new_status: str)`: 
   <br> - Updates the status of a show with the given name to a new status.
  <br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the show, and the **new status** next to it.

## `Shot`

Belows are the functions (that are only used for Shot class) you can use
> `create(self, name: str, duration: int, status: str, path: str, file_json_name: str, show_name: str):`
   <br> - Creates the data of shot with the specified details as a dictionary form and adds it to the JSON file.
   <br> - You should put **name**, **duration**, and **status** of the shot. Then, put the **path** where you want to (did) save JSON file, the **name of the JSON file** ( you must put '**.json**' at the end of the name ), and **show name** to store shot data into the specific show.
   <br> - You don't use this function to put assets in the shot here

> `delete(self, name: str, path: str, file_json_name: str, show_name: str):`
<br> - Deletes a shot information with the given name from the JSON file.
   <br> - You should put **name** of the show or shot. Then, put the **path** where you saved JSON file, the **name of the JSON file** ( you must put '**.json**' at the end of the name ), and **show name** to delete the shot data from the specific show.

>`edit_name(self, path: str, file_json_name: str, name: str, new_name: str,show_name: str):`
<br> - Updates the name of a shot with the given name to a new name.
   <br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **original name** of the shot, the **new name** next to it, and **show name** of the show for which you want to update the shot data.

>`edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int, show_name: str):`
<br> - Updates the duration of a shot with the given name to new duration.
<br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the shot, the **new duration** next to it, and **show name** of the show for which you want to update the shot data.

>`edit_status(self, path: str, file_json_name: str, name: str, new_status: str, show_name: str):`
<br> - Updates the status of a shot with the given name to new status.
<br> - You should put the **path** where you saved JSON file and the **name of the JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the shot, the **new status** next to it, and **show name** of the show for which you want to update the shot data.

>`create_or_add_assets(self, name:str, asset_name:str, path: str, file_json_name: str, asset_file_json_name:str, show_name: str):`

>`delete_asset(self, name:str, asset_name:str, path:str, file_json_name:str, show_name:str):`

>`edit_asset_name(self,name:str,asset_name:str,new_asset_name:str,path:str,file_json_name:str,asset_file_json_name:str ,show_name:str):`

>`find_assets_by_shot(self,name:str,path:str,file_json_name:str):`

>`find_shots_by_asset(self,asset_name:str,path:str,file_json_name:str):`




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

<br>

<br>

# JSON File Example

- **`Order to Use`**: 
<br> STEP 1 ) Create **SHOW** data first 
<br>STEP 2 ) Create **ASSET** data for the show 
<br>STEP 3 ) Create **SHOT** data for the show

- **`Show JSON File`**: A child class of details.
- **`Shot JSON File`**: A child of **Base_for_Directory_and_Info** details.
- **`Asset JSON File`**: A child of **Base_for_Directory_and_Info** details.


<br>

<font size="4.5">**Example**</font>

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

<br>

<br>



# Project Structure


- `ShowShotAsset_manager_AspynM.py`: Contains the implementation of the database management system.
- `README.md`: Provides information about the project and usage examples.
