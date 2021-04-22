from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#Starts with full screen.
root.attributes("-fullscreen",True)
#Title of project with icon picture.
root.title('Smartphone city')
root.iconbitmap('smartphone2.ico')
#login window image
background = ImageTk.PhotoImage(Image.open('login_im.jpg'))
my_label=Label(image=background)
my_label.pack()
#exit button.
exit =PhotoImage(file='clear.png')
exit_button = Button(root, text="Exit",font=('Times New Roman', 20,"bold"),image=exit,compound=CENTER, borderwidth=0,command=root.destroy)
exit_button.place(x=670,y=560)
#texts
text=Label(root,text="Login",font=('Times New Roman', 20,"bold"))
text.place(x=670,y=150)
text=Label(root,text="(Get exciting offer)",font=('Times New Roman', 13))
text.place(x=635,y=190)
text=Label(root,text="Name:",font=('Times New Roman', 13))
text.place(x=590,y=230)
name_display = Entry(root, text="", width=18, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
name_display.place(x=660,y=230)
v_gender=IntVar()
#gender option
gender=Label(root,text="Gender:",font=('Times New Roman', 13))
gender.place(x=590,y=270)
Radiobutton(root,text="Male",variable=v_gender,value=1).place(x=680,y=270)
Radiobutton(root,text="Female",variable=v_gender,value=2).place(x=750,y=270)

text=Label(root,text="Email:",font=('Times New Roman', 13))
text.place(x=590,y=310)
email_display = Entry(root, text="", width=18, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
email_display.place(x=660,y=310)
#quit button

root.mainloop()