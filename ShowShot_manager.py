import os
import json
# directory
#os.makedirs()

class Template:
    def __init__(self, name : str, duration : float, status:str,filename:str):
        self.name = name
        self.duration=duration
        self.status=status
        self.filename=filename

    '''
    def title_or_name(self):
        return self.name
    def runningTime_or_duration(self):
        return self.duration
    def status(self):
        return self.status'''
    
    def create_and_add(self,name,duration,status,filename):
        pass
        #new_show=Show(name, duration, status)
        #self.SHOW_DB.append(new_show)
        with open(filename,'w+') as file:
            json.dump(file,{"name":name,"duration":duration,"status":status})

    def delete_folder(self,name):
        pass

    def get_single_info(self,name):
        print("Name: "+name+" / "+"Duration: "+self.duration+" / "+"Status: "+self.status)

    def get_all_info(self):
        for i in 
        print("It's all working")

    # edits
    def edit_name(self,new_name):
        self.status=new_name

    def edit_duration(self,new_duration):
        self.status=new_duration
    
    def edit_status(self,new_status):
        self.status=new_status


class Show(Template):
    '''def __init__(self):
        super(Show, self).__init__(name="Showtime")
        super(Show, self).__init__(duration=90)
        super(Show, self).__init__(status="In Progress")
        self.SHOW_DB=[]'''
    def __init__(self, name: str, duration: float, status: str, filename: str):
        super().__init__(name, duration, status, filename)
        self.SHOW_DB=[]
    
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
    def __init__(self, name: str, duration: float, status: str, filename: str):
        super().__init__(name, duration, status, filename)
        self.SHOT_DB=[]
    
    def create_folder(self,name, duration, status):
        new_shot=Shot(name, duration, status)
        self.SHOT_DB.append(new_shot)

    def delete_folder(self,name):
        removed_shot=Shot(name)
        self.SHOT_DB.remove(removed_shot)

    def get_single_info(self,name):
        print(name+"It's working")

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
#Jurassic=Show("JurassicPark",50,"Done","Bao")
#Jurassic.get_single_info("JurassicPark")

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



