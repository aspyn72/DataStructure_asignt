import os
# directory
os.makedirs()

class Template:
    def __init__(self, name=str(""), duration=float(""), status=str("")):
        self._name = name
        self._duration=duration
        self._status=status
    '''
    def title_or_name(self):
        return self.name
    def runningTime_or_duration(self):
        return self.duration
    def status(self):
        return self.status'''
    def create_and_add(self,name,duration,status):
        pass
        #new_show=Show(name, duration, status)
        #self.SHOW_DB.append(new_show)
    def delete(self,name):
        pass
    def get_info(self,name):
        print("It's working")

class Show(Template):
    def __init__(self):
        super(Show, self).__init__(name=str)
        super(Show, self).__init__(duration=)
        super(Show, self).__init__(status)
        self.SHOW_DB=[]
    
    def create_and_add(self,name, duration, status):
        new_show=Show(name,name, duration, status)
        self.SHOW_DB.append(new_show)

     def delete(self,name):
        removed_show=Show(name)
        self.SHOW_DB.remove(removed_show)

    def get_info(self,name):
        print("It's working")

class Shot(Template):
    pass

######
show = Show()
shot= Shot()

assert isinstance(Show, Template)
assert isinstance(Shot, Template)

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



