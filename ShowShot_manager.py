import os
from os import path as osPath
import sys
import json
import shutil
from typing import List, Dict

# ======== Global Variables for DIRECTORY (FOLDERS) ========
# you should put your directory PATH and folder NAME here / I put random strings for example
# ****** put Directory Path to save Show DB and Shot DB (folders and .json files) inside ****** #
TEMP_DIR_PATH = "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/"
TEMP_NAME = "Show_Shot_DB" 
    # need to put show folder name here to avoid putting the path manually
SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
SHOW_NAME = "My_Show"
    # need to put shot folder name here to avoid putting the path manually
SHOT_DIR_PATH = SHOW_DIR_PATH + SHOW_NAME + "/"
SHOT_Name= "01_A"
# =======================================================

# ======== CLASSes Starts Here ========

### Abstract Class ###
class Template:
    def __init__(self, name : str, duration : int, status:str, path:str):
        self.name = name
        self.duration=duration
        self.status=status
        self.path= path

    # Make Directory (Folder)
    def make_directory(self,path: str, name: str):
        folder_dir = osPath.join(path, name)
        #folder_dir = os.path.join(path, name)
        #if os.path.exists(folder_dir):
        if osPath.exists(folder_dir):
            print(f"'{folder_dir}' already exists.")
        else:
            os.makedirs(folder_dir)
            print(f"'{folder_dir}' is created.")

    # CREATE shows or shots and will ADD to .json file
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str):
        data = {
                    "Name": name,
                    "Time Duration": duration,
                    "Status": status,
                    }
        filePathNameWExt = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(filePathNameWExt):
            # in case the file already exists
            print(".json file exists")
            with open(filePathNameWExt) as file:
                self.list_for_org = json.load(file)
            # we put the data(Dictionary) in .json file here
            self.list_for_org.append(data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)
        else:
            # in case the file doesn't exist
            print("created .json file")
            self.list_for_org=[]

            with open(filePathNameWExt,'w') as file:
                json.dump(self.list_for_org,file)

            with open(filePathNameWExt) as file:
                self.list_for_org = json.load(file)

            # we put the data(Dictionary) in .json file here
            self.list_for_org.append(data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)

        # Print results
        print("=== Dictionary Show(or Shot) data ====")
        print(name+" info is created and added")
        print(data)
        print("=== data that exists in the file so far ===")
        print(self.list_for_org)

    # delete specific data from .json file
    def delete(self, name: str, path: str, file_json_name: str):
        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    self.list_for_org.remove(deletedinfo)
                    print("It's deleted")
                else:
                    pass
         # Update the content of .json file which removed desired show(or shot) data
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    # Read the file you want and print all the content inside the file
    def get_all_info(self, path: str, file_json_name: str ):
         filePathNameWExt = path + file_json_name
         with open(filePathNameWExt, 'r') as file:
            self.list_to_print = json.load(file)
            print("")
            print("===== Get ALL information =====")
            print("")
            print(self.list_to_print)
            print("")
            print("===== END =====")
            print("")

    # Read the file and print the data you want to check
    def get_single_info(self, name: str, path: str, file_json_name: str):
        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_infor = json.load(file)

        for sinfo in self.list_for_infor:
            for key, val in sinfo.items():
                if val==name:
                    print("")
                    print("===== Get information =====")
                    print("")
                    print(sinfo)
                    print("")
                    print("===== END =====")
                    print("")
                else:
                    pass
        
    ## EDIT data part ##

    # edit name info
    def edit_name(self, path: str, file_json_name: str, name: str, new_name: str):
        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo['Name']=new_name
                    print("Name is updated")
                    break
                else:
                    print("There's nothing to edit")
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    # edit time duration info - recieve name to pick out the desirable data dictionary
    def edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int):
        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    #self.list_for_org.remove(deletedinfo)
                    deletedinfo['Time Duration']=new_duration
                    print("Duration is updated")
                    break
                else:
                    print("There's nothing to edit")
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
    
    # edit status info
    def edit_status(self, path: str, file_json_name: str, name: str, new_status: str ):
        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo['Status']=new_status
                    print("Status is updated")
                    break
                else:
                    pass
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)


### SHOW class (child of the abstract class) ###
class Show(Template):

    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOW_NAME
        self.path=SHOW_DIR_PATH
        self.SHOW_DB=[]

    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str):
        return super().create(name, duration, status, path, file_json_name)
    
    def delete(self, name: str, path: str, file_json_name: str):
        return super().delete(name, path, file_json_name)
    
    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)

    def get_single_info(self, name: str, path: str, file_json_name: str):
        return super().get_single_info(name, path, file_json_name)

    ## EDIT part
    def edit_name(self, path: str, file_json_name: str, name: str, new_name: str):
        return super().edit_name(path, file_json_name, name, new_name)
    
    def edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int):
        return super().edit_duration(path, file_json_name, name, new_duration)
    
    def edit_status(self, path: str, file_json_name: str, name: str, new_status: str):
        return super().edit_status(path, file_json_name, name, new_status)

### SHOT class (child of the abstract class) ###
class Shot(Template):
    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOT_Name
        self.path=SHOT_DIR_PATH
        self.SHOT_DB=[]
    
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str):
        return super().create(name, duration, status, path, file_json_name)
    
    def delete(self, name: str, path: str, file_json_name: str):
        return super().delete(name, path, file_json_name)

    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)
    
    def get_single_info(self, name: str, path: str, file_json_name: str):
        return super().get_single_info(name, path, file_json_name)
    
    ## EDIT part
    def edit_name(self, path: str, file_json_name: str, name: str, new_name: str):
        return super().edit_name(path, file_json_name, name, new_name)
    
    def edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int):
        return super().edit_duration(path, file_json_name, name, new_duration)
    
    def edit_status(self, path: str, file_json_name: str, name: str, new_status: str):
        return super().edit_status(path, file_json_name, name, new_status)

# ======== Variables to CALL CLASS ========
# you can use these or create on your own
ShowFunc=Show("FilmTitle",1000,"Done",SHOW_DIR_PATH)
ShotFunc=Shot("ShotName",100,"Done",SHOT_DIR_PATH)

# ======== Use this line below to create DIRECTORY ========
    # Below will create Directory in hierarchy [Show_Shot_DB folder <- "Your_Show" folder <- "01_A" folder]
    # You can create show (or shot) folder for different shows (or shots) as many as you want
ShowFunc.make_directory(SHOT_DIR_PATH,SHOT_Name)

#ShowFunc.create("JurassicPark",50,"Done",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#ShotFunc.create("1A",24,"Done",SHOT_DIR_PATH,"My_Shot_DB.json")

# ========== TESTing here ========== #
#May.delete("Maybe",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#May.edit_name(SHOW_DIR_PATH,"MY_SHOW_DB.json","Maybe","Maynot")
#Jurassic.create("JurassicPark",50,"Done",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Parasite.create("Parasite",90,"Done",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.edit_name(SHOW_DIR_PATH,"MY_SHOW_DB.json","JurassicPark","Maynot")
#May.create("Maybe",40,"Inprogress",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#May.delete("Maybe",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.delete("JurassicPark",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.get_all_info(SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Parasite.get_single_info("JurassicPark",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.edit_name(SHOW_DIR_PATH,"MY_SHOW_DB.json","JurassicPark","wow")
#Jurassic.edit_duration(SHOW_DIR_PATH,"MY_SHOW_DB.json","JurassicPark",10)
#Parasite.edit_status(SHOW_DIR_PATH,"MY_SHOW_DB.json","Parasite","In Progress")
#Jurassic.delete_folder("MY_SHOW_DB.json","JurassicPark")


#assert isinstance(Show, Template)
#assert isinstance(Shot, Template)