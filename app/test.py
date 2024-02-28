import tkinter as tk

root = tk.Tk()

# Create a menu
menu = tk.Menu(root)

# Create a dropdown menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

# Add the dropdown menu to the main menu
menu.add_cascade(label="File", menu=file_menu)

# Attach the main menu to the root window
root.config(menu=menu)

# Run the application
root.mainloop()
