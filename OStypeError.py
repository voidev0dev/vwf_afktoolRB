from tkinter import *
import pyautogui
import sys
import os
import signal
import threading

screen_cords_x = pyautogui.resolution()[0]
screen_center_x = int(screen_cords_x/2)

screen_cords_y = pyautogui.resolution()[1]
screen_center_y = int(screen_cords_y/2)

class OsTypeError():
    def __init__(self):
            
        error = Tk()
        error['bg'] = 'black'
        error.overrideredirect(1)
        error.geometry(f"500x300+{screen_center_x-250}+{screen_center_y-200}")
        error.attributes("-topmost", True)
        
        warning = Label(
            error,
            text=f'''
            WARNING!
            App is not intended for your OS ({sys.platform})
            ''',
            bg="black",
            fg="red",
            font="Asio 15 bold"
        )
        
        understood = Button(
            error,
            font="Asio 10 bold",
            text="UNDERSTOOD",
            fg="red",
            bg="black",
            activebackground="black",
            activeforeground="red",
            borderwidth=0,
            command=lambda: error.destroy()
        )
        warning.place(x=0, y=30)
        understood.place(x=207, y=120)
        
        error.mainloop()