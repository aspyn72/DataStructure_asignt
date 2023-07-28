import os
from os import path as osPath
import sys
import json
import shutil
from typing import List, Dict
from pathlib import Path


# ======== Global Variables for DIRECTORY (FOLDERS) ========
# you should put your directory PATH and folder NAME here / I put random strings for example
# ****** put Directory Path to save Show DB and Shot DB (folders and .json files) inside ****** #
TEMP_DIR_PATH = "/Users/moon/Desktop/"
TEMP_NAME = "Show_Shot_DB" 
    # need to put show folder name here to avoid putting the path manually
SHOW_DIR_PATH = TEMP_DIR_PATH + TEMP_NAME + "/"
SHOW_NAME = "ShowTitle"
    # need to put shot folder name here to avoid putting the path manually
SHOT_DIR_PATH = SHOW_DIR_PATH + SHOW_NAME + "/"
SHOT_NAME= "01_A"
    # need to put asset folder name here to avoid putting the path manually
ASSET_DIR_PATH  = SHOW_DIR_PATH + SHOW_NAME + "/"
ASSET_NAME= "AssetDB"
# =======================================================

# ======== CLASSes Starts Here ========

### Parent Class ###
class Template:
    def __init__(self, name : str, duration : int, status:str, path:str) -> None:
        self.name = name
        self.duration=duration
        self.status=status
        self.path= path

    # Make Directory (Folder)
    def make_directory(self, path: str, name: str) -> None:
        folder_dir = osPath.join(path, name)
        if osPath.exists(folder_dir):
            print(f"'{folder_dir}' already exists.")
        else:
            os.makedirs(folder_dir)
            print(f"'{folder_dir}' is created.")
    
    def delete_directory(self, path: str, name: str) -> None:
        shutil.rmtree(path+name)

    # CREATE shows or shots and will ADD to .json file
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str) -> None:
        data = {
                    "Name": name,
                    "Time Duration": duration,
                    "Status": status,
                    "Shots":[]
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
                    print("There's nothing named " + name)
                    break

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
            print("============ END =============")
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
                    break
                else:
                    print("There's nothing named "+name)
                    break
        
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
                    print("There's nothing named "+name)
                    break
    
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
                    print("There's nothing named "+name)
                    break
    
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
                    print("There's nothing named" + name)
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)


### SHOW class (child class) ###
class Show(Template):

    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOW_NAME
        self.path=SHOW_DIR_PATH

    # DIRECTORY part
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)
    
    # Create and Delete Show Part
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str):
        return super().create(name, duration, status, path, file_json_name)
    
    def delete(self, name: str, path: str, file_json_name: str):
        return super().delete(name, path, file_json_name)
    
    ## INFO part
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
        self.name=SHOT_NAME
        self.path=SHOT_DIR_PATH
    
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)
    
    def create(self, name: str, duration: int, status: str, assets: list, show_name: str, path: str, file_json_name: str):
        self.show_name=show_name
        data = {
                    "Name": name,
                    "Time Duration": duration,
                    "Status": status,
                    "Asset":assets
                    }
                    
        filePathNameWExt = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(filePathNameWExt):
            # in case the file already exists
            print(".json file exists")
            with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)
            # we put the data(Dictionary) in .json file here
            self.list_for_shots.append(data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_shots,file,indent=4)
        else:
            # in case the file doesn't exist
            print("created .json file")
            self.list_for_shots=[]

            with open(filePathNameWExt,'w') as file:
                json.dump(self.list_for_shots,file)

            with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

            # we put the data(Dictionary) in .json file here
            self.list_for_shots.append(data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_shots,file,indent=4)

        # Print results
        print("=== Dictionary Show(or Shot) data ====")
        print(name+" info is created and added")
        print(data)
        print("=== data that exists in the file so far ===")
        print(self.list_for_shots)

            # fetch ShowDB file name
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)
            print(self.list_for_shows)
            print(data)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's nothing")
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)

        return self.list_for_shots
    
    def delete(self, name: str, path: str, file_json_name: str,show_name: str):

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
                    print("There's no shot named " + str(name))
                    break

         # Update the content of .json file which removed desired show(or shot) data
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

         # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put edited shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's no show named -> " + str(show_name))
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)


    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)
    
    def get_single_info(self, name: str, path: str, file_json_name: str):
        return super().get_single_info(name, path, file_json_name)

 
    ## EDIT part
    def edit_name(self, path: str, file_json_name: str, name: str, new_name: str,show_name: str):
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
                    print("There's nothing named "+name)
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put edited shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)
            print(self.list_for_shows)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's no show named -> " + str(show_name))
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)

    
    def edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int,show_name: str):
        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo['Time Duration']=new_duration
                    print("Time Duration is updated")
                    break
                else:
                    print("There's nothing named "+str(name))
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put edited shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)
            print(self.list_for_shows)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's no show named -> " + str(show_name))
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)

        
    def edit_status(self, path: str, file_json_name: str, name: str, new_status: str,show_name: str):

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
                    print("There's nothing named "+str(name))
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put edited shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)
            print(self.list_for_shows)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's no show named -> " + str(show_name))
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)

    
    def edit_assets(self, path: str, file_json_name: str, name: str, new_assets: list, show_name: str):
        self.path=path
        self.file_json_name=file_json_name
        self.name=name
        self.new_assets=new_assets
        
        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo['Asset']=new_assets
                    print(str(new_assets)+"is updated")
                    break
                else:
                    print("There's nothing named "+str(new_assets))
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).rglob("*"))
        show_file_name=os.path.basename(file_path_of_show[0])
        print("=====show_file_name=======")
        print(show_path)
        print(show_file_name)
        print(file_path_of_show[0])
        print("==========================")

        # put edited shots to show
        with open(filePathNameWExt) as file:
                self.list_for_shots = json.load(file)

        with open(file_path_of_show[0], 'r') as file:
            self.list_for_shows = json.load(file)
            print(self.list_for_shows)

        for updateinfo in self.list_for_shows:
            for key, val in updateinfo.items():
                if val==show_name:
                    updateinfo['Shots']=self.list_for_shots
                    print("Shot is updated")
                    break
                else:
                    print("There's no show named -> " + str(show_name))
                    break
    
        with open(file_path_of_show[0], 'w') as file:
            json.dump(self.list_for_shows, file, indent=4)

        return self.list_for_shots



class Asset(Template):

    def __init__(self, name: str, path: str) -> None:
        self.name=name
        self.path=path

    def make_directory(self, path: str, name: str) -> None:
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)

        # isn't inherited from Template class
    def create(self, category: str, name: str, path: str, file_json_name: str) -> None:

        self.category=category
        self.name=name
        self.asset_list_cate=[]
        CAT=[]
        
        asset_data = {category:self.asset_list_cate}

        filePathNameWExt = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(filePathNameWExt):
            # in case the file already exists
            print(".json file exists")
            
            with open(filePathNameWExt) as file:
                self.list_for_org = json.load(file)

            for deletedinfo in self.list_for_org:
                for key, val in deletedinfo.items():
                    if key==category:
                        print("category exists")
                        CAT.append("NoNeedtoProcedd")
                        val.append(name)
                        deletedinfo[category]=val
                        
                        with open(filePathNameWExt,mode= "w") as file:
                            json.dump(self.list_for_org,file,indent=4)

                    else:
                        print("category doesn't exist")
                        break
            
            if CAT==[]:
                self.asset_list_cate.append(name)
                self.list_for_org.append(asset_data)
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
            self.asset_list_cate.append(name)
            self.list_for_org.append(asset_data)
            with open(filePathNameWExt,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)

        # Print results
        print("=== Dictionary Show(or Shot) data ====")
        print(name+" info is created and added")
        print(asset_data)
        print("=== data that exists in the file so far ===")
        print(self.list_for_org)

        return asset_data
    
    # DELETE
    def delete_whole_category(self, category: str, path: str, file_json_name: str):

        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if key==category:
                    self.list_for_org.remove(deletedinfo)
                    print("It's deleted")
                else:
                    print("There's nothing named " + category)
                    break

         # Update the content of .json file which removed desired show(or shot) data
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
    
    def delete_asset(self, name: str, category:str, path: str, file_json_name: str):
        self.val_list=[]
        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:     
            for key, val in deletedinfo.items():
                if key==category:
                    self.val_list=deletedinfo[key]
                    print(self.val_list)
                    for each_asset in self.val_list:
                        if each_asset==name:
                            self.val_list.remove(name)
                            deletedinfo[key]=self.val_list
                        else:
                            print("Asset named " + str(name))
                else:
                    print("category named " + str(category))
                    
         # Update the content of .json file which removed desired show(or shot) data
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        print("=======Check if it's deleted=======")
        print(self.list_for_org)
        
    # EDIT
    def edit_asset(self, path: str, file_json_name: str, name: str, new_name: str, category:str):

        filePathNameWExt = path + file_json_name
        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo[key]=new_name
                    print("Asset is updated")
                    break
                else:
                    print("There's nothing named "+str(name))
                    break
    
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)
    
    # Have to do this
    def get_single_asset_info(self, name: str, path: str, file_json_name: str):
        filePathNameWExt = path + file_json_name

        cate=""

        print( str(name) + " is in the " + str(cate) + " category.")

    def get_single_category_info ( self, category: str, path: str, file_json_name: str):

        filePathNameWExt = path + file_json_name

        with open(filePathNameWExt, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if key==category:
                    print("   ")
                    print("====== Assets in category =======")
                    print("   ")
                    print(deletedinfo)
                    print("   ")
                    print("=================================")
                    print("   ")
                else:
                    print("-")

         # Update the content of .json file which removed desired show(or shot) data
        with open(filePathNameWExt, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
    


# ========================================================
__name__ == "__main__"

# =============== Variables to CALL CLASS ================== #
# you can use these or create on your own
ShowFunc=Show("FilmTitle",1000,"Done",SHOW_DIR_PATH)
ShotFunc=Shot("ShotName",100,"Done",SHOT_DIR_PATH)
AssetFunc=Asset("AssetName",ASSET_DIR_PATH)

# ======== Use this line below to create DIRECTORY ======== #
    # Below will create Directory in hierarchy [Show_Shot_DB folder <- "Your_Show" folder <- "01_A" folder]
    # You can create show (or shot) folder for different shows (or shots) as many as you want
ShowFunc.make_directory(SHOT_DIR_PATH,SHOT_NAME)
AssetFunc.make_directory(ASSET_DIR_PATH,ASSET_NAME) 
# ========================================================== #

#ShowFunc.create("JuJu",23,"done",SHOW_DIR_PATH,"showDB.json")
#ShotFunc.get_single_info("AA",SHOT_DIR_PATH,"shot.json")
#AssetFunc.get_single_info("Bread",ASSET_DIR_PATH,"ASSET_DB.json") 

#ShowFunc.create("Show",12,"done",SHOW_DIR_PATH,"show.json")

#AssetFunc.create("Costume","Princess Dress",ASSET_DIR_PATH,"ASSET_DB.json")
#AssetFunc.get_all_info(ASSET_DIR_PATH,"ASSET_DB.json")
AssetFunc.get_single_category_info("now",ASSET_DIR_PATH,"ASSETdb.json")

#AssetFunc.delete("Princess Dress",ASSET_DIR_PATH,"ASSET_DB.json")'''