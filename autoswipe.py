import tkinter as tk
from tkinter import *
from pynput.keyboard import Key, Controller
import time

def click():

    n=0

    keyboard = Controller()

    time.sleep(20)

    while True:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        n=n+1
        print("Session swipe", n,"Hopefully a match!")
        time.sleep(0.4)

window = Tk()
window.title("LazySwiperr")
window.configure(background="black")

Label (window, text="LazySwiperr", bg="black", fg="white", font="none 60 bold") .grid(row=1, column=0, sticky=W)

Button(window, text="GO!", width=10, command=click) .grid(row=3, column=1, sticky=W)

    
