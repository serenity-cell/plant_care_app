import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Plant Care")
root.geometry("600x850")

# main content frame (pack it so it's visible)
content = ttk.Frame(root, padding=10)
content.pack(fill='both', expand=True)

# a button inside the content frame (also packed)
button = ttk.Button(content, text="Done!", command=lambda: print(f"Button pressed!"))
button.pack(pady=20)

root.mainloop()