import random
import numpy
class Wild:
    def __init__(self, points):
        self.description="Wild beast. Keep Your distance!"
        self.name="placeholder"
        self.points=points
        self.health=0
        self.attack=0
        self.armor=0
    def getaName(self):
        names=["Grizzly","Goblin","Hobgoblin","Darth Vader","Dwight","Valakas","Antharas", "Onyxxia", "Queen Bee", "Zerg"]
        x=random.randint(0,10)
        self.name = names[x]
    def assignPoints(self,points):
        self.health=points//3
        points-=self.health
        while points>0:
            x=random.randint(0,2)
            if x==0:
                self.health+=1
                points-=1
            elif x==1:
                self.attack+=1
                points-=1
            elif x==2:
                self.armor+=1
                points-=1
class Tame:
    def __init__(self, points):
        self.description="Not as ferral, but still dangerous!"
        self.name="placeholder"
        self.points=points
        self.health=0
        self.attack=0
        self.armor=0
    def getaName(self):
        names=["Starved Programmer", "Angry Analyst", "Lawless Judge", "Nice Guy"]
        x=random.randint(0,4)
        self.name = names[x]
    def assignPoints(self,points):
        self.health=points//2
        points-=self.health
        while points>0:
            x=random.randint(0,3)
            if x==0:
                self.health+=1
                points-=1
            elif x==1:
                self.attack+=1
                points-=1
            elif x==2:
                self.armor+=1
                points-=1
            elif x==3:
                points-=1