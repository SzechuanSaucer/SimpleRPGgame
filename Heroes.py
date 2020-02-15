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
    def heavyhit(attack, luck, energy, health):
        if energy<5:
            health-=2
            energy=0
            print("You lost 2 health, you have no energy left!")
        else:
            energy-=5
            print("You spent 5 energy")
        hit=2*attack*luck 
        return (hit, energy, health)
    def hit(attack, luck, energy, health):
        if energy<2:
            health-=1
            energy=2
            print("You lost 1 health. You have 2 energy")
        else:
            energy-=1
            print("You spent 1 energy")
        hit=attack*luck
        print("You hit for {} damage".format(hit))
        return (hit, luck, energy, health)
    def jab(attack,energy):
        energy+=2
        print("You recover 2 energy")
        print("You hit for {} damage".format(attack))
        return attack, energy
    def recover(energy, health):
        energy+=5
        health+=2
        print("You recover 5 energy and 2 health")
        return energy, health
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
    def shatter(attack, luck):
        hit=attack*luck
        print("You hit for {} damage".format(hit))
        return hit
    def helplessStrike(attack, energy, health, luck):
        if energy> 5:
            energy-=-5
            print("You lost 5 energy")
        elif energy<5:
            health-=-5
            energy+=10
            print("You lost 5 health and recovered 10 energy")
        hit=np.floor(abs(health*luck - energy/luck))
        print("You hit for {} damage".format(hit))
        return (hit, energy, health)
    def energeticStrike(energy,luck):
        energydifference=np.floor(energy-energy/luck)
        print("You spent {} energy".format(energydifference))
        energy-=energy/luck
        hit=energy*luck
        print("You hit for {} damage".format(hit))
        return (hit, energy, health)
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
    def drain(health, energy):
        if health<5:
            health+=15
            energy=0
            print("You recover 15 health. You have no energy left")
            return (energy,health)
        elif energy<5:
            energy+=15
            health+=5
            print("You recover 15 energy and 5 health")
            return(energy,health)
        else:
            hit=10
            energy+=5
            health-=5
            print("You recovered 5 energy and lost 5 health")
            print("You hit for {} damage".format(hit))
            return (hit, energy,health)
    def trueStrike(luck,attack,energy):
        hit=np.floor(luck*attack*energy/health)
        print("You recover 1 energy and health")
        energy+=1
        health+=1
        print("You hit for {} damage".format(hit))
        return (hit, energy, health)
    def enhance(energy, luck, health):
        health+=2
        energy+=2
        luck+=0.1
        print("You recover 2 health and 2 energy. Your luck increases slightly")
        return(energy,health)