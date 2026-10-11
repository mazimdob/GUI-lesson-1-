from tkinter import *

root=Tk()
root.title("First App")
root.geometry("250x250")
root.config(background="green")

btn=Button(root,text="click here", bg="yellow", command=root.destroy)
btn.pack(side="bottom")




root.mainloop()
