import os
import sys
import json
import shutil
from typing import List, Dict
# directory
#os.makedirs()

# Global variables - FOLDER.
# you should put your directory PATH and folder NAME here
TEMP_DIR_PATH = "/Users/moon/Library/CloudStorage/OneDrive-BCIT/TERM 3/P2_DataStructure/TEST" # you should 
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
    '''
    def create_and_add(self,name,duration,status,filename):
        pass
        #new_show=Show(name, duration, status)
        #self.SHOW_DB.append(new_show)
        with open(filename,'w+') as file:
            json.dump(file,{"name":name,"duration":duration,"status":status})

    def delete_folder(self,name):
        pass
'''
    def get_single_info(self,name):
        print("Name: "+name+" / "+"Duration: "+str(self.duration)+" mins / "+"Status: "+self.status)

#-------
    def get_all_info(self):
        #for i in 
        print("It's all working")

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
    
    def create_and_add(self, name, duration, status, filename):
        return super().create_and_add(name, duration, status, filename)
    
    '''def add_folder(self,filename="filename",name="add_name",duration=70.0,status='si'):
        with open(filename,'w+') as file:
            json.dump(file,{"name":name,"duration":duration,"status":status})'''

    def delete_folder(self, name):
        return super().delete_folder(name)
    
    def get_single_info(self, name):
        return super().get_single_info(name)
    
    '''def delete_folder(self,name):
        removed_show=Show(name)
        self.SHOW_DB.remove(removed_show)

    def get_single_info(self,name):
        print("It's working")'''
    
    def get_all_info(self, name):
        return super().get_all_info(name)

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

    def create_folder(self,name, duration, status):
        new_shot=Shot(name, duration, status)
        self.SHOT_DB.append(new_shot)

    def delete_folder(self,name):
        removed_shot=Shot(name)
        self.SHOT_DB.remove(removed_shot)

    def get_single_info(self, name):
        return super().get_single_info(name)

    def read_all_shots(self,filename="ShotList.txt"):
        with open(filename,'r') as file:
            data=json.load(file)
        return Shot(**data)
    
    # edit
    
    def edit_name(self, new_name):
        return super().edit_name(new_name)
    
    def edit_duration(self, new_duration):
        return super().edit_duration(new_duration)
    
    def edit_status(self, new_status):
        return super().edit_status(new_status)

##### TESTing here #####
Jurassic=Show("JurassicPark",50,"Done","Bao")
Jurassical=Shot("SC1_1",5,"Done","JuJu")
#Jurassic.get_single_info("JurassicPark")

#Template.make_directory(TEMP_DIR_PATH,TEMP_NAME)
Jurassic.make_directory(SHOW_DIR_PATH,SHOW_NAME)
Jurassical.make_directory(SHOT_DIR_PATH,SHOT_Name)

######
#show = Show()
#shot= Shot()

#assert isinstance(Show, Template)
#assert isinstance(Shot, Template)

'''
# Default / Global
#SHOW_DB=[]
#SHOT_DB=[]

# Show class
class Show:
    def __init__(self,name,status,runningTime,director,genre,date):
        self.name=name
        self.status=status
        self.runningTime=runningTime
        self.director=director
        self.genre=genre
        self.date=date

        self.SHOW_DB=[]

        #to refer SHOT CLASS
        self.class_shot_access=Shot()

    def create_show(self,name,status,runningTime,director,genre,date):
        new_show=Show(name,status,runningTime,director,genre,date)
        self.SHOW_DB.append(new_show)

    def delete_show(self,name):
        removed_show=Show(name)
        self.SHOW_DB.remove(removed_show)


        # edit
    def edit_show_status(self,new_show_status):
        self.status=new_show_status

    # have to refer SHOT CLASS
    def create_shot(self,name,status,duration,talent,vfx,date):
        new_shot=Shot(name,status,duration,talent,vfx,date)
        self.class_shot_access.SHOT_DB.append(new_shot)

    def delete_shot(self,name):
        removed_shot=Shot(name)
        self.class_shot_access.SHOT_DB.remove(removed_shot)

        # edit
    def edit_shot_status(self,new_shot_status):
        self.class_shot_access.status=new_shot_status

# Shot class
class Shot(Show):
    def __init__(self,name,status,duration,talent,vfx,date):
        self.name=name
        self.status=status
        self.duration=duration
        self.talent=talent # Yes or No / boolean
        self.vfx=vfx # string
        self.date=date

        self.SHOT_DB=[]'''

