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

        #Login background image.
        self.login = ImageTk.PhotoImage(Image.open('login_im.jpg'))
        self.login_img=Label(self.root,image=self.login).place(x=0,y=0,relwidth=1,relheight=1)

        # texts
        register = Label(root, text="Registration", font=('Times New Roman', 20, "bold"),bg="white")
        register.place(x=630, y=112)
        offer = Label(root, text="(Register and get exciting offer)", font=('Times New Roman', 12),bg="white")
        offer.place(x=605, y=145)
        user_name = Label(root, text="User name ", font=('Times New Roman', 13),bg="white")
        user_name.place(x=580, y=180)
        self.name_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.name_display.place(x=670, y=181)
        v_gender = IntVar()
        # gender option
        gender = Label(root, text="Gender        ", font=('Times New Roman', 13),bg="white")
        gender.place(x=580, y=210)
        Radiobutton(root, text="Male",bg="white", variable=v_gender, value=1).place(x=660, y=212)
        Radiobutton(root, text="Female",bg="white", variable=v_gender, value=2).place(x=710, y=212)
        Radiobutton(root, text="Other", bg="white", variable=v_gender, value=3).place(x=771, y=212)
        text = Label(root, text="Email         ", font=('Times New Roman', 13),bg="white")
        text.place(x=580, y=240)
        self.email_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.email_display.place(x=670, y=242)

        text = Label(root, text="Set Password:", font=('Times New Roman', 11), bg="white")
        text.place(x=578, y=270)
        self.password_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.password_display.place(x=670, y=270)
        self.register = PhotoImage(file='register.png')
        register = Button(root, text="Register", font=('Times New Roman', 15, "bold"),bg="white", image=self.register, compound=CENTER,borderwidth=0)
        register.place(x=640, y=300)

        #for login:
        login = Label(root, text="Login", font=('Times New Roman', 20, "bold"), bg="white")
        login.place(x=670, y=340)
        offer = Label(root, text="(If you have already registered)", font=('Times New Roman', 12), bg="white")
        offer.place(x=605, y=375)
        user_name_login = Label(root, text="User name ", font=('Times New Roman', 13), bg="white")
        user_name_login.place(x=580, y=400)
        self.user_name_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.user_name_display.place(x=670, y=403)
        user_password_login = Label(root, text="Password ", font=('Times New Roman', 13), bg="white")
        user_password_login.place(x=580, y=430)
        self.user_password_display = Entry(root, text="", width=17, borderwidth=1, bg='bisque', font=('Times New Roman', 13))
        self.user_password_display.place(x=670, y=430)
        login_btn = Button(root, text="Login",bg="white", font=('Times New Roman', 15, "bold"), image=self.register,compound=CENTER, borderwidth=0)
        login_btn.place(x=640, y=460)
        guest_login = Label(root, text="Login as guest", font=('Times New Roman', 20, "bold"), bg="white")
        guest_login.place(x=625, y=500)
        user_name_login = Label(root, text="(No information required)", font=('Times New Roman', 13), bg="white")
        user_name_login.place(x=615, y=535)
        guest = Button(root, text="Guest Login",bg="white", font=('Times New Roman', 15, "bold"), image=self.register, compound=CENTER,borderwidth=0)
        guest.place(x=640, y=560)
#quit button
obj=Login(root)
root.mainloop()