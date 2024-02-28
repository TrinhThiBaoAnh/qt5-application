import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter.colorchooser import askcolor
import numpy as np
import math
from tkinter import ttk
import cv2
from datetime import date
from PIL import Image, ImageEnhance, ImageFilter
class TextOnImage:
    def __init__(self, master):
        self.master = master
        self.master.title("Insert Text on Image")
        self.master.geometry("600x600")
        self.img_path = ""
        self.text = ""
        self.brush_color = "black"
        self.coordinates = (0, 0)
        self.font = "font passport/D-DIN-PRO-500-Medium.otf"
        # Create Widgets
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack(side="top", fill="both", expand=True)
        
        self.btn_browse = tk.Button(self.master, text="Browse", command=self.browse_image)
        self.btn_browse.pack(side="left", padx=10, pady=10)

        self.selected_option = tk.StringVar()

        # Create the radio buttons
        self.option1 = tk.Radiobutton(root, text="Cropped Image", variable=self.selected_option, value="crop")
        self.option2 = tk.Radiobutton(root, text="Normal Image", variable=self.selected_option, value="normal")
        # Pack the radio buttons into the window
        self.option1.pack()
        self.option2.pack()

        self.btn_browse = tk.Button(self.master, text="Choose Avatar", command=self.browse_avatar)
        self.btn_browse.pack(side="left", padx=10, pady=10)

        self.btn_browse = tk.Button(self.master, text="Choose Font", command=self.browse_font)
        self.btn_browse.pack(side="left", padx=10, pady=20)
        self.label = tk.Label(self.master, text="")
        self.label.pack(side="left", padx=10, pady=20)
        
        self.btn_insert_text = tk.Button(self.master, text="Insert Name", command=self.insert_text_on_image)
        self.btn_insert_text.pack(side="left", padx=10, pady=30)

        self.text_box = tk.Entry(self.master, width=30)
        self.text_box.pack(side="left", padx=10, pady=30)
        self.btn_save = tk.Button(self.master, text="Save", command=self.save_image)
        self.btn_save.pack(side="left", padx=10, pady=40)

        self.canvas.bind("<Button-1>", self.get_coordinates)
        
    def save_image(self):
        self.image.save("edited.jpg")
        messagebox.showinfo("Notification", "Save!")

    def browse_image(self):
        self.img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.img_path:
            self.show_image_on_canvas()

    def browse_avatar(self):
        self.avt_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.avt_path:
            self.insert_avatar()

    def browse_font(self):
        self.font = filedialog.askopenfilename()
        self.label.config(text="Your font:" + self.font.split("/")[-1])

    def show_image_on_canvas(self):
        self.image = Image.open(self.img_path)
        print('Image shape', self.image.size)
        self.image = self.image.resize((960//2, 1280//2))
        self.img_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.img_tk, anchor="nw")
        
    def insert_avatar(self):
        self.avatar = Image.open(self.avt_path)
        if self.selected_option=='crop':
            print("Here")
            self.avatar = self.avatar.resize((int(self.image.size[0] * 5.4/20.4) , int(self.image.size[1] *4.7/20.7)))
            coordinates2 = (int(0.7*self.image.size[0]/14.8), int(12.9*self.image.size[1]/21.5))
        else:
            self.avatar = self.avatar.resize((108, 156))
            coordinates2 = (42, 383)

        self.image.paste(self.avatar, coordinates2)
        self.img_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.img_tk, anchor="nw")

    def insert_text_on_image(self):
        self.text = self.text_box.get()
        self.text = self.text.upper()
        text1 = self.text.split(" ")[0]
        text2 = self.text.split(" ")[1]
        self.date = "13 April 2023"
        self.id = "1254897634"
        if self.text:
            img_draw = ImageDraw.Draw(self.image)
            if self.selected_option=='crop':
                font = ImageFont.truetype(self.font, size=25)
                coordinates1 = (int(5.2*self.image.size[0]/14.8), int(12.5*self.image.size[1]/21.5))
                coordinates2 = (168, 375)
                coordinates3 = (168, 498)
            else:
                font = ImageFont.truetype(self.font, size=14)
                coordinates1 = (168, 375)
                coordinates2 = (168, 398)
                coordinates3 = (168, 443)
                coordinates4 = (345, 358)
                font_date = ImageFont.truetype(self.font, size=11)
            img_draw.text(coordinates1, text1, fill=self.brush_color, font=font)
            img_draw.text(coordinates2, text2, fill=self.brush_color, font=font)
            img_draw.text(coordinates3, self.date, fill=self.brush_color, font=font_date)
            img_draw.text(coordinates4, self.id, fill=self.brush_color, font=font)
            self.img_tk = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, image=self.img_tk, anchor="nw")

    def get_coordinates(self, event):
        self.coordinates = (event.x, event.y)
        print("Coordinates: ", self.coordinates)

if __name__ == "__main__":
    root = tk.Tk()
    TextOnImage(root)
    root.mainloop()


