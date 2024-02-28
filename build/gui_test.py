import tkinter as tk
import tkinter.ttk as ttk

# Create the main window
root = tk.Tk()
root.title("My Application")

# Create a treeview widget
treeview = ttk.Treeview(root)
treeview.pack(fill="both", expand=True)

# Add the root folder to the treeview
root_node = treeview.insert("", "end", text="Root", open=True)

# Add some child nodes to the root folder
treeview.insert(root_node, "end", text="Child 1")
treeview.insert(root_node, "end", text="Child 2")
treeview.insert(root_node, "end", text="Child 3")

# Start the main loop
root.mainloop()
