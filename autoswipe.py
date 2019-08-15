import tkinter as tk
from tkinter import *
from pynput.keyboard import Key, Controller
import time
import random
from random import randint
import threading

##To be used on tinder web-app

##Autoswiper function for low chance of bot detection
def calmswiperr():

    print("Calmswiperr active")
    n=1 ##Likes counter
    m=1 #Dislikes counter
    l=0 #Sleeps counter

    keyboard = Controller()
    time.sleep(10)

    dislike=6 ##variable to use as original mod value for a dislike

    while True: ##loop for if elif else statement
        
        restfloat=random.uniform(0.4, 5) ##time rest inbetween each swipe

        ##sleep
        if n%30==0: 
            print("asleep for 10 minutes, thank you")
            time.sleep(600)
            l=l+1
            n=n+1
            
        ##dislike
        elif n%dislike==0:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print("Dislike, session action", n ,"Definitely not a bot! ;)")
            m=m+1
            time.sleep(restfloat)
            dislike=randint(4,6)
            n=n+1

        ##like
        else:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print("Like, session action", n,"Hopefully a match!", "Next swipe in:", restfloat, "seconds.")
            n=n+1
            time.sleep(restfloat)


##swipes the most and helps elo
def optimalswiperr():
    print("OptimalSwiperr active")
    counter=1 ##Likes counter
    x=1 #Dislikes counter
    b=0 #Sleeps counter

    keyboard = Controller()
    time.sleep(10)

    dislike=6 ##variable to use as original mod value for a dislike

    while True: ##loop for if elif else statement
        
        sleepfloat=random.uniform(1.9, 2.2)##time rest inbetween each swipe

        ##sleep at day limit for 1 hour
        if counter%49000==0: 
            print("program stop for 1 hour, thank you")
            time.sleep(3600)
            b=b+1
            counter=counter+1
            
        ##dislike
        elif counter%dislike==0:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print("Dislike. Session action", counter,"Definitely not a bot! ;)")
            x=x+1
            time.sleep(sleepfloat)
            dislike=randint(4,6)
            counter=counter+1

        ##like
        else:
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print("Session swipe", counter,"Hopefully a match!", "Next swipe in:", sleepfloat, "seconds.")
            counter=counter+1
            time.sleep(sleepfloat)


##Bombs through 1800 right swipes asap. Tanks elo but produces quick results.
def hyperswiperr():
    print("Hyperswiperr active")    
    keyboard = Controller()
    time.sleep(10)

    k=0

    while True:
        if k<1800:

            keyboard.press(Key.right)
            keyboard.release(Key.right)
            time.sleep(0.4)
            k=k+1
            print("Like number:", k)
            
        else:
            time.sleep(3000)
            k=0

##Constructors
window = Tk()
window.title("LazySwiperr")
window.configure(background="black")

Label (window, text="LazySwiperr", bg="black", fg="white", font="none 60 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="Most active and linear, chance of ban.", bg="black", fg="red", font="none 12 bold") .grid(row=3, column=0, sticky=W)
Button(window, text="HyperXX ", width=30, command=hyperswiperr) .grid(row=4, column=0, sticky=W)
Label (window, text="\nLeast likely setting to result in a ban, most natural and elo friendly.", bg="black", fg="green", font="none 12 bold") .grid(row=6, column=0, sticky=W)
Button(window, text="CalmSwiperr", width=30, command=calmswiperr) .grid(row=7, column=0, sticky=W)
Label (window, text="\nBest mix of swiping frequently and risk of not getting banned.", bg="black", fg="orange", font="none 12 bold") .grid(row=9, column=0, sticky=W)
Button(window, text="OptimalSwiperr", width=30, command=optimalswiperr) .grid(row=10, column=0, sticky=W)

