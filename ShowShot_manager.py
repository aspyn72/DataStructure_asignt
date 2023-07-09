# directory

# Default / Global
SHOW_DB=[]
SHOT_DB=[]

# Show class
class Show:

    def __init__(self,name,status,runningTime,director,genre,date):
        self.name=name
        self.status=status
        self.runningTime=runningTime
        self.director=director
        self.genre=genre
        self.date=date

        #to refer SHOT CLASS
        self.class_shot_access=Shot()

    def create_show(self,name,status,runningTime,director,genre,date):
        new_show=Show(name,status,runningTime,director,genre,date)
        SHOW_DB.append(new_show)

    def delete_show(self,name):
        removed_show=Show(name)
        SHOW_DB.remove(removed_show)

    def delete_all_show():
        pass

        # edit
    def edit_show_status(self,new_show_status):
        self.status=new_show_status

    # have to refer SHOT CLASS
    def create_shot(self,name,status,duration,talent,vfx,date):
        new_shot=Shot(name,status,duration,talent,vfx,date)
        SHOT_DB.append(new_shot)

    def delete_shot(self,name):
        removed_shot=Shot(name)
        SHOT_DB.remove(removed_shot)

        # edit
    def edit_shot_status(self,new_shot_status):
        self.class_shot_access.status=new_shot_status

# Shot class
class Shot:
    def __init__(self,name,status,duration,talent,vfx,date):
        self.name=name
        self.status=status
        self.duration=duration
        self.talent=talent # Yes or No / boolean
        self.vfx=vfx # string
        self.date=date

