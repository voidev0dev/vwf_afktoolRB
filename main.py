import keyboard
import time
from tkinter import *
import threading
import os
import sys
from PIL import ImageTk
from errors import *
import signal

# FUNCTIONS 

def start_afk_main():
    try:
        while True:
            time.sleep(10)
            keyboard.press_and_release("w")
            time.sleep(10)
            keyboard.press_and_release('s')
    except:
        root.destroy()
        #ErrorWindow(width=500, height=500, text="Something went wrong with <STEALTHY_ANTI_KICK>. Please reload the app and report us in discord server.", bg="gray10", text_font="Trebuchet 10 bold", button_height=3, button_width=20)
        sys.exit()
        
def text_main():
    try:
        while True:
            text_enter_got_1 = text_enter_1.get()
            text_enter_got_2 = text_enter_2.get()
            if text_enter_got_1 or text_enter_got_2 or text_enter_got_1 and text_enter_got_2 == None:
                pass
                #root.destroy()
                #ErrorWindow(width=500, height=500, text="Text entry cant be empty. Please reload the app", bg="gray10", text_font="Trebuchet 10 bold", button_height=3, button_width=20)
            
            text_sec_enter_got = int(text_sec_enter.get())
            time.sleep(int(text_sec_enter_got))
            keyboard.press_and_release("/")
            time.sleep(1)
            keyboard.write(text_enter_got_1)
            time.sleep(1)
            keyboard.press_and_release("Enter")
            time.sleep(text_sec_enter_got)
            keyboard.press_and_release("/")
            time.sleep(1)
            keyboard.write(text_enter_got_2)
            time.sleep(1)
            keyboard.press_and_release("Enter")
    except:
        pass
        #root.destroy()
        #ErrorWindow(width=500, height=500, text="Something went wrong with <TEXT>. Please reload the app", bg="gray10", text_font="Trebuchet 10 bold", button_height=3, button_width=20)
        #sys.exit()

def text():
    text_thread = threading.Thread(target=text_main)
    text_thread.start()
    
def start_afk():
    afk_thread = threading.Thread(target=start_afk_main)
    afk_thread.start()
    
def stop_main():
    root.quit
    root.destroy
    os.kill(os.getpid(), signal.SIGTERM)
    
def stop():
    threading.Thread(target=stop_main).start()

def start_emotion_main(): 
    try:
        while True:
            emotion_got = emotion.get()
            time.sleep(3)
            keyboard.press(".")
            time.sleep(1)
            keyboard.press(emotion_got)
    except:
        root.destroy()
        ErrorWindow(width=500, height=500, text="Something went wrong with <EMOTION>. Please reload the app", bg="gray10", text_font="Trebuchet 10 bold", button_height=3, button_width=20)
        sys.exit()
        
def start_emotion():
    threading.Thread(target=start_emotion_main).start()


def set_pos(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

def minimize():
    root.state('withdrawn')
    root.overrideredirect(True)

def deploy():
    root.state("normal")
    root.overrideredirect(True)

# WINDOW  
root = Tk()
root.geometry("500x600+600+200")
root.resizable(False, False)
root['bg']='gray10'
root.title("PL$ ROBUX")
root.overrideredirect(True)


frame_title = Frame(
root, 
bg="black"
)

mini = Button(
    frame_title,
    text="-",
    borderwidth=0,
    font="Trebuchet 15 bold",
    bg='black',
    fg='white',
    activebackground='black',
    activeforeground='orange',
    command=minimize
)

close = Button(
    frame_title,
    text="×",
    borderwidth=0,
    font="Trebuchet 15 bold",
    bg='black',
    fg='white',
    activebackground='black',
    activeforeground='red',
    command=stop
)

frame_text = Label(
    frame_title,
    text="PL$ ROBUX [v 0.0.0 BETA]",
    font="Courier 12 bold",
    bg="black",
    fg="white"
)

panel = Tk()
panel.geometry("50x70")
panel.resizable(False, False)
panel['bg'] = 'black'
panel.overrideredirect(True)

panel_button = Button(
    panel,
    text="+",
    font="Trebuchet 30 bold",
    borderwidth=0,
    width=3,
    height=5,
    bg='black',
    fg='white',
    command=deploy,
    activebackground="white",
    activeforeground="black"
)
panel_button.pack()

frame_title.pack(anchor=N, fill=BOTH)
close.pack(side=RIGHT)
mini.pack(side=RIGHT)
frame_text.place(y=7, x=10)

'''
×-+
'''

icon_img = ImageTk.PhotoImage(file="img/icon.png")
root.iconphoto(False, icon_img)

frame_title.bind("<B1-Motion>", set_pos)
root.bind('<Escape>', stop)

# IMAGES
enter_img = ImageTk.PhotoImage(file="img/start.png")
start_img = ImageTk.PhotoImage(file="img/start.png")

# BUTTONS
start = Button(
    text="S T A R T",
    bg="gray10",
    fg="red",
    borderwidth=0,
    highlightbackground="red",
    highlightcolor="red",
    highlightthickness=0,
    width=140,
    height=50,
    activebackground="gray10",
    activeforeground="red",
    command=start_afk,
    image=start_img
)

text_enter_1 = Entry(
    borderwidth=3,
    relief='solid',
    width=20,
    font="Trebuchet 10 bold"
)

text_enter_2 = Entry(
    borderwidth=3,
    relief='solid',
    width=20,
    font="Trebuchet 10 bold"
)

enter = Button(
    text="E N T E R",
    bg="gray10",
    fg="red",
    borderwidth=0,
    highlightbackground="gray10",
    highlightcolor="gray10",
    highlightthickness=0,
    width=150,
    height=60,
    activebackground="gray10",
    activeforeground="red",
    command=text,
    image=enter_img
)

text_spam = Label(
    text="TEXTS",
    borderwidth=0,
    bg='gray10',
    fg='black',
    font="Courier 30 bold",
)

entry_1 = Label(
    text="1",
    borderwidth=0,
    bg="gray10",
    fg="black",
    font="Courier 20 bold"
)

entry_2 = Label(
    text="2",
    borderwidth=0,
    bg="gray10",
    fg="black",
    font="Courier 20 bold"
)

text_sec_enter = Entry(
    borderwidth=3,
    font="Trebuchet 10 bold",
    width=20,
    relief='solid'
)

text_sec = Label(
    text="TEXT SENDING TIME(S)",
    borderwidth=0,
    bg='gray10',
    fg='black',
    font="Courier 28 bold",
)

stealth_antikick = Label(   
    text="STEALTHY ANTI KICK",
    bg='gray10',
    fg='black',
    font="Courier 30 bold",
    borderwidth=0
)

emotion = Label(
    text="EMOTIONS (EMOTION SLOT)",
    font="Courier 30 bold",
    bg='gray10',
    fg='black',
    borderwidth=0
)

emotion_entry = Entry(
    borderwidth=0
)

start_emotion = Button(
    text="S T A R T  A N I M A T I O N",
    bg='black',
    fg='red',
    activeforeground='red',
    activebackground='black',
    highlightbackground='red',
    highlightcolor='red',
    highlightthickness=0,
    borderwidth=0,
    height=1,
    width=25,
    command=start_emotion
    )

text_spam.pack(pady=10)
text_enter_1.pack(pady=10)
text_enter_2.pack(pady=10)
entry_1.place(x=153, y=113)
entry_2.place(x=153, y=156)
text_sec.pack(pady=10)
text_sec_enter.pack(pady=10)

enter.pack(pady=20)

stealth_antikick.pack(pady=10)
start.pack()

threading.Thread(target=root.mainloop())
threading.Thread(target=panel.mainloop())