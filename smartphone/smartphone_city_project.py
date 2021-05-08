from tkinter import *
from PIL import ImageTk,Image

root=Tk()
'''
#Starts with full screen.
root.attributes("-fullscreen",True)'''

#Title of project with icon picture.
root.title('Smartphone city')
root.iconbitmap('smartphone2.ico')
#login window image
var = IntVar()
class Login:
    #making full screen
    def toggle_geom(self,event):
        geom=self.root.winfo_geometry()
        print(geom,self._geom)
        self.root.geometry(self._geom)
        self._geom=geom

    def __init__(self, root):

        self.root = root
        pad=3
        self._geom='200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth()-pad, root.winfo_screenheight()-pad))
        root.bind('<Escape>',self.toggle_geom)
        expression = ""


        #Login background image.
        self.login = ImageTk.PhotoImage(Image.open('login_im.jpg'))
        self.login_img=Label(self.root,image=self.login).place(x=0,y=0,relwidth=1,relheight=1)

        # refister
        register_name = Label(root, text="Registration", font=('Times New Roman', 20, "bold"),bg="white")
        register_name.place(x=630, y=112)
        offer = Label(root, text="(Register and get exciting offer)", font=('Times New Roman', 12),bg="white")
        offer.place(x=605, y=150)

        user_name = Label(root, text="User name ", font=('Times New Roman', 13),bg="white")
        user_name.place(x=580, y=180)
        self.var = StringVar()
        self.name_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque',textvariable=self.var,font=('Times New Roman', 13))
        self.name_display.place(x=670, y=181)

        # gender option

        gender = Label(root, text="Gender        ", font=('Times New Roman', 13),bg="white")
        gender.place(x=580, y=210)
        Radiobutton(root, text="Male", variable=var, bg="white",value=1).place(x=650, y=210)
        Radiobutton(root, text="Female", variable=var, value=2, bg="white").place(x=700, y=210)
        Radiobutton(root, text="Others", variable=var, value=3, bg="white").place(x=762, y=210)
        text = Label(root, text="Email         ", font=('Times New Roman', 13),bg="white")
        text.place(x=580, y=240)
        self.email_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.email_display.place(x=670, y=242)

        text = Label(root, text="Set Password:", font=('Times New Roman', 11), bg="white")
        text.place(x=578, y=270)
        self.password_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.password_display.place(x=670, y=270)
        self.checkButton=Checkbutton(root,text="I agree the terms and conditions.", variable=var,onvalue="0n",offvalue="Off")
        self.checkButton.deselect()
        self.checkButton.place(x=605,y=300)
        self.register = PhotoImage(file='register.png')
        btn_register = Button(root, text="Register", font=('Times New Roman', 15, "bold"),command=self.register_data,bg="white", image=self.register, compound=CENTER,borderwidth=0)
        btn_register.place(x=640, y=330)
        #for login:
        login = Label(root, text="Login Here", font=('Times New Roman', 20, "bold"), bg="white")
        login.place(x=640, y=380)
        offer = Label(root, text="(If you have already registered)", font=('Times New Roman', 12), bg="white")
        offer.place(x=605, y=415)
        login_btn = Button(root, text="Login",bg="white", font=('Times New Roman', 15, "bold"), image=self.register,compound=CENTER, borderwidth=0)
        login_btn.place(x=640, y=440)
        guest_login = Label(root, text="Login as guest", font=('Times New Roman', 20, "bold"), bg="white")
        guest_login.place(x=625, y=490)
        user_name_login = Label(root, text="(No information required)", font=('Times New Roman', 13), bg="white")
        user_name_login.place(x=615, y=525)
        guest = Button(root, text="Guest Login",bg="white", font=('Times New Roman', 15, "bold"), image=self.register, compound=CENTER,borderwidth=0)
        guest.place(x=640, y=545)
    def register_data(self):
        print(self.var.get())
#quit button
obj=Login(root)
root.mainloop()