import Heroes
import Enemies
import Loot
import text
import random
text.start()
name=text.name()
while True:
    classe=text.classe().lower()
    if classe=="heavyhitter":
        hero=Heroes.HeavyHitter(name)
        break
    elif classe=="glasscannon":
        hero=Heroes.GlassCannon(name)
        break
    elif classe=="necro":
        hero=Heroes.Necro(name)
        break
    else:
       text.down()
text.simple("Your stats are:")
stats={"health":hero.health,"attack":hero.attack,"armor":hero.armor,"luck":hero.luck,"energy":hero.energy}
for key,value in stats.items():
    print(key,":",value)
text.simple("Your skills are:")
for key,value in hero.skills.items():
    print(key,":",value)
text.simple("If you want me to remind your skills, type 'skills', if you'd like to know how\
 close you're to death, type 'stats'. If you want me to tell you how handsome you are, type\
 'beetlejuice'")
round=1
points=30
while hero.health>0:
    text.simple("Prepare for round:{} ".format(round))  
    choices=[0,1]
    en=random.choices(choices, weights=[3,1])
    if en==[0]:
        monster=Enemies.Tame(points)
    if en==[1]:
        monster=Enemies.Wild(points)
    monster.getaName()
    monster.assignPoints(points)
    enstats={"health":monster.health,"attack":monster.attack,"armor":monster.armor}
    text.simple("Your enemy name is {} ".format(monster.name))
    text.simple("Monster stats are: ")
    for key,value in enstats.items():
        print(key,":",value)
    while hero.health>0 and monster.health>0:
        text.simple("You get to attack! What do you do?")
        do=input()
