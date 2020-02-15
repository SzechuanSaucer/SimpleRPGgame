import time
import random
tc=0.1
def start():
    text="Welcome to the simple RPG game. Here you can play a totally unique character\n\
with totally unique abilities in a totally unique world which doesn't exist.\n\
Yes I said word 'totally' three times. Now four. That's not the point. Well anyways,\n\
you can encounter endless hordes of wild or tame beasts. Like The Programmer or even Darth Vader!.\n\
explore the world with endless possibilities*!"
    text2="\n*The world is not really endless."
    text3="\nSorry."
    for char in text:
        print (char, end="", flush=True)
        time.sleep(tc)
    time.sleep(tc*30)
    for char in text2:
        print(char, end="", flush=True)
        time.sleep(tc)
    time.sleep(tc*30)
    for char in text3:
        print(char, end="", flush=True)
        time.sleep(tc)
    print("")
    time.sleep(tc*10)
def name():
    text=("Anyway, let's get started. What is the name of you character? Leaving blank works too!\n")
    for char in text:
        print (char, end="", flush=True)
        time.sleep(tc)
    return(input())
def classe():
    text=("What is your preffered class? Maybe a HeavyHitter? Perhaps a GlassCannon. No, no, a Necro?\n")
    for char in text:
        print (char, end="", flush=True)
        time.sleep(tc)
    return input()
def down():
    x=random.randint(1,5)
    if x==1:
        text="Calm down there chief!"
    elif x==2:
        text="Relax and try again!"
    elif x==3:
        text="You're making me anxious"
    elif x==4:
        text="BEEP, BOOP. Something went wrong."
    elif x==5:
        text="Read the transcripts."
    for char in text:
        print(char, end="", flush=True)
        time.sleep(tc)
    print("")
def simple(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(tc)
    print("\n")