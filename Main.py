import Heroes
import Enemies
import Loot
import text
import random
text.start()
name=text.name()
temp=0
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
        while True:
                do=input()
                if do.lower()=="beetlejuice":
                    text.simple("You're quite handsome!")
                if do.lower()=="stats":
                    text.simple("Your stats are:")
                    for key,value in stats.items():
                        print(key,":",value)
                    text.simple("Monster stats are: ")
                    for key,value in enstats.items():
                        print(key,":",value)
                if hero.__class__.__name__=="Necro" and do.lower()=="drain":
                   temp=hero.drain()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="Necro" and do.lower()=="truestrike":
                   temp=hero.trueStrike()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="Necro" and do.lower()=="enhance":
                   temp=hero.enhance()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="GlassCannon" and do.lower()=="shatter":
                   temp=hero.shatter()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="GlassCannon" and do.lower()=="helplessstrike":
                   temp=hero.helplessStrike()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="GlassCannon" and do.lower()=="energeticstrike":
                   temp=hero.energeticStrike()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="HeavyHitter" and do.lower()=="heavyhit":
                   temp=hero.heavyhit()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="HeavyHitter" and do.lower()=="hit":
                   temp=hero.hit()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="HeavyHitter" and do.lower()=="jab":
                   temp=hero.jab()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                elif hero.__class__.__name__=="HeavyHitter" and do.lower()=="recover":
                   temp=hero.recover()
                   monster.health-=temp*temp/(monster.armor+temp)
                   if monster.health<=0:
                       break
                   temp=monster.attack-hero.armor
                   if temp<0:
                       temp=0
                   hero.health=monster.attack-temp
                else:
                    text.simple("You can't do that or you just typed nonsense. Try again.")
                    continue
                break
    if hero.health<=0:
            break
    if monster.health<=0:
        text.simple("You beat {} round(s). Time for the next one!".format(round))
        points+=1
        round+=1
        continue
text.simple("You had a good game, but it's over!")