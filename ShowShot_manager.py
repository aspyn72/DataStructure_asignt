import os
import sys
import json
import shutil
from typing import List, Dict
# directory
#os.makedirs()

# Global variables - FOLDER.
# you should put your directory PATH and folder NAME here / I put those strings for example
TEMP_DIR_PATH = "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST"
TEMP_NAME = "ShowDB"
SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
SHOW_NAME = "Jurassic Park"
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
    #---
    def create_and_add(self,name,duration,status,file_json_name):
        data = {
                "Name": name,
                "Time Druation": duration,
                "Status": status,
                "Shots": [],
                }
        
        #new_show=Show(name, duration, status)
        #self.SHOW_DB.append(new_show)
        with open(file_json_name,'w') as file:
            json.dump(data,file,indent=4)

        print(name+" info is created and added")
        print(type(data))
        print("=== Dictionary SHOW data +++")
        print(data)

    def delete_folder(self,name):
        pass

        print(name+" info is deleted")

    def get_all_info(self):
        print("It's all working")
#---
    def get_single_info(self,name):
        print("Name: "+name+" / "+"Duration: "+str(self.duration)+" mins / "+"Status: "+self.status)

    # edits
    def edit_name(self,new_name):
        self.status=new_name
        print("Name is changed to" + new_name)

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
    
    def create_and_add(self, name, duration, status, file_json_name):
        return super().create_and_add(name, duration, status, file_json_name)

    



    def get_single_info(self, name):
        return super().get_single_info(name)

    # edit

    def edit_name(self, new_name):
        return super().edit_name(new_name)
    
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

Jurassic=Show("JurassicPark",50,"Done","Bao")
#Jurassical=Shot("SC1_1",5,"Done","JuJu")

Jurassic.create_and_add("JurassicPark",50,"Done","MYSHOWDB.json")
#Jurassical.make_directory(SHOT_DIR_PATH,SHOT_Name)'''

#assert isinstance(Show, Template)
#assert isinstance(Shot, Template)