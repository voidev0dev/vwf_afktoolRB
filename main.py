import keyboard
import time
from tkinter import *
import threading
import os
import sys
from PIL import ImageTk
import signal
import webbrowser

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
        sys.exit()
        
def text_main():
    try:
        while True:
            text_enter_got_1 = text_enter_1.get()
            text_enter_got_2 = text_enter_2.get()
            if text_enter_got_1 or text_enter_got_2 or text_enter_got_1 and text_enter_got_2 == None:
                pass
            
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

def dance_main():
    try:
        dance_got = int(emotion_entry.get())
            
        if dance_got == str or dance_got == None:
            pass
            
        time.sleep(5)
        keyboard.press_and_release("/")
        time.sleep(1)
        keyboard.press_and_release("/")
        time.sleep(1)
        if dance_got == 1:
            keyboard.write(f"e dance")
        else:
            keyboard.write(f"e dance{dance_got}")       
        time.sleep(1)
        keyboard.press_and_release("Enter")
    except:
        pass

def dance():
    threading.Thread(target=dance_main).start()
 
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


def clear_main_1(event=None):
    try:
        if text_enter_1.get() == bgtext:
            text_enter_1.delete(0, END)
    except:
        None
        
def add_main_1(event=None):
    try:
        if text_enter_1.get() == '':
            text_enter_1.insert(0, bgtext)
    except:
        None

def add_main_2(event=None):
    try:
        if text_enter_2.get() == '':
            text_enter_2.insert(0, bgtext)
    except:
        None

def clear_main_2(event=None):
    try:
        if text_enter_2.get() == bgtext:
            text_enter_2.delete(0, END)
    except:
        None

def add_seconds_main(event=None):
    try:
        if text_sec_enter.get() == '':
            text_sec_enter.insert(0, bgsec)
    except:
        None
        
def clear_seconds_main(event=None):
    try:
        if text_sec_enter.get() == bgsec:
            text_sec_enter.delete(0, END)
    except:
        None

def add_dance_main(event=None):
    try:
        if emotion_entry.get() == '':
            emotion_entry.insert(0, bgdance)
    except:
        None
        
def clear_dance_main(event=None):
    try:
        if emotion_entry.get() == bgdance:
            emotion_entry.delete(0, END)
    except:
        None


def add_dance(event=None):
    threading.Thread(target=add_dance_main).start()

def clear_dance(event=None):
    threading.Thread(target=clear_dance_main).start() 

def add_seconds(event=None):
    threading.Thread(target=add_seconds_main).start()

def clear_seconds(event=None):
    threading.Thread(target=clear_seconds_main).start()
   
def clear_1(event=None):
    threading.Thread(target=clear_main_1).start()

def add_1(event=None):
    threading.Thread(target=add_main_1).start()

def clear_2(event=None):
    threading.Thread(target=clear_main_2).start()

def add_2(event=None):
    threading.Thread(target=add_main_2).start()
    
# WINDOW 
root = Tk()
root.geometry("500x735+600+200")
root.resizable(False, False)
root['bg']="grey10"
root.title("PL$ ROBUX")
root.overrideredirect(True)
root.attributes("-topmost", True)

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

frame_text = Button(
    frame_title,
    text="PL$ ROBUX [v0.2.0 BETA]",
    font="Courier 12 bold",
    bg="black",
    fg="white",
    borderwidth=0,
    activeforeground='blue',
    activebackground='black',
    command=lambda: webbrowser.open_new_tab("https://discord.gg/PYVJB48Xjx")
)

panel = Tk()
panel.geometry("50x70")
panel.resizable(False, False)
panel['bg'] = 'black'
panel.overrideredirect(True)
panel.attributes("-topmost", True)

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
frame_text.place(y=5, x=7)

'''
×-+
'''

icon_img = ImageTk.PhotoImage(file="img/icon.png")
root.iconphoto(False, icon_img)

frame_title.bind("<B1-Motion>", set_pos)
root.bind('<Escape>', stop)

# IMAGES
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
    width=160,
    height=60,
    activebackground="gray10",
    activeforeground="red",
    command=start_afk,
    image=start_img
)

bgtext = 'Your text here'
bgsec = 'Time'
bgdance = 'Slot'

text_enter_1 = Entry(
    borderwidth=3,
    relief='solid',
    width=20,
    font="Trebuchet 13 bold"
)

text_enter_2 = Entry(
    borderwidth=3,
    relief='solid',
    width=20,
    font="Trebuchet 13 bold"
)

add_1()
add_2()

text_enter_1.bind('<FocusIn>',clear_1)
text_enter_1.bind('<FocusOut>',add_1)

text_enter_2.bind('<FocusIn>',clear_2)
text_enter_2.bind('<FocusOut>',add_2)

enter = Button(
    text="E N T E R",
    bg="gray10",
    fg="red",
    borderwidth=0,
    highlightbackground="gray10",
    highlightcolor="gray10",
    highlightthickness=0,
    width=170,
    height=90,
    activebackground="gray10",
    activeforeground="red",
    command=text,
    image=start_img
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
    font="Courier 23 bold"
)

entry_2 = Label(
    text="2",
    borderwidth=0,
    bg="gray10",
    fg="black",
    font="Courier 23 bold"
)

text_sec_enter = Entry(
    borderwidth=3,
    font="Trebuchet 13 bold",
    width=10,
    relief='solid'
)

add_seconds()

text_sec_enter.bind('<FocusIn>',clear_seconds)
text_sec_enter.bind('<FocusOut>',add_seconds)

text_sec = Label(
    text="TEXT SENDING TIME(S)",
    borderwidth=0,
    bg='gray10',
    fg='black',
    font="Courier 30 bold",
)

stealth_antikick = Label(   
    text="STEALTHY ANTI KICK",
    bg='gray10',
    fg='black',
    font="Courier 30 bold",
    borderwidth=0
)

emotion = Label(
    text="DANCE (1-3)",
    font="Courier 30 bold",
    bg='gray10',
    fg='black',
    borderwidth=0
)

emotion_entry = Entry(
    borderwidth=3,
    font="Trebuchet 13 bold",
    relief='solid',
    width=10
)

add_dance()

emotion_entry.bind('<FocusIn>',clear_dance)
emotion_entry.bind('<FocusOut>',add_dance)

emotion_start = Button(
    bg="gray10",
    fg="red",
    borderwidth=0,
    highlightbackground="gray10",
    highlightcolor="gray10",
    highlightthickness=0,
    width=170,
    height=90,
    activebackground="gray10",
    activeforeground="red",
    command=dance,
    image=start_img
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
entry_1.place(x=130, y=114)
entry_2.place(x=130, y=161)
text_sec.pack(pady=10)
text_sec_enter.pack(pady=10)

enter.pack()

stealth_antikick.pack(pady=10)
start.pack()

emotion.pack(pady=25)
emotion_entry.pack()
emotion_start.pack()

threading.Thread(target=root.mainloop())
threading.Thread(target=panel.mainloop())