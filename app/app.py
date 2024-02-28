import os
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
class DirectoryTreeApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Directory Tree App")
        self.master.geometry("1012x506")
        self.master.configure(bg = "#545861")
        # create left frame for directory tree
        self.master.resizable(False, False)
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
        self.left_frame = tk.Frame(self.canvas, bg='#545861', width=215, height=506)
        self.canvas.create_window((0, 0), window=self.left_frame, anchor='nw')

        self.right_frame = tk.Frame(self.canvas, bg='#080707', width=1012-215, height=506)
        self.canvas.create_window((215, 0), window=self.right_frame, anchor='nw')
        
        text = tk.Label(self.left_frame, bg ='#545861', fg='#FFFFFF',text='HotinGo', font=('Montserrat Bold', 36))
        text.pack()

        self.button_image_1 = PhotoImage(file="/home/baoanh/Desktop/visa_process/app/assets/frame0/button_1.png")
        self.button_show = Button(
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=self.show_content,
                relief="flat"
        )
        self.canvas.create_window(110, 133.0, width=208.0,height=47.0, window=self.button_show)

        self.button_image_2 = PhotoImage(file="/home/baoanh/Desktop/visa_process/app/assets/frame0/button_2.png")
        self.button_contact = Button(
                image=self.button_image_2,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button contact clicked"),
                relief="flat"
        )
        self.canvas.create_window(110, 283.0, width=208.0,height=47.0, window=self.button_contact)

        self.button_image_3 = PhotoImage(file="/home/baoanh/Desktop/visa_process/app/assets/frame0/button_3.png")
        self.button_quit = Button(
                image=self.button_image_3,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button quit clicked"),
                relief="flat"
        )
        self.canvas.create_window(110, 460.0, width=208.0,height=47.0, window=self.button_quit)

        self.button_image_4 = PhotoImage(file="/home/baoanh/Desktop/visa_process/app/assets/frame0/button_4.png")
        self.button_conf = Button(
                image=self.button_image_4,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: print("button_4 clicked"),
                relief="flat"
        )
        self.canvas.create_window(105, 236.0, width=208.0,height=47.0, window=self.button_conf)
        self.button_image_5 = PhotoImage(file="/home/baoanh/Desktop/visa_process/app/assets/frame0/button_5.png")
        self.button_func = Button(
                image=self.button_image_5,
                borderwidth=0,
                highlightthickness=0,
                command=self.show_menu,
                relief="flat"
        )
        
        self.canvas.create_window(105, 183.0, width=208.0,height=47.0, window=self.button_func)


        self.menu = tk.Menu(master, tearoff=0)
        self.menu.add_command(label="Send Message")
        self.menu.add_command(label="Option 2")
        self.menu.add_command(label="Option 3")
        # self.canvas.create_text(28.0,21.0, anchor="nw",text="HotinGo",fill="#FFFFFF",font=("Montserrat Bold", 36 * -1))
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


    def show_content(self):
        table = ttk.Treeview(self.right_frame)
        table["columns"] = ("Name", "Age", "City")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("Name", width=500, anchor=tk.W)
        table.column("Age", width=90, anchor=tk.CENTER)
        table.column("City", width=200, anchor=tk.W)
        table.heading("Name", text="Name")
        table.heading("Age", text="Age")
        table.heading("City", text="City")
        table.insert("", "end", text="1", values=("John Doe", "30", "New York"))
        table.insert("", "end", text="2", values=("Jane Doe", "25", "San Francisco"))
        table.pack()
    def show_menu(self):
        self.menu.tk_popup(self.button_func.winfo_rootx(), 
                           self.button_func.winfo_rooty()+ self.button_func.winfo_height())
    def send_message(self):
        print("send message")
# create main window and run the app
root = tk.Tk()
app = DirectoryTreeApp(root)
root.mainloop()
