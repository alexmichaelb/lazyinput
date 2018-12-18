import tkinter as tk
from tkinter import *
from pynput.keyboard import Key, Controller
import time
import random
from random import randint
import threading

##Autoswiper function
def click():

    n=1 ##Likes counter
    m=1 #Dislikes counter
    l=0 #Sleeps counter

    keyboard = Controller()
    time.sleep(20)

    dislike=10 ##variable to use as original mod value for a dislike

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
            keyboard.press(Key.right)
            keyboard.release(Key.right)
            print("Session dislike", m,"Definitely not a bot! ;)")
            m=m+1
            time.sleep(restfloat)
            dislike=randint(7,16)

        ##like
        else:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
            print("Session swipe", n,"Hopefully a match!", "Next swipe in:", restfloat, "seconds.")
            n=n+1
            time.sleep(restfloat)

click()

##Constructors
#window = Tk()
#window.title("LazySwiperr")
#window.configure(background="black")

#Label (window, text="LazySwiperr", bg="black", fg="white", font="none 60 bold") .grid(row=1, column=0, sticky=W)
#Button(window, text="GO!", width=10, command=click) .grid(row=3, column=1, sticky=W)
