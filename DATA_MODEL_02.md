

>You can check the commits that I’ve made in this page
>Github link>
: https://github.com/aspyn72/DataStructure_asignt 

<br>

This document explains the data model I created and the rationale for why I’ve chosen the data types and structures that I have. The data model provides a structured approach for managing show and shot data within a directory structure. 

## 1. Classes
The data model includes three classes: *Template, Show*, and *Shot*. 

Template class is on the top on the hierarchy. Show and shot classes are on the same hierarchy (in the script wise) but below the Template class. In  directory wise, the shot folder(s) is(are) inside the show folder.

The Template class is an abstract class which is a parent class of Show and Shot class. It defines common methods and attributes for shows and shots. It includes methods for creating, deleting, and editing data and directory.

The Show and Shot classes are inherited from the Template class because they are the child classes. So, they extend the functionality of the Template class.

## 2. Global Variables
*TEMP_DIR_PATH, TEMP_NAME, SHOW_DIR_PATH, SHOW_NAME, SHOT_DIR_PATH*, and *SHOT_Name* represent the directory paths and folder names used in the data model. They are defined as global variables for easy modification and reuse. To create multiple different directories, user should put different paths and names to the variables.

## 3. Directory
The data model includes methods for creating directories(/folders) to organize shows and shots.

The *make_directory* method creates a new folder within the specified directory path.

The directory structure is represented by the *SHOW_DIR_PATH* and *SHOT_DIR_PATH* variables, which determine the location of show and shot folders.


## 4. Data Storage
The data model uses JSON files to store information about shows and shots. Each JSON file represents a collection of show or shot data.

The data for each show or shot is stored as a dictionary with keys such as *"Name," "Time Duration,"* and *"Status"*.

The *create* method adds a new dictionary of show or shot data to the respective JSON file.

The *delete* method removes a specific dictionary from the JSON file based on the provided name.

The *get_all_info* method prints all the show or shot data from the JSON file.

The *get_single_info* method prints a specific show or shot data from the JSON file based on the provided name.

The *edit_name, edit_duration,* and *edit_status* methods modifies specific attributes of a show or shot.

