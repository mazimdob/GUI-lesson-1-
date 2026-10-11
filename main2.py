

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1' 
import tkinter as tk

root=tk.Tk()
root.title("Login me ")
root.geometry("450x300")

username=tk.Label(root,text="username")
username.pack()
username_entry=tk.Entry(root,width=30)
username_entry.pack()














root.mainloop()
