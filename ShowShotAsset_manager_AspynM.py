import os
from os import path as osPath
import sys
import json
import shutil
from pathlib import Path
import zipfile


# ======== Global Variables for DIRECTORY (FOLDERS) ========
# you should put your directory PATH and folder NAME here / I put random strings for example
# ****** put Directory Path to save Show DB and Shot DB (folders and .json files) inside ****** #
TEMP_DIR_PATH = "/Users/moon/Desktop/"
TEMP_NAME = "Show_Shot_Asset_DB" 
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

### Parent Class ### for Directory_and_Info functions (common for all classes)
class Base_for_Directory_and_Info:
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

    
    # Read the file you want and print all the content inside the file
    def get_all_info(self, path: str, file_json_name: str ):
         file_path_name_ext = path + file_json_name
         with open(file_path_name_ext, 'r') as file:
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
        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
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
        


### SHOW class (child class) ###
class Show(Base_for_Directory_and_Info):

    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOW_NAME
        self.path=SHOW_DIR_PATH

    # DIRECTORY part
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)
    
    # CREATE shows or shots and will ADD to .json file
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str):
        data = {
                    "Name": name,
                    "Time Duration": duration,
                    "Status": status,
                    "Shots":[]
                    }
        file_path_name_ext = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(file_path_name_ext):
            # in case the file already exists
            print(".json file exists")
            with open(file_path_name_ext) as file:
                self.list_for_org = json.load(file)
            # we put the data(Dictionary) in .json file here
            self.list_for_org.append(data)
            with open(file_path_name_ext,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)
        else:
            # in case the file doesn't exist
            print("created .json file")
            self.list_for_org=[]

            with open(file_path_name_ext,'w') as file:
                json.dump(self.list_for_org,file)

            with open(file_path_name_ext) as file:
                self.list_for_org = json.load(file)

            # we put the data(Dictionary) in .json file here
            self.list_for_org.append(data)
            with open(file_path_name_ext,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)

        # Print results
        print("=== Dictionary Show(or Shot) data ====")
        print(name+" info is created and added")
        print(data)
        print("=== data that exists in the file so far ===")
        print(self.list_for_org)


    # delete specific data from .json file
    def delete(self, name: str, path: str, file_json_name: str):
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
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
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    
    ## INFO part
    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)

    def get_single_info(self, name: str, path: str, file_json_name: str):
        return super().get_single_info(name, path, file_json_name)


     ## EDIT data part ##
    # edit name info
    def edit_name(self, path: str, file_json_name: str, name: str, new_name: str):
        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
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
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

    # edit time duration info - recieve name to pick out the desirable data dictionary
    def edit_duration(self, path: str, file_json_name: str, name: str, new_duration: int):
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
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
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
    
    # edit status info
    def edit_status(self, path: str, file_json_name: str, name: str, new_status: str ):
        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
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
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)



### SHOT class (child of the abstract class) ###
class Shot(Base_for_Directory_and_Info):
    def __init__(self, name: str, duration: int, status: str, path: str):
        super().__init__(name, duration, status, path)
        self.name=SHOT_NAME
        self.path=SHOT_DIR_PATH
    
    def make_directory(self, path: str, name: str):
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)
    
    def create(self, name: str, duration: int, status: str, path: str, file_json_name: str, show_name: str):
        self.show_name=show_name
        
        data = {
                    "Name": name,
                    "Time Duration": duration,
                    "Status": status,
                    "Asset":[]
                    }
                    
        file_path_name_ext = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(file_path_name_ext):
            # in case the file already exists
            print(".json file exists")
            with open(file_path_name_ext) as file:
                self.list_for_shots = json.load(file)
            # we put the data(Dictionary) in .json file here
            self.list_for_shots.append(data)
            with open(file_path_name_ext,mode= "w") as file:
                json.dump(self.list_for_shots,file,indent=4)
        else:
            # in case the file doesn't exist
            print("created .json file")
            self.list_for_shots=[]

            with open(file_path_name_ext,'w') as file:
                json.dump(self.list_for_shots,file)

            with open(file_path_name_ext) as file:
                self.list_for_shots = json.load(file)

            # we put the data(Dictionary) in .json file here
            self.list_for_shots.append(data)
            with open(file_path_name_ext,mode= "w") as file:
                json.dump(self.list_for_shots,file,indent=4)

        # Print results
        print("=== Dictionary Show(or Shot) data ====")
        print(name+" info is created and added")
        print(data)
        print("=== data that exists in the file so far ===")
        print(self.list_for_shots)

            # fetch ShowDB file name
        show_path = osPath.dirname(osPath.abspath(osPath.dirname(path)))
        file_path_of_show = list(Path(show_path).glob("*.json"))
        #show_file_name=os.path.basename(file_path_of_show[0])

        # put shots to show
        with open(file_path_name_ext) as file:
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

        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
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
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

         # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).glob("*.json"))
        show_file_name=os.path.basename(file_path_of_show[0])

        # put edited shots to show
        with open(file_path_name_ext) as file:
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
        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
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
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).glob("*.json"))
        show_file_name=os.path.basename(file_path_of_show[0])

        # put edited shots to show
        with open(file_path_name_ext) as file:
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
        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    deletedinfo['Time Duration']=new_duration
                    print("Time Duration is updated")
                    break
                else:
                    print("=======================================")
                    print("There's nothing named "+str(name))
                    print("=======================================")
                    break
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).glob("*.json"))
        show_file_name=os.path.basename(file_path_of_show[0])

        # put edited shots to show
        with open(file_path_name_ext) as file:
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

        file_path_name_ext = path + file_json_name
        with open(file_path_name_ext, 'r') as file:
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
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        # fetch Show directory
        show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
        file_path_of_show = list(Path(show_path).glob("*.json"))
        show_file_name=os.path.basename(file_path_of_show[0])

        # put edited shots to show
        with open(file_path_name_ext) as file:
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


    # ASSETS FUNC in SHOT
    def create_or_add_assets(self, name:str, asset_name:str, path: str, file_json_name: str, asset_file_json_name:str, show_name: str):
        
        CAT=[]
        file_path_name_ext = path + file_json_name
        asset_file_path_name_w_ext=path+asset_file_json_name
        print(asset_file_path_name_w_ext)

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        with open(asset_file_path_name_w_ext, 'r') as file:
            self.list_for_assets = json.load(file)

        # To get the desired info  
        for deletedinfo in self.list_for_assets:
            for key, val in deletedinfo.items():
                for indi_val in val:
                    if indi_val==asset_name:
                        CAT.append("exist")
                        category=str(key)
                        print(category)
                    else:
                        print("")

        asset_dict={
            category:asset_name
        }

        if CAT==[]:
            print("") 
            print("There is no asset named "+str(name))
            print("Put asset in asset's .json file first.")   
            print("and then try again")      
            print("")     
        else:
            for asset_info in self.list_for_org:
                for key, val in asset_info.items():
                    if val==name:
                        asset_list=asset_info['Asset']
                        asset_list.append(asset_dict)
                        print(str(asset_dict)+"is updated")
                        break
                    else:
                        print("There's nothing named "+str(asset_name))
                        break
        
            with open(file_path_name_ext, 'w') as file:
                json.dump(self.list_for_org, file, indent=4)

            # fetch Show directory
            show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
            file_path_of_show = list(Path(show_path).glob("*.json"))
            show_file_name=os.path.basename(file_path_of_show[0])
            print("=====show_file_name=======")
            print(show_path)
            print(show_file_name)
            print(file_path_of_show[0])
            print("==========================")

            # put edited shots to show
            with open(file_path_name_ext) as file:
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

    def delete_asset(self,name:str,asset_name:str,path:str,file_json_name:str,show_name:str):
        CAT=[]
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # To get the desired info  
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    asset_list=deletedinfo['Asset']
                    print(asset_list)
                    for indi_asset in asset_list:
                        for key, val in indi_asset.items():
                            if val==asset_name:
                                asset_list.remove(indi_asset)
                                deletedinfo['Asset']=asset_list
                                break
                else:
                    break
                    
        if CAT==[]:
            print("") 
            print("There is no asset named "+str(asset_name))
            print("check if you had typo")      
            print("")     
        
            with open(file_path_name_ext, 'w') as file:
                json.dump(self.list_for_org, file, indent=4)

            # fetch Show directory
            show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
            file_path_of_show = list(Path(show_path).glob("*.json"))
            show_file_name=os.path.basename(file_path_of_show[0])
            print("=====show_file_name=======")
            print(show_path)
            print(show_file_name)
            print(file_path_of_show[0])
            print("==========================")

            # put edited shots to show
            with open(file_path_name_ext) as file:
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

    def edit_asset_name(self,name:str,asset_name:str,new_asset_name:str,path:str,file_json_name:str,asset_file_json_name:str ,show_name:str):
        CAT=[]
        file_path_name_ext = path + file_json_name
        asset_file_path_name_w_ext=path+asset_file_json_name
        print(asset_file_path_name_w_ext)

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        with open(asset_file_path_name_w_ext, 'r') as file:
            self.list_for_assets = json.load(file)

        # To get the desired info  
        for deletedinfo in self.list_for_assets:
            for key, val in deletedinfo.items():
                for indi_val in val:
                    if indi_val==asset_name:
                        CAT.append("exist")
                    else:
                        print("")

        if CAT==[]:
            print("") 
            print("There is no asset named "+str(name)+" in asset's JSON file")
            print("Update asset name in the asset's JSON file first.")   
            print("and then try again")      
            print("")     
        else:
            for asset_info in self.list_for_org:
                for key, val in asset_info.items():
                    if val==name:
                        asset_list=asset_info['Asset']
                        for indi_as in asset_list:
                            for key,val in indi_as.items():
                                if val==asset_name:
                                    indi_as[key]=new_asset_name
                                else:
                                    print("There's nothing named "+str(asset_name))
        
            with open(file_path_name_ext, 'w') as file:
                json.dump(self.list_for_org, file, indent=4)

            # fetch Show directory
            show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
            file_path_of_show = list(Path(show_path).glob("*.json"))
            show_file_name=os.path.basename(file_path_of_show[0])

            # put edited shots to show
            with open(file_path_name_ext) as file:
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

            # update asset file too
            with open(asset_file_path_name_w_ext, 'r') as file:
                self.list_for_assets = json.load(file)

            for update_asset in self.list_for_assets:
                for key,val in update_asset.items():
                    for i in val:
                        if i==asset_name:
                            assets_list=update_asset[key]
                            assets_list.remove(asset_name)
                            assets_list.append(new_asset_name)
                            update_asset[key]=assets_list
                        else:
                            pass

            with open(asset_file_path_name_w_ext, 'w') as file:
                json.dump(self.list_for_assets, file, indent=4)
    
    # get asset and shot info seesion

    def find_assets_by_shot(self,name:str,path:str,file_json_name:str):

        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # To get the desired info  
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if val==name:
                    print("")
                    print("----------------------Asset List---------------------------")                    
                    print("Shot '"+str(name)+"' asset list: "+str(deletedinfo['Asset']))
                    print("-----------------------------------------------------------")
                    print("")
                else:
                    pass

    def find_shots_by_asset(self,asset_name:str,path:str,file_json_name:str):

        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # To get the desired info  
        print("----------------------SHOTs---------------------------")  
        for deletedinfo in self.list_for_org:
            for alist in deletedinfo['Asset']:
                for key,val in alist.items():
                    if val==asset_name:
                        print("")                  
                        print("Shot [ "+str(deletedinfo['Name'])+" ] has asset "+str(asset_name))
        print("")
        print("-------------------------------------------------------") 
        
            
                
class Asset(Base_for_Directory_and_Info):

    def __init__(self, name: str, path: str) -> None:
        self.name=name
        self.path=path

    def make_directory(self, path: str, name: str) -> None:
        return super().make_directory(path, name)
    
    def delete_directory(self, path: str, name: str) -> None:
        return super().delete_directory(path, name)

        # isn't inherited from Template class
    def create(self, name: str, category: str, path: str, file_json_name: str) -> None:

        self.category=category
        self.name=name
        self.asset_list_cate=[]
        CAT=[]
        asset_data = {category:self.asset_list_cate}
        file_path_name_ext = path + file_json_name
        
        # check if .json file already exists
        if osPath.exists(file_path_name_ext):
            # in case the file already exists
            print(".json file exists")
            
            with open(file_path_name_ext) as file:
                self.list_for_org = json.load(file)

            for deletedinfo in self.list_for_org:
                for key, val in deletedinfo.items():
                    if key==category:
                        print("   ")
                        print("category exists")
                        print("   ")
                        CAT.append("NoNeedtoProcedd")
                        val.append(name)
                        deletedinfo[category]=val
                        
                        with open(file_path_name_ext,mode= "w") as file:
                            json.dump(self.list_for_org,file,indent=4)
                    else:
                        print("category doesn't exist")
                        break
            
            if CAT==[]:
                self.asset_list_cate.append(name)
                self.list_for_org.append(asset_data)
                with open(file_path_name_ext,mode= "w") as file:
                    json.dump(self.list_for_org,file,indent=4)

        else:
            # in case the file doesn't exist
            print("created .json file")
            self.list_for_org=[]

            with open(file_path_name_ext,'w') as file:
                json.dump(self.list_for_org,file)

            with open(file_path_name_ext) as file:
                self.list_for_org = json.load(file)

            # we put the data(Dictionary) in .json file here
            self.asset_list_cate.append(name)
            self.list_for_org.append(asset_data)
            with open(file_path_name_ext,mode= "w") as file:
                json.dump(self.list_for_org,file,indent=4)

        # Print results
        print("=== data that exists in the file so far ===")
        print(self.list_for_org)
        print("   ")

        return asset_data
    

    # DELETE
    def delete_whole_category(self, category: str, path: str, file_json_name: str):

        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if key==category:
                    self.list_for_org.remove(deletedinfo)
                    print("It's deleted")
                else:
                    print("   ")
                    print("There's nothing named " + category)
                    print("   ")
                    break

         # Update the content of .json file which removed desired show(or shot) data
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
    
    def delete_single_asset(self, name: str, category:str, path: str, file_json_name: str):
        self.val_list=[]
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
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
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)
        
        print("=======Check if it's deleted=======")
        print(self.list_for_org)


    ## GET INFO part
    def get_all_info(self, path: str, file_json_name: str):
        return super().get_all_info(path, file_json_name)

    def get_single_asset_info(self, name: str, path: str, file_json_name: str):
        CAT=[]
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # To get the desired info  
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                for indi_val in val:
                    if indi_val==name:
                        CAT.append("exist")
                        print("=======Asset in Category========")
                        print("   ")
                        print( "[ " + str(name) + " ] is in the [ " + str(key) + " ] category.")
                        print("   ")
                        print("=================================")
                    else:
                        print("")

        if CAT==[]:
            print("There is no asset named "+str(name))
            print("")          
        else:
            pass


    def get_single_category_info(self, category: str, path: str, file_json_name: str):
        CAT=[]
        file_path_name_ext = path + file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        # Modify the data structure to remove the desired dictionary
        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if key==category:
                    CAT.append("exist")
                    print("   ")
                    print("====== Assets in category =======")
                    print("   ")
                    print(deletedinfo)
                    print("   ")
                    print("=================================")
                    print("   ")
                else:
                    print("")
        
        if "exist" in CAT:
            pass
        else:
            print("There is not category named "+category)
            print("")

    def edit_asset(self, name: str, new_name: str, category:str, path: str, file_json_name: str, shot_file_json_name: str, show_name:str):
        CAT=[]
        file_path_name_ext = path + file_json_name
        shot_file_path_name_ext = path + shot_file_json_name

        with open(file_path_name_ext, 'r') as file:
            self.list_for_org = json.load(file)

        for deletedinfo in self.list_for_org:
            for key, val in deletedinfo.items():
                if key==category:
                    list_we_want=deletedinfo[category]
                    for asi in list_we_want:
                        if asi==name:
                            list_we_want.remove(name)
                            list_we_want.append(new_name)
                    break
                else:
                    print("There's nothing named "+name)
                    break
    
        with open(file_path_name_ext, 'w') as file:
            json.dump(self.list_for_org, file, indent=4)

        # Update to shot.json
        with open(shot_file_path_name_ext, 'r') as file:
            self.list_for_sht = json.load(file)

        for editinfo in self.list_for_sht:
            for key,val in editinfo.items():
                if key=="Asset":
                    key_list=editinfo["Asset"]
                    print(key_list)
                    for key_dict in key_list:
                        for key,val in key_dict.items():
                            if val==name:
                                if key==category:
                                    key_dict[category]=new_name
                                    print(key_dict[category])
                                else:
                                    print("-")
                            else:
                                print(" ")
                else:
                    print("")

        with open(shot_file_path_name_ext, 'w') as file:
            json.dump(self.list_for_sht, file, indent=4)

        # fetch Show directory
            show_path = os.path.dirname(os.path.abspath(os.path.dirname(path)))
            file_path_of_show = list(Path(show_path).glob("*.json"))

            # put edited shots to show
            with open(file_path_of_show[0], 'r') as file:
                self.list_for_shows = json.load(file)

            for updateinfo in self.list_for_shows:
                for key, val in updateinfo.items():
                    if val==show_name:
                        updateinfo['Shots']=self.list_for_sht
                        print("Shot is updated")
                        break
                    else:
                        print("There's no show named -> " + str(show_name))
                        break
        
            with open(file_path_of_show[0], 'w') as file:
                json.dump(self.list_for_shows, file, indent=4)





# for archiving
class Zip_to_Archieve():

    def __init__(self, path:str, file_name:str):
        self.path=path
        self.file_name=file_name

    def archive(self,path:str, folder_name:str):
        file_ext=path+folder_name
        zip_filename = f"{folder_name}.zip"
        # to get upper directory path
        show_path = osPath.dirname(path)
        print(show_path)

        if not osPath.exists(file_ext):
            print(f"The file '{file_ext}' does not exist.")
            return
        
        shutil.make_archive(zip_filename[:-4], "zip", path, folder_name)
        shutil.move(zip_filename,show_path)
        shutil.rmtree(file_ext)
    
    def read_zip_file(self, folder_name:str, path:str, zip_filename:str):
        dir_path=path+zip_filename
        file_path=path+zip_filename+'/'+folder_name

        with zipfile.ZipFile(dir_path, 'r') as zip_file:
            try:
                # Read the contents of the file_inside_zip.txt without extracting it
                with zip_file.open(folder_name) as file_in_zip:
                    file_content = file_in_zip.read().decode('utf-8')
                print(file_content)
            except KeyError:
                print(f"The file '{folder_name}' does not exist in the ZIP archive.")





# ========================================================
if __name__ == "__main__":

    # =============== Variables to CALL CLASS ================== #
    # you can use these or create on your own
    ShowFunc=Show("FilmTitle",1000,"Done",SHOW_DIR_PATH)
    ShotFunc=Shot("ShotName",100,"Done",SHOT_DIR_PATH)
    AssetFunc=Asset("AssetName",ASSET_DIR_PATH)
    ArchiveFunc=Zip_to_Archieve(TEMP_DIR_PATH,TEMP_NAME)

    # ======== Use this line below to create DIRECTORY ======== #
        # Below will create Directory in hierarchy [Show_Shot_DB folder <- "Your_Show" folder <- "01_A" folder]
        # You can create show (or shot) folder for different shows (or shots) as many as you want
    ShowFunc.make_directory(SHOW_DIR_PATH,SHOW_NAME)
    ShotFunc.make_directory(SHOT_DIR_PATH,SHOT_NAME)
    AssetFunc.make_directory(ASSET_DIR_PATH,ASSET_NAME) 
    # ========================================================== #
