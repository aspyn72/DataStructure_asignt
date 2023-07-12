import os
from os import path as osPath
import sys
import json
import shutil
from typing import List, Dict

# Global variables - FOLDER.
# you should put your directory PATH and folder NAME here / I put those strings for example
    # Directory Path to save Show DB and Shot DB (folders and .json files) inside
TEMP_DIR_PATH = "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST/"
TEMP_NAME = "Show_Shot_DB" 
    # need to put show folder name here to avoid putting the path manually
SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
SHOW_NAME = "JurassicPark"
    # need to put shot folder name here to avoid putting the path manually
SHOT_DIR_PATH = SHOW_DIR_PATH + SHOW_NAME + "/"
SHOT_Name= "01_A"

SHOT_QUANTITY = []


class Template:
    def __init__(self, name : str, duration : int, status:str, path:str):
        self.name = name
        self.duration=duration
        self.status=status
        self.path= path

    def make_directory(self,path: str, name: str):
        folder_dir = os.path.join(path, name)

        if os.path.exists(folder_dir):
            print(f"'{folder_dir}' already exists.")
        else:
            os.makedirs(folder_dir)
            print(f"'{folder_dir}' is created.")

    def create(self,name,duration,status,path,file_json_name):
        data = {
                    "Name": name,
                    "Time Druation": duration,
                    "Status": status,
                    "Shots": [],
                    }
        #self.list_for_org=[]
        filePathNameWExt = path + file_json_name

        print(filePathNameWExt)
        
        if osPath.exists(filePathNameWExt):
            print(".json file exists")
            #self.list_for_org.append(data)
            with open(filePathNameWExt) as file:
                self.list_for_org = json.load(file)
            self.list_for_org.append(data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)
            #for dic in self.list_for_org:

        else:
            print("create .json file")
            #filePathNameWExt = path + file_json_name #+'.json'
            #print(filePathNameWExt)
            #read the file
            self.list_for_org=[]
            #self.list_for_org.append(data)

            with open(filePathNameWExt,'w') as file:
                json.dump(self.list_for_org,file)

            with open(filePathNameWExt) as file:
                self.list_for_org = json.load(file)
            #print the data that we save in our variable type list
            print(self.list_for_org)
            print(type(self.list_for_org))

            self.list_for_org.append(data)

            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)

            print(name+" info is created and added")
            print(type(data))
            print("=== Dictionary SHOW data +++")
            print(data)

    def delete(self,name,path,file_json_name):
        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    #del_dic=deletedinfo[key]
                    #print(deletedinfo[key])
                    #print(val)
                    self.list_for_org.remove(deletedinfo)
                    print("It's deleted")
                    #del self.list_for_org[i]
                    #del deletedinfo[key]
                else:
                    pass
                    #print(str(deletedinfo)+" I'm good")
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    def get_all_info(self,path,file_json_name):
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

    def get_single_info(self,name,path,file_json_name):
        filePathNameWExt = path + file_json_name
        
        
        with open(filePathNameWExt, 'r') as file:
            self.list_to_print = json.load(file)
            print("")
            print("===== Get information =====")
            print("")
            print(self.list_to_print)
            print("")
            print("===== END =====")
            print("")

    # edits
    def edit_name(self,path,file_json_name,name,new_name):
        
        self.data_update_dictionary={"name": name}
        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, mode="rb") as file:
            self.loaded_data_dictionary=json.load(file)
            print(self.loaded_data_dictionary)

        for value in self.data_update_dictionary.values():
            #print(key)
            print(value)
            if self.loaded_data_dictionary.get(value) != None:
                print("load data json filedictionary has this key: ", key )
                self.loaded_data_dictionary[value] = new_name


            else:
                print("NO KEY IN load data json file")


    def edit_duration(self,new_duration):
        self.status=new_duration
        print("Duration is changed to" + new_duration)
    
    def edit_status(self,new_status):
        self.status=new_status
        print("Status is changed to" + new_status)


class Show(Template):

    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOW_NAME
        self.path=SHOW_DIR_PATH

        self.SHOW_DB=[]

    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def create(self, name, duration, status, path, file_json_name):
        return super().create(name, duration, status, path, file_json_name)
    
    def delete(self, name, path, file_json_name):
        return super().delete(name, path, file_json_name)

    def get_single_info(self, name):
        return super().get_single_info(name)

    # edit

    def edit_name(self, path, file_json_name, name, new_name):
        return super().edit_name(path, file_json_name, name, new_name)
    
    def edit_duration(self, new_duration):
        return super().edit_duration(new_duration)
    
    def edit_status(self, new_status):
        return super().edit_status(new_status)


class Shot(Template):
    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOT_Name

        self.SHOT_DB=[]
    
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def create(self, name, duration, status, path, file_json_name):
        return super().create(name, duration, status, path, file_json_name)

    def get_single_info(self, name):
        return super().get_single_info(name)

    '''def read_all_shots(self,filename="ShotList.txt"):
        with open(filename,'r') as file:
            data=json.load(file)
        return Shot(**data)'''
    
    # edit
    def edit_name(self, new_name):
        return super().edit_name(new_name)
    
    def edit_duration(self, new_duration):
        return super().edit_duration(new_duration)
    
    def edit_status(self, new_status):
        return super().edit_status(new_status)

##### TESTing here #####

Jurassic=Show("JurassicPark",50,"Done",SHOW_DIR_PATH)
May=Show("Maybe",40,"Inprogress",SHOW_DIR_PATH)
Parasite=Show("Parasite",90,"Done",SHOW_DIR_PATH)
#Jurassical=Shot("SC1_1",5,"Done","JuJu")
#Jurassic.make_directory(SHOT_DIR_PATH,SHOT_Name)
#May.make_directory(SHOT_DIR_PATH,SHOT_Name)
#May.delete("Maybe",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#May.edit_name(SHOW_DIR_PATH,"MY_SHOW_DB.json","Maybe","Maynot")
#Jurassic.create("JurassicPark",50,"Done",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Parasite.create("Parasite",90,"Done",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.edit_name(SHOW_DIR_PATH,"MY_SHOW_DB.json","JurassicPark","Maynot")
#May.create("Maybe",40,"Inprogress",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#May.delete("Maybe",SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.delete("JurassicPark",SHOW_DIR_PATH,"MY_SHOW_DB.json")
Jurassic.get_all_info(SHOW_DIR_PATH,"MY_SHOW_DB.json")
#Jurassic.delete_folder("MY_SHOW_DB.json","JurassicPark")


#assert isinstance(Show, Template)
#assert isinstance(Shot, Template)