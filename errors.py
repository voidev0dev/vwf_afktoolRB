from tkinter import *
import sys

class ErrorWindow():
    def __init__(self, width, height, text:str, bg, text_font, button_height, button_width):
        root = Tk()
        root.geometry(f"{width}x{height}")
        root['bg'] = bg
        root.resizable(False, False)
        root.title("ERROR")
        
        err_text = Label(
            text=text,
            bg=bg,
            fg='red',
            font=text_font,
            compound='center'
        )
        
        understood = Button(
            text="UNDERSTOOD",
            command=lambda: sys.exit(),
            height=button_height,
            width=button_width,
            bg="black",
            fg="red",
            borderwidth=0
        )
        err_text.pack(pady=50)
        understood.pack(pady=20)
        
        root.mainloop()
