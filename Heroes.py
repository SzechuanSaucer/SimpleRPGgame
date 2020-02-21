import numpy as np
class HeavyHitter:
    def __init__(self, name="Chonk"):
        self.description="Heavy hitter hits hard, but fast to take a rest. He doesn't need luck to succeed"
        self.name=name
        self.health=10
        self.attack=5
        self.armor=2
        self.luck=1
        self.energy=10
        self.skills={"heavyhit":"Hits hard as long as you have energy",
                    "hit":"Low powered attack",
                   "jab":"Attack that lets you catch your breath",
                  "recover":"Recover some health and energy"}
    def heavyhit(self):
        if self.energy<5:
            self.health-=2
            self.energy=0
            print("You lost 2 health, you have no energy left!")
        else:
            self.energy-=5
            print("You spent 5 energy")
        hit=2*self.attack*self.luck 
        return (hit)
    def hit(self):
        if self.energy<2:
            self.health-=1
            self.energy=2
            print("You lost 1 health. You have 2 energy")
        else:
            self.energy-=1
            print("You spent 1 energy")
        hit=self.attack*self.luck
        print("You hit for {} damage".format(hit))
        return (hit)
    def jab(self):
        self.energy+=2
        print("You recover 2 energy")
        print("You hit for {} damage".format(attack))
        return 0
    def recover(self):
        self.energy+=5
        self.health+=2
        print("You recover 5 energy and 2 health")
        return 0
class GlassCannon:
    def __init__(self, name="Razor"):
        self.description="Fast to win, fast to die"
        self.name=name
        self.health=20
        self.attack=5
        self.armor=0
        self.luck=1.2
        self.energy=20
        self.skills={"shatter": "Lucky attack",
                    "helplessStrike":"Hits hard when you're out of breath",
                   "energeticStrike":"Use your energy to attack"}
    def shatter(self):
        hit=self.attack*self.luck
        print("You hit for {} damage".format(hit))
        return hit
    def helplessStrike(self):
        if self.energy> 5:
            self.energy-=-5
            print("You lost 5 energy")
        elif self.energy<5:
            self.health-=-5
            self.energy+=10
            print("You lost 5 health and recovered 10 energy")
        hit=np.floor(abs(self.health*self.luck - self.energy/self.luck))
        print("You hit for {} damage".format(hit))
        return hit
    def energeticStrike(self):
        energydifference=np.floor(self.energy-self.energy/self.luck)
        print("You spent {} energy".format(energydifference))
        self.energy-=self.energy/self.luck
        hit=self.energy*self.luck
        print("You hit for {} damage".format(hit))
        return hit
class Necro:
    def __init__(self, name="Vlad"):
        self.description="Fast to win, fast to die"
        self.name=name
        self.health=30
        self.attack=1
        self.armor=4
        self.luck=0.8
        self.energy=5
        self.skills={"drain":"Watch out for low kicks",
                     "trueStrike":"The lower the health, the stronger the impact",
                     "enhance":"You're lucky man. Or ought to be one"}
    def drain(self):
        if self.health<5:
            self.health+=15
            self.energy=0
            print("You recover 15 health. You have no energy left")
            return 0
        elif self.energy<5:
            self.energy+=15
            self.health+=5
            print("You recover 15 energy and 5 health")
            return 0
        else:
            hit=10
            self.energy+=5
            self.health-=5
            print("You recovered 5 energy and lost 5 health")
            print("You hit for {} damage".format(hit))
            return hit
    def trueStrike(self):
        hit=np.floor(self.luck*self.attack*self.energy/self.health)
        print("You recover 1 energy and health")
        self.energy+=1
        self.health+=1
        print("You hit for {} damage".format(hit))
        return hit
    def enhance(self):
        self.health+=2
        self.energy+=2
        self.luck+=0.1
        print("You recover 2 health and 2 energy. Your luck increases slightly")
        return 0