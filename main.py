import keyboard
import time
from tkinter import *
import threading
import os
import sys
from PIL import ImageTk
import signal
import webbrowser
import win32gui
import pyautogui
from OStypeError import *

if sys.platform != "win32":
    OsTypeError()

#FUNCTIONS
stop_event = threading.Event()
def kill_thread():
    threading.Thread(target=root.destroy()).start()
    os._exit(1)
    sys.exit()

def on_focus_hotkey(event):
    if event.widget == set_hotkey_text:
        set_hotkey_text.configure(text=captured_key_text)
        
    elif event.widget == set_hotkey_afk:
        set_hotkey_afk.configure(text=captured_key_afk)
        
    elif event.widget == set_hotkey_dance:
        set_hotkey_dance.configure(text=captured_key_dance)

def out_focus_hotkey(event):
    if event.widget == set_hotkey_text:
        set_hotkey_text.configure(text="Set hotkey")
        
    elif event.widget == set_hotkey_afk:
        set_hotkey_afk.configure(text="Set hotkey")
        
    elif event.widget == set_hotkey_dance:
        set_hotkey_dance.configure(text="Set hotkey")

# CAPTURING
captured_key_text = None
captured_key_afk = None
captured_key_dance = None
is_capturing = False
capture_timer = None

just_captured_text = False
just_captured_afk = False
just_captured_dance = False
7
def start_capture_text():
    global is_capturing, captured_key_text, capture_timer
    is_capturing = True
    captured_key_text = None
    capture_timer = threading.Timer(3.0, stop_capture_text)
    capture_timer.start()

def stop_capture_text():
    global is_capturing, capture_timer
    if is_capturing:
      is_capturing = False

    elif capture_timer:
      capture_timer.cancel()
        
    set_hotkey_text.configure(text=captured_key_text)

def on_press_text(event_text):
    global captured_key_text, is_capturing, just_captured_text
    if is_capturing:
            captured_key_text = event_text.name
            
            just_captured_text = True
            return
        
    elif captured_key_text == event_text.name and not just_captured_text:
        text()
    just_captured_text = False
    
def activate_capture_text():
    thread_text = threading.Thread(target=start_capture_text)
    thread_text.start()


def start_capture_afk():
    global is_capturing, captured_key_afk, capture_timer
    is_capturing = True
    captured_key_afk = None
    capture_timer = threading.Timer(3.0, stop_capture_afk)
    capture_timer.start()

def stop_capture_afk():
    global is_capturing, capture_timer
    if is_capturing:
      is_capturing = False

    elif capture_timer:
      capture_timer.cancel()

    set_hotkey_afk.configure(text=captured_key_afk)
    
def on_press_afk(event_afk):
    global captured_key_afk, is_capturing, just_captured_afk
    if is_capturing:
        captured_key_afk = event_afk.name
        just_captured_afk = True
        return
    
    elif captured_key_afk == event_afk.name and not just_captured_afk:
        start_afk()

def activate_capture_afk():
    thread_afk = threading.Thread(target=start_capture_afk)
    thread_afk.start()


def start_capture_dance():
    global is_capturing, captured_key_dance, capture_timer
    is_capturing = True
    captured_key_dance = None
    capture_timer = threading.Timer(3.0, stop_capture_dance)
    capture_timer.start()

def stop_capture_dance():
    global is_capturing, capture_timer
    if is_capturing:
      is_capturing = False

    elif capture_timer:
      capture_timer.cancel()

    set_hotkey_dance.configure(text=captured_key_dance)
    
def on_press_dance(event_dance):
    global captured_key_dance, is_capturing, just_captured_dance
    if is_capturing:
        captured_key_dance = event_dance.name
        just_captured_dance = True
        return
    
    elif captured_key_dance == event_dance.name and not just_captured_dance:
        dance()

def activate_capture_dance():
    thread = threading.Thread(target=start_capture_dance)
    thread.start()


def start_afk_main(event=None):
    start.configure(state="disabled")
    try:
        while True:
                time.sleep(535)
                keyboard.press_and_release("w")
                time.sleep(535)
                keyboard.press_and_release('s')
    except:
        pass
        
def text_main(event=None):
    enter.configure(state="disabled")
    try:
        while True:
                text_enter_got_1 = text_enter_1.get()
                text_enter_got_2 = text_enter_2.get()
                if text_enter_got_1 or text_enter_got_2 == None:
                    pass
                    return
                
                text_sec_enter_got = text_sec_enter.get()
                if text_sec_enter_got == 0:
                    return
                
                time.sleep(int(text_sec_enter_got))
                keyboard.press_and_release("/")
                time.sleep(0.2)
                keyboard.write(text_enter_got_1)
                time.sleep(0.2)
                keyboard.press_and_release("Enter")
                time.sleep(int(text_sec_enter_got))
                keyboard.press_and_release("/")
                time.sleep(0.2)
                keyboard.write(text_enter_got_2)
                time.sleep(0.2)
                keyboard.press_and_release("Enter")
                
                start_afk()
    except:
        pass

def dance_main(event=None):
    emotion_start.configure(state="disabled")
    try:
        dance_got = int(emotion_entry.get())
                    
        if dance_got == 0 or dance_got == '':
            pass
            return
                    
        time.sleep(4)
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

def dance(event=None):
    threading.Thread(target=dance_main).start()
 
def text():
    threading.Thread(target=text_main).start()
    
def start_afk():
    threading.Thread(target=start_afk_main).start()
    
def stop_main():
    root.quit
    root.destroy
    os.kill(os.getpid(), signal.SIGTERM)
    
def stop():
    threading.Thread(target=stop_main).start()


# FRAME
root_x = 100
root_y = 100

offset_x = 0
offset_y = 0
moving = False

def start_move(event):
    global moving, offset_x, offset_y, root_x, root_y, target_x, target_y, last_move_time
    moving = True
    offset_x = event.x
    offset_y = event.y
    target_x = root_x
    target_y = root_y
    last_move_time = 0

def move(event):
    global moving, offset_x, offset_y, root_x, root_y, target_x, target_y, last_move_time
    if moving:
      new_x = root_x + event.x - offset_x
      new_y = root_y + event.y - offset_y
      target_x = new_x
      target_y = new_y
      current_time = time.time()
      if (current_time - last_move_time) > 0.01:
        move_window() 
        
def move_window():
    global moving, offset_x, offset_y, root_x, root_y, target_x, target_y, last_move_time
    if moving:
        dx = target_x - root_x
        dy = target_y - root_y
        if abs(dx) > 0.1 or abs(dy) > 0.1:
          root_x += dx * 0.3
          root_y += dy * 0.3
          root.geometry(f"+{int(root_x)}+{int(root_y)}") 
          root.update_idletasks()
          root.after(10, move_window)
        else:
          root.geometry(f"+{int(target_x)}+{int(target_y)}")
          root.update_idletasks()
          root_x = target_x
          root_y = target_y

def stop_move(event):
   global moving, offset_x, offset_y, root_x, root_y, target_x, target_y, last_move_time
   moving = False
   root_x = root.winfo_x()
   root_y = root.winfo_y()
   target_x = root_x
   target_y = root_y

def minimize():
    root.state('withdrawn')
    root.overrideredirect(True)
    
def restore():
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
            text_sec_enter.insert(0, "0")
    except:
        None
        
def clear_seconds_main(event=None):
    try:
        if text_sec_enter.get() == "0":
            text_sec_enter.delete(0, END)
    except:
        None

def add_dance_main(event=None):
    try:
        if emotion_entry.get() == '':
            emotion_entry.insert(0, 0)
    except:
        None
        
def clear_dance_main(event=None):
    try:
        if emotion_entry.get() == "0":
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


def config_bg():
    if root['bg'] == "GhostWhite":
        root.configure(bg="grey10")
        emotion_start.configure(bg="grey10")
        start.configure(bg="grey10")
        enter.configure(bg="grey10")
        text_sec.configure(bg="grey10")
        entry_1.configure(bg="grey10")
        entry_2.configure(bg="grey10")
        text_spam.configure(bg="grey10")
        text_sec.configure(bg="grey10")
        emotion.configure(bg="grey10")
        stealth_antikick.configure(bg="grey10")
        moon.configure(bg="grey10", image=sun_afk_img, activebackground='grey10', activeforeground='GhostWhite')
        stop_button.configure(bg="grey10", activebackground="grey10")
        stop_button_2.configure(bg="grey10", activebackground="grey10")
        stop_button_3.configure(bg="grey10", activebackground="grey10")
        set_hotkey_text.configure(bg="grey10", activebackground="grey10", fg="GhostWhite", activeforeground="GhostWhite")
        set_hotkey_afk.configure(bg="grey10", activebackground="grey10", fg="GhostWhite", activeforeground="GhostWhite")
        set_hotkey_dance.configure(bg="grey10", activebackground="grey10", fg="GhostWhite", activeforeground="GhostWhite")
        moon.place(x=467, y=38)

    elif root['bg'] == "grey10":
        root.configure(bg="GhostWhite")
        emotion_start.configure(bg="GhostWhite")
        start.configure(bg="GhostWhite")
        enter.configure(bg="GhostWhite")
        text_sec.configure(bg="GhostWhite")
        entry_1.configure(bg="GhostWhite")
        entry_2.configure(bg="GhostWhite")
        text_spam.configure(bg="GhostWhite")
        text_sec.configure(bg="GhostWhite")
        emotion.configure(bg="GhostWhite")  
        stealth_antikick.configure(bg="GhostWhite")
        stop_button.configure(bg="GhostWhite", activebackground="GhostWhite")
        stop_button_2.configure(bg="GhostWhite", activebackground="GhostWhite")
        stop_button_3.configure(bg="GhostWhite", activebackground="GhostWhite")
        moon.configure(bg="GhostWhite", image=moon_afk_img, activebackground='GhostWhite', activeforeground='grey10')
        set_hotkey_text.configure(bg="GhostWhite", activebackground="GhostWhite", fg='black', activeforeground='black')
        set_hotkey_afk.configure(bg="GhostWhite", activebackground="GhostWhite", fg='black', activeforeground='black')
        set_hotkey_dance.configure(bg="GhostWhite", activebackground="GhostWhite", fg='black', activeforeground='black')
        moon.place(x=465, y=38)

def config_btn_main():
    while True:
        if is_capturing == True:
            set_hotkey_text.configure(text="Capturing...")
            set_hotkey_afk.configure(text="Capturing...")
            set_hotkey_dance.configure(text="Capturing...")
            
        elif is_capturing == False:
            set_hotkey_text.configure(text="Set hotkey")
            set_hotkey_afk.configure(text="Set hotkey")
            set_hotkey_dance.configure(text="Set hotkey")
        
def config_btn():
    threading.Thread(target=config_btn_main).start()

screen_cords_x = pyautogui.resolution()[0]
screen_center_x = int(screen_cords_x/2)

screen_cords_y = pyautogui.resolution()[1]
screen_center_y = int(screen_cords_y/2)

position = 1
def replace(event=None):
    global position
    if position == 1:
        panel.geometry(f"+{screen_center_x}+0")
        position = 2
        return
            
    elif position == 2:
        panel.geometry(f"+{screen_center_x+screen_center_x-30}+0")
        position = 3
        return

    elif position == 3:
        panel.geometry(f"+0+{screen_cords_y-77}")
        position = 4
        return

    elif position == 4:
        panel.geometry(f"+{screen_center_x+screen_center_x-30}+{screen_center_y+screen_center_y-77}")
        position = 5
        return
    
    elif position == 5:
        panel.geometry(f"30x30+0+0")
        position = 1
        return

# WINDOW
root = Tk()
root.geometry("500x900+700+100")
root.resizable(False, False)
root['bg']="GhostWhite"
root.title("afktoolRB")
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

frame_text = Label(
    frame_title,
    text="AfkToolRB",
    font="Courier 12 bold",
    bg="black", 
    fg="white",
    borderwidth=0,
    activeforeground='white',
    activebackground='black',
)

frame_version = Label(
    frame_title,
    text="[v1.4] by",
    font="Courier 12 bold",
    bg='black',
    fg='white',
    borderwidth=0
)

frame_team = Button(
    frame_title,
    text="VWF Team",
    font="Courier 12 bold",
    borderwidth=0,
    highlightthickness=0,
    activebackground="black",
    bg="black",
    activeforeground="blue",
    fg="light sky blue",
    command=lambda: webbrowser.open_new_tab("https://discord.gg/eeYQkgFRAk")
)

frame_title.pack(anchor=N, fill=BOTH)
close.pack(side=RIGHT)
mini.pack(side=RIGHT)
frame_text.place(y=9, x=3)
frame_version.place(y=9, x=105)
frame_team.place(y=6, x=203)

frame_title.bind("<Button-1>", start_move)
frame_title.bind("<B1-Motion>", move)
frame_title.bind("<ButtonRelease-1>", stop_move)

root.bind('<Escape>', stop)

panel = Tk()
panel.geometry("30x30")
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
    command=restore,
    activebackground="black",
    activeforeground="white",
)
panel_button.pack()

panel_button.bind("<Button-2>", replace)

# IMAGES
start_afk_img = ImageTk.PhotoImage(file="img/start.png")
moon_afk_img = ImageTk.PhotoImage(file="img/moon.png")
sun_afk_img = ImageTk.PhotoImage(file="img/sun.png")
stop_afk_img = ImageTk.PhotoImage(file="img/stop.png")

# BUTTONS
start = Button(
    text="S T A R T",
    bg="GhostWhite",
    fg="red",
    borderwidth=0,
    highlightbackground="red",
    highlightcolor="red",
    highlightthickness=0,
    width=160,
    height=60,
    activebackground="GhostWhite",
    activeforeground="red",
    command=start_afk,
    image=start_afk_img
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
    bg="GhostWhite",
    fg="red",
    borderwidth=0,
    highlightbackground="GhostWhite",
    highlightcolor="GhostWhite",
    highlightthickness=0,
    width=160,
    height=60,
    activebackground="GhostWhite",
    activeforeground="red",
    command=text,
    image=start_afk_img
)

text_spam = Label(
    text="TEXTS",
    borderwidth=0,
    bg='GhostWhite',
    fg='black',
    font="Courier 30 bold",
)

entry_1 = Label(
    text="1",
    borderwidth=0,
    bg="GhostWhite",
    fg="black",
    font="Courier 23 bold"
)

entry_2 = Label(
    text="2",
    borderwidth=0,
    bg="GhostWhite",
    fg="black",
    font="Courier 23 bold"
)

# HOTKEYS
hotkey_text_frame = Frame(root, width=150, height=50, bg='black')
hotkey_text_frame.place(x=344, y=320)

set_hotkey_text = Button(
    hotkey_text_frame,
    text="Set hotkey",
    bg="GhostWhite",
    fg="black",
    activebackground="GhostWhite",
    activeforeground="black",
    font="Courier 13 bold",
    borderwidth=0,
    height=3,
    command=activate_capture_text,
    highlightthickness=0,
)

set_hotkey_afk = Button(
    root,
    text="Set hotkey",
    bg="GhostWhite",
    fg="black",
    activebackground="GhostWhite",
    activeforeground="black",
    font="Courier 13 bold",
    borderwidth=0,
    height=3,
    command=activate_capture_afk,
    highlightthickness=0
)

set_hotkey_dance = Button(
    root,
    text="Set hotkey",
    bg="GhostWhite",
    fg="black",
    activebackground="GhostWhite",
    activeforeground="black",
    font="Courier 13 bold",
    borderwidth=0,
    height=3,
    command=activate_capture_dance,
    highlightthickness=0
)
set_hotkey_text.pack(expand=True)
set_hotkey_afk.place(x=344, y=500)
set_hotkey_dance.place(x=344, y=760)

set_hotkey_afk.bind("<Enter>", on_focus_hotkey)
set_hotkey_dance.bind("<Enter>", on_focus_hotkey)
set_hotkey_text.bind("<Enter>", on_focus_hotkey)

set_hotkey_afk.bind("<Leave>", out_focus_hotkey)
set_hotkey_dance.bind("<Leave>", out_focus_hotkey)
set_hotkey_text.bind("<Leave>", out_focus_hotkey)

config_btn()
keyboard.on_press(on_press_text)
keyboard.on_press(on_press_afk)
keyboard.on_press(on_press_dance)

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
    bg='GhostWhite',
    fg='black',
    font="Courier 30 bold",
)

stealth_antikick = Label(   
    text="STEALTHY ANTI KICK",
    bg='GhostWhite',
    fg='black',
    font="Courier 30 bold",
    borderwidth=0
)

emotion = Label(
    text="DANCE (1-3)",
    font="Courier 30 bold",
    bg='GhostWhite',
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
    bg="GhostWhite",
    fg="red",
    borderwidth=0,
    highlightbackground="GhostWhite",
    highlightcolor="GhostWhite",
    highlightthickness=0,
    width=160,
    height=60,
    activebackground="GhostWhite",
    activeforeground="red",
    command=dance,
    image=start_afk_img
)

stop_button = Button(
    root,
    image=stop_afk_img,
    font="Courier 15 bold",
    fg="red",
    bg="GhostWhite",
    borderwidth=0,
    activebackground="GhostWhite",
    command=kill_thread
)

stop_button_2 = Button(
    root,
    image=stop_afk_img,
    font="Courier 15 bold",
    fg="red",
    bg="GhostWhite",
    borderwidth=0,
    width=117,
    height=40,
    command=kill_thread
)

stop_button_3 = Button(
    root,
    image=stop_afk_img,
    font="Courier 15 bold",
    fg="red",
    bg="GhostWhite",
    borderwidth=0,
    width=117,
    height=40,
    command=kill_thread
)

moon = Button(
    root,
    bg='GhostWhite',
    borderwidth=0,
    activebackground='GhostWhite',
    activeforeground='Black',
    highlightthickness=0,
    image=moon_afk_img,
    command=config_bg
)

moon.place(x=470, y=40)

text_spam.pack(pady=10)
text_enter_1.pack(pady=10)
text_enter_2.pack(pady=10)
entry_1.place(x=130, y=114)
entry_2.place(x=130, y=161)
text_sec.pack(pady=10)
text_sec_enter.pack(pady=10)
enter.pack()
stop_button.pack()

stealth_antikick.pack(pady=10)
start.pack()
stop_button_2.pack()

emotion.pack(pady=25)
emotion_entry.pack()
emotion_start.pack(pady=10)
stop_button_3.pack()

threading.Thread(target=root.mainloop()).start()