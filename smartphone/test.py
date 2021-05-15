from tkinter import  *
root=Tk()
root.geometry('500x500')
MODES=[
    ("a","a"),
    ("b","b"),
    ("c","c")

]
pizza=StringVar()
pizza.set("a")
frame=LabelFrame(root,text="",padx=50,pady=50)
frame.place(x=250,y=250)
for text,mode in MODES:
    Radiobutton(frame,text=text,variable=pizza,value=mode).pack(anchor=W)

root.mainloop()