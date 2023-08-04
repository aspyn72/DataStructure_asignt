# Data Model <br> - Show, Shot, Asset Database Management #

<br>

>You can check the commits that I’ve made in this page
>Github link>
: https://github.com/aspyn72/DataStructure_asignt 
<br>

This document explains the data model I created and the rationale for why I’ve chosen the data types and structures that I have. The data model provides a structured approach for managing show and shot data within a directory structure. 


<br>

# Index
- Classes
- Global Variables
- Directory
- Data Storage & Archive
- JSON File

<br>

# 1. Classes
The data model includes five classes: ***Base_for_Directory_and_Info***, ***Show***, ***Shot***, ***Asset***, and ***Zip_to_Archieve***. 

## Class Structure

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

*Base_for_Directory_and_Info* class is a parent class of Show, Shot, and Asset classes. It defines common methods and attributes for shows, shots, and assets. It includes methods for creating & deleting a directory, and getting information. *Show, Shot, *and* Asset classes* inherit and use those functions from Base_for_Directory_and_Info class as child classes. *Zip_to_Archive class* is independent from other classes. 

<br>

# 2. Global Variables

`TEMP_DIR_PATH`, `TEMP_NAME`, `SHOW_DIR_PATH`, `SHOW_NAME`, `SHOT_DIR_PATH`, `SHOT_NAME`, `ASSET_DIR_PATH`, and `ASSET_NAME` represent the directory paths and folder names used in the data model. They are defined as global variables for easy modification and reuse. To create multiple different directories, users should put different paths and folder names to the variables.

<br>

# 3. Directory
The data model includes methods for creating or deleting directories to organize shows, shots, and assets.

The **make_directory** method creates a new folder within the specified directory path.

The **delete_directory** method deletes a new folder within the specified directory path.

The directory structure is represented by the *SHOW_DIR_PATH*, *SHOT_DIR_PATH*, and *ASSET_DIR_PATH* variables, which determine the location of show, Shot, and Asset folders.

<br>

# 4. Data Storage & Archive
The data model uses JSON files to store information about shows and shots. Each JSON file represents a collection of show or shot data.

The data for each  <br>
->&nbsp;**show** is stored as a dictionary with keys such as *"Name", "Time Duration", "Status"*, and *"Shot"*. <br>
->&nbsp;**shot** is stored as a dictionary with keys such as *"Name", "Time Duration", "Status"*, and *"Asset"*. <br>
->&nbsp;**asset** is stored as a dictionary with a key, *"category"*.

The **`create`**, and **`create_or_add_assets`** methods add a new dictionary or ata of *show, shot, asset in a shot*, and *asset data* to the respective JSON file.

The **`delete`**,  **`delete_whole_category`**, **`delete_single_asset`**, and **`delete_asset`** methods remove a specific dictionary or data from the JSON file based on the provided name.

The **`get_all_info`** method prints all the show, shot, or asset data from the JSON file.

The **`get_single_info`**, **`find_assets_by_shot`**, **`find_shots_by_asset`**, **`get_single_asset_info`**, **`get_single_category_info`**, and **`read_zip_file`** methods print a specific show, shot, or asset data from the JSON file based on the provided name.

The **`edit_name`, `edit_duration`, `edit_status`**, and **`edit_asset`** methods modifies specific attributes of a show, shot, or asset.

The **`archive`** method zips folders in the specified directory path.

# 5. JSON File

- **`Show JSON File`**<br>
: Should exist only one file to store all shows.<br>
: "Shots" section in the file will be automatically filled up when shot's json file is updated. <br>
: User can check show, shot, and asset data in the file.
               
- **`Shot JSON File`** <br>
: Can exist as many files as the number of shows. <br>
: 'category' in "Asset" will automatically be filled up from asset's JSON file. <br>
: Shot will be automatically updated on show's JSON file<br>
: Only assets existing in asset's JSON file can be put in Shot file's "Asset" section.<br>
: User can check shot and asset data in the file.

- **`Asset JSON File`**: <br>
: Can exist as many files as the number of shows.<br>
: Edited asset will be automatically updated on shot's JSON file as well.<br>
: User can check asset data in the file

<br>

*For more information, please check README.md file*