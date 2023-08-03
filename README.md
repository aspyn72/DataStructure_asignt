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

>&nbsp;<br>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+-----------------------------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+----------------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Base_for_Director_and_Info |
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| Zip_to_Archive |
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
+-----------------------------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+----------------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;|
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;V&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;V&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; V
<br> &nbsp;&nbsp; +------+
&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;+------+
&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;+------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;| Show |
&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;| Shot |
&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;| Asset |
<br>  &nbsp;&nbsp; +------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+------+
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;+------+
<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|___ <font size=1>interact</font> ___| &nbsp;&nbsp;| ___<font size=1>interact</font> ___| <br>
>&nbsp;<br>


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
   ><br>
   >ShowFunc=Show("FilmTitle",1000,"Done",SHOW_DIR_PATH)
   >ShotFunc=Shot("ShotName",100,"Done",SHOT_DIR_PATH)
   >AssetFunc=Asset("AssetName",ASSET_DIR_PATH)
   >ArchiveFunc=Zip_to_Archive(TEMP_DIR_PATH,TEMP_NAME)
   >
   ><br>
   
   <br>
  Codes above are already written on the main script, so you can use those.

<br>

## 3. Use the methods provided by the classes 

###  `Base_for_Directory_and_Info` (Common Functions)

Belows are the functions you can use in Shot, Show, and Asset classes

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

Belows are the functions you can use only for Show class

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

Belows are the functions you can use only for Shot class

> `create(self, name: str, duration: int, status: str, path: str, file_json_name: str, show_name: str):`
<br> - Creates the data of shot with the specified details as a dictionary form and adds it to the JSON file.
<br> - You should put **name**, **duration**, and **status** of the shot. Then, put the **path** where you want to (did) save JSON file, the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ), and **show name** to store shot data into the specific show.
<br> - You don't use this function to put assets in the shot here

> `delete(self, name: str, path: str, file_json_name: str, show_name: str):`
<br> - Deletes a shot information with the given name from the JSON file.
<br> - You should put **name** of the show or shot. Then, put the **path** where you saved JSON file, the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ), and **show name** to delete the shot data from the specific show.

>`edit_name(self, path: str, file_json_name: str, name: str, new_name: str,show_name: str):`
<br> - Updates the name of a shot with the given name to a new name.
<br> - You should put the **path** where you saved JSON file and the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **original name** of the shot, the **new name** next to it, and **show name** of the show for which you want to update the shot data.

>`edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int, show_name: str):`
<br> - Updates the duration of a shot with the given name to new duration.
<br> - You should put the **path** where you saved JSON file and the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the shot, the **new duration** next to it, and **show name** of the show for which you want to update the shot data.

>`edit_status(self, path: str, file_json_name: str, name: str, new_status: str, show_name: str):`
<br> - Updates the status of a shot with the given name to new status.
<br> - You should put the **path** where you saved JSON file and the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ). Then, put the **name** of the shot, the **new status** next to it, and **show name** of the show for which you want to update the shot data.

>`create_or_add_assets(self, name:str, asset_name:str, path: str, file_json_name: str, asset_file_json_name:str, show_name: str):`
<br> - Creates the data of assets with their categories as a dictionary form and adds it to a shot's JSON file.
<br> - You should put **shot name**, **asset name**, **path** where you want to (did) save JSON file, the **name of the shot's JSON file** ( you must put '**.json**' at the end ), the **name of the asset's JSON file** to fetch the category of the asset ( you must put '**.json**' at the end ), and the **show name** of the show for which you want to update the shot data in order.

>`delete_asset(self, name:str, asset_name:str, path:str, file_json_name:str, show_name:str):`
>
>-&nbsp;Deletes a asset information with the given name from the JSON file.<br>
>-&nbsp;You should put **shot name**, **asset name**, **path** where you want to (did) save JSON file, the **name of the shot's JSON file** ( you must put '**.json**' at the end ), and the **show name** of the show for which you want to update the shot data in order.

>`edit_asset_name(self, name:str, asset_name:str, new_asset_name:str, path:str, file_json_name:str, asset_file_json_name:str, show_name:str):`
>
>-&nbsp;Updates the name of a asset with the given name to new asset name.<br>
>-&nbsp;You should put **shot name**, **asset name**, **new asset name**, **path** where you want to (did) save JSON file, the **name of the shot's JSON file** ( you must put '**.json**' at the end ), the **name of the asset's JSON file** to update ( you must put '**.json**' at the end ), and the **show name** of the show for which you want to update the shot data in order.

>`find_assets_by_shot(self,name:str,path:str,file_json_name:str):`
>
>-&nbsp;Prints the information of asset(s) of a shot.<br>
>-&nbsp;You should put the **name** of the shot, **path** where you saved shot's JSON file, and the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ).

>`find_shots_by_asset(self,asset_name:str,path:str,file_json_name:str):`
>
>-&nbsp;Prints the information of shot(s) which have a specific asset.<br>
>-&nbsp;You should put the **asset name**, **path** where you saved shot's JSON file, and the **name of the shot's JSON file** ( you must put '**.json**' at the end of the name ).

## `Asset`

Belows are the functions you can use only for Asset class

>`create(self, name: str, category: str, path: str, file_json_name: str) -> None:`
>
>-&nbsp;Creates the data of assets and categories as a dictionary form and adds it to an asset's JSON file.
<br> - You should put **asset name**, **asset category**, **path** where you want to (did) save asset's JSON file, and the **name of the asset's JSON file** ( you must put '**.json**' at the end ) in order.

>`delete_whole_category(self, category: str, path: str, file_json_name: str):`
>
>-&nbsp;Deletes a category and assets inside with the given category name from the asset's JSON file.<br>
>-&nbsp;You should put **category name**, **path** where you saved asset's JSON file, and the **name of the asset's JSON file** ( you must put '**.json**' at the end ).

>`delete_single_asset(self, name: str, category:str, path: str, file_json_name: str):`
>
>-&nbsp;Deletes an asset with the given name from the asset's JSON file.<br>
>-&nbsp;You should put **asset name**, **catergory name** where the asset is, **path** where you saved asset's JSON file, and the **name of the asset's JSON file** ( you must put '**.json**' at the end ) in order.

>`get_single_asset_info(self, name: str, path: str, file_json_name: str):`
>
>-&nbsp;Print the information of an asset and it's category.<br>
>-&nbsp;You should put **asset name**, **path** where you saved asset's JSON file, and the **name of the asset's JSON file** ( you must put '**.json**' at the end ) in order.

>`get_single_category_info ( self, category: str, path: str, file_json_name: str):`
>
>-&nbsp;Print the information of an category and all the assets inside.<br>
>-&nbsp;You should put **category name**, **path** where you saved asset's JSON file, and the **name of the asset's JSON file** ( you must put '**.json**' at the end ) in order.

>`edit_asset(self, name: str, new_name: str, category:str, path: str, file_json_name: str, shot_file_json_name: str, show_name:str):`<br>
>-&nbsp;Updates the name of an asset to a new asset name.
>-&nbsp;You should put **asset name**, **new asset name**,**asset's category name**,**path** where you saved asset's JSON file, the **name of the asset's JSON file** ( you must put '**.json**' at the end ), the **name of the shot's JSON file** ( you must put '**.json**' at the end ), and it's **show name** in order.

### `Zip_to_Archieve`

Belows are the functions you can use only for Zip_to_Archieve class

>`archive(self,path:str, folder_name:str):`
>
>-&nbsp;Zip the folder you want.<br>
>-&nbsp;You should put **path** where the directory exist, and the **folder name** in order.

>`read_zip_file(self, folder_name:str, path:str, zip_filename:str)`
>
>-&nbsp;Read data in a zipped folder.<br>
>-&nbsp;You should put **folder name**, **path** where the directory exist, and the **zip filename** in order.

## `Example Usage`


```python
# Create Directory
ShotFunc.make_directory(SHOT_DIR_PATH, SHOT_NAME)
AssetFunc.make_directory(ASSET_DIR_PATH, ASSET_NAME)

# Create a show, shot, asset
ShowFunc.create("ShowTitle", 60, "InProgress", SHOW_DIR_PATH, "ShowDB.json")
AssetFunc.

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

- **`Order to create`**: 
<br> STEP 1 ) Create **SHOW** data first 
<br>STEP 2 ) Create **ASSET** data for the show 
<br>STEP 3 ) Create **SHOT** data for the show

- **`Show JSON File`**: A child class of details.
- **`Shot JSON File`**: A child of **Base_for_Directory_and_Info** details.
- **`Asset JSON File`**: A child of **Base_for_Directory_and_Info** details.



<br>



# Project Structure


- `ShowShotAsset_manager_AspynM.py`: Contains the implementation of the database management system.
- `README.md`: Provides information about the project and usage examples.
