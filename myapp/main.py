import tkinter as tk
import tkinter.ttk as ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# from view import View
# from config import Config
# from contact import Contact
# from function import Function

import tkinter as tk
from tkinter import ttk


class MyApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("My Application")
        self.master.geometry("1012x506")
        self.master.configure(bg = "#545861")
        self.master.resizable(False, False)
        self.ASSETS_PATH =  Path(__file__).parent / Path(r"assets/frame0")  
        self.create_widgets()
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def create_widgets(self):
        self.canvas = Canvas(
            self.master,
            bg = "#545861",
            height = 506,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            215.0,
            0.0,
            1012.0,
            506.0,
            fill="#080707",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_view = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_view.place(
            x=7.0,
            y=133.0,
            width=208.0,
            height=47.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_contact = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_contact.place(
            x=7.0,
            y=283.0,
            width=208.0,
            height=47.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_logout = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_logout.place(
            x=0.0,
            y=441.0,
            width=215.0,
            height=47.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_config = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_config.place(
            x=0.0,
            y=236.0,
            width=208.0,
            height=47.0
        )


        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="HotinGo",
            fill="#FFFFFF",
            font=("Montserrat Bold", 36 * -1)
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        
        self.button_functions = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_functions.place(
            x=3.0,
            y=183.0,
            width=208.0,
            height=47.0
        )
        self.treeview = ttk.Treeview(root)
        self.treeview.pack(fill="both", expand=True)
        self.treeview.insert(self.canvas,)
        self.treeview.insert(self.canvas,)
        self.treeview.insert(self.canvas, )
# Create the main window and run the application
root = tk.Tk()
app = MyApplication(master=root)

app.mainloop()
