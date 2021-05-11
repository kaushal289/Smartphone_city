from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

root = Tk()
# Title of project with icon picture.
root.title('Smartphone city')
root.iconbitmap('smartphone2.ico')
# for making the full screen.
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
# Login background image.
login = ImageTk.PhotoImage(Image.open('login_im.png'))
login_img = Label(root, image=login).place(x=0, y=0)


# creating a database or connect to one
def mainpage():
    mroot = Toplevel()
    mroot.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    background_img=PhotoImage(file='background1.png')
    #creating a canvas
    my_canvas=Canvas(mroot)
    my_canvas.pack(fill="both",expand=True)
    #setting background image in canvas.
    my_canvas.create_image(0,0,image=background_img,anchor="nw")


    my_img1 = PhotoImage(file='mobile1.png')
    my_img2 = PhotoImage(file='mobile2.png')
    my_img3 = PhotoImage(file='mobile3.png')
    my_img4 = PhotoImage(file='mobile4.png')
    my_img5 = PhotoImage(file='mobile5.png')
    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
    next = ImageTk.PhotoImage(Image.open('next.png'))
    back1 = ImageTk.PhotoImage(Image.open('back.png'))
    my_label = Label(mroot, image=my_img3).place(x=890, y=240)
    my_canvas.create_text(1080,210,text="Some pictures of smartphones:", font=('Times New Roman', 18,"bold"))


    def forward(image_number):
        global my_label
        global button_forward
        global button_back
        my_label = Label(mroot, image=image_list[image_number - 1])
        button_forward = Button(mroot, borderwidth=10, image=next, command=lambda: forward(image_number + 1))
        button_back = Button(mroot, borderwidth=10, image=back1, command=lambda: back(image_number - 1))
        if image_number == 5:
            button_forward = Button(mroot, borderwidth=10, image=next, state=DISABLED)
        my_label.place(x=890, y=240)
        button_back.place(x=1010, y=570)
        button_forward.place(x=1090, y=570)

    def back(image_number):
        global my_label
        global button_forward
        global button_back
        my_label.grid_forget()
        my_label = Label(mroot, image=image_list[image_number - 1])
        button_forward = Button(mroot, borderwidth=10, image=next, command=lambda: forward(image_number + 1))
        button_back = Button(mroot, borderwidth=10, image=back1, command=lambda: back(image_number - 1))
        if image_number == 1:
            button_back = Button(mroot, borderwidth=10, image=back1, state=DISABLED)
        my_label.place(x=890, y=240)
        button_back.place(x=1010, y=570)
        button_forward.place(x=1090, y=570)

    button_back = Button(mroot, borderwidth=10, image=back1, command=lambda: back(1), state=DISABLED)
    button_forward = Button(mroot, borderwidth=10, image=next, command=lambda: forward(1))
    button_back.place(x=1010, y=570)
    button_forward.place(x=1090, y=570)
    my_canvas.create_text(240, 210, text="Search smart-phone by its name.", font=('Times New Roman', 18,"bold"))
    my_canvas.create_text(130, 240, text="Smart-phone name:", font=('Times New Roman', 14))

    smartphone_entry = Entry(mroot, width=17, font=('Times New Roman', 15))
    smartphone_entry.place(x=210, y=230)
    smartphone_search_btn = Button(mroot, text="Search", font=('Times New Roman', 11))
    smartphone_search_btn.place(x=440, y=225)

    my_canvas.create_text(250, 290, text="Search smart-phone by its brand.", font=('Times New Roman', 17, "bold"))

    my_canvas.create_text(130, 320, text="Smart-phone brand:", font=('Times New Roman', 14))

    # list
    brand_list = ['Samsung', 'Oppo', 'Vivo', 'Oneplus', 'Apple', 'Xiaomi']
    c = StringVar()
    droplist = OptionMenu(mroot, c, *brand_list)
    droplist.config(width=14, bg="white", font=('Times New Roman', 13), borderwidth=0)
    c.set('Select brand')
    droplist.place(x=215, y=305)
    brand_search_btn = Button(mroot, text="Search", font=('Times New Roman', 11), bg="white")
    brand_search_btn.place(x=440, y=310)
    my_canvas.create_text(270, 370, text="Search smart-phone by the budget category.", font=('Times New Roman', 17, "bold"))
    my_canvas.create_text(115, 500, text="Budget catogeries:", font=('Times New Roman', 13))

    var1 = IntVar()
    my_canvas.create_rectangle(180,390,430,620,fill="lightblue")
    radio11 = Radiobutton(mroot, text="Entry level(10,000-25,000)", font=('Times New Roman', 12), variable=var1,
                          value=1, bg="lightblue").place(x=190, y=400)
    radio22 = Radiobutton(mroot, text="Lower mid-range(25,000-35000)", font=('Times New Roman', 12), variable=var1,
                          value=2, bg="lightblue").place(x=190, y=430)
    radio33 = Radiobutton(mroot, text="Mid-range(35000-45,000)", font=('Times New Roman', 12), variable=var1, value=3,
                          bg="lightblue").place(x=190, y=460)
    radio44 = Radiobutton(mroot, text="Upper mid-range(50000-60000)", font=('Times New Roman', 12), variable=var1,
                          value=4, bg="lightblue").place(x=190, y=490)
    radio55 = Radiobutton(mroot, text="Lower flag-ship(60,000-80,000)", font=('Times New Roman', 12), variable=var1,
                          value=5, bg="lightblue").place(x=190, y=520)
    radio66 = Radiobutton(mroot, text="Flag-ship(80,000-1,00,000)", font=('Times New Roman', 12), variable=var1,
                          value=6, bg="lightblue").place(x=190, y=550)
    radio77 = Radiobutton(mroot, text="Killer flag-ship(1,00,000-so on) ", font=('Times New Roman', 12), variable=var1,
                          value=7, bg="lightblue").place(x=190, y=580)
    budget_search_btn = Button(mroot, text="Search", font=('Times New Roman', 11), bg="white")
    budget_search_btn.place(x=440, y=490)
    my_canvas.create_text(680, 225, text="Click smart-phone by your \n            requirement.",
                          font=('Times New Roman', 17, "bold"))


    my_canvas.create_rectangle(540,180,825,670,width=3)
    my_canvas.create_line(540, 530, 825, 530, width=3)
    my_canvas.create_rectangle(20, 180, 525, 670, width=3)
    my_canvas.create_rectangle(840, 180, 1325, 670, width=3)
    my_canvas.create_line(20, 270, 525, 270, width=3)
    my_canvas.create_line(20, 350, 525, 350, width=3)

    camera_img = PhotoImage(file='camera.png')
    camera_img_btn=Button(mroot,text="Camera",font=('Times New Roman', 14),image=camera_img,borderwidth=0,compound="top")

    camera_img_btn.place(x=580,y=270)
    game_img = ImageTk.PhotoImage(Image.open('game.png'))
    game_img_btn = Button(mroot, text="Game", font=('Times New Roman', 14), image=game_img, borderwidth=0,
                            compound="top")

    game_img_btn.place(x=700, y=270)

    battery_img =PhotoImage(file='battery.png')
    battery_img_btn = Button(mroot, text="Battery", font=('Times New Roman', 14), image=battery_img, borderwidth=0,
                            compound="top")

    battery_img_btn.place(x=580, y=400)

    G5_img = ImageTk.PhotoImage(Image.open('5G.png'))
    G5_img_btn = Button(mroot, text="5G", font=('Times New Roman', 14), image=G5_img, borderwidth=0,
                          compound="top")

    G5_img_btn.place(x=700, y=400)

    my_canvas.create_text(680, 570, text="You can follow  us  in\n these social platform.",
                          font=('Times New Roman', 17, "bold"))


    facebook_img = PhotoImage(file='facebook.png')
    facebook_img_btn = Button(mroot, image=facebook_img, borderwidth=0)
    facebook_img_btn.place(x=600, y=600)

    insta_img = PhotoImage(file='instagram.png')
    insta_img_btn = Button(mroot, image=insta_img, borderwidth=0)
    insta_img_btn.place(x=660, y=600)

    twitter_img = PhotoImage(file='twitter.png')
    twitter_img_btn = Button(mroot, image=twitter_img, borderwidth=0)
    twitter_img_btn.place(x=720, y=600)

    mroot.mainloop()


conn = sqlite3.connect('address_book.db')
# creating cursor
# cursor class is an instance using which you can invoke methods that
# execute SQLITE statements,fetch data from the result sets of the queries
c = conn.cursor()
# create table
'''c.execute("""CREATE TABLE addresses(
           user_name text,
            address text,
            email text,
            password text
)
""")'''


def submit():
    if user_name.get() == "" or address.get() == "" or email.get() == "" or password.get() == "":
        messagebox.showinfo("Warning", "Please Fill and Select all the question ")
    else:
        messagebox.showinfo("Register", "registered")
        mainpage()
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES(:user_name,:address,:email,:password)", {
        'user_name': user_name.get(),
        'address': address.get(),
        'email': email.get(),
        'password': password.get()
    })
    conn.commit()
    conn.close()
    # clear the text boxes

    user_name.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)
    password.delete(0, END)
    agreement.deselect()
    var.set(None)
    car.set("Select District")


def login_function():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()

    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    c.execute("SELECT *,oid FROM addresses")

    records = c.fetchall()
    print(records)

    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + ' ' + '\t' + str(record[4]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


# create textbox labels
register_name = Label(root, text="Registration", font=('Times New Roman', 20, "bold"), bg="white")
register_name.place(x=650, y=140)
offer = Label(root, text="(Register and get exciting offer)", font=('Times New Roman', 12), bg="white")
offer.place(x=625, y=175)

user_name_label = Label(root, text="User Name", font=('Times New Roman', 13), bg="white")
user_name_label.place(x=600, y=198)

gender_label = Label(root, text="Gender", font=('Times New Roman', 13), bg="white")
gender_label.place(x=600, y=228)

district_label = Label(root, text="District", font=('Times New Roman', 13), bg="white")
district_label.place(x=600, y=258)

address_label = Label(root, text="Address", font=('Times New Roman', 13), bg="white")
address_label.place(x=600, y=288)

email_label = Label(root, text="Email", font=('Times New Roman', 13), bg="white")
email_label.place(x=600, y=318)

password_label = Label(root, text="Set password", font=('Times New Roman', 13), bg="white")
password_label.place(x=600, y=348)

# create text box

user_name = Entry(root, text="", width=16, font=('Times New Roman', 13))
user_name.place(x=695, y=198)

var = StringVar()
var.set(None)
radio1 = Radiobutton(root, text="Male", variable=var, value="1", bg="white").place(x=670, y=228)
radio2 = Radiobutton(root, text="Female", variable=var, value="2", bg="white").place(x=725, y=228)
radio3 = Radiobutton(root, text="Other", variable=var, value="3", bg="white").place(x=790, y=228)

district_list = ['Kathmandu', 'Pokhara', 'Biratnagar', 'Kavre', 'Dhankuta', 'other']
car = StringVar()
car.set('Select District')
droplist = OptionMenu(root, car, *district_list)
droplist.config(width=15, bg="white", font=('Times New Roman', 11), borderwidth=0)

droplist.place(x=695, y=258)

address = Entry(root, width=16, font=('Times New Roman', 13))
address.place(x=695, y=288)

email = Entry(root, width=16, font=('Times New Roman', 13))
email.place(x=695, y=318)

password = Entry(root, width=16, font=('Times New Roman', 13),show="*")
password.place(x=695, y=348)

var1 = StringVar()
var1.set(None)
agreement = Checkbutton(root, text="I agree the terms and conditions.", font=('Times New Roman', 12, "bold"),
                        variable=var1, value=None, bg="white")
agreement.deselect()
agreement.place(x=600, y=370)
# create submit button
register = PhotoImage(file='register.png')
submit_btn = Button(root, text="Register", bg="white", font=('Times New Roman', 15, "bold"), command=submit,
                    image=register, compound=CENTER, borderwidth=0)
submit_btn.place(x=660, y=395)

# commit change
conn.commit()
# close connection
conn.close()


def login_fn():
    global image_login
    lroot = Toplevel()
    lroot.title('Smartphone city')
    lroot.iconbitmap('smartphone2.ico')
    # for making the full screen.
    lroot.geometry("%dx%d+0+0" % (lroot.winfo_screenwidth(), lroot.winfo_screenheight()))
    # Login background image.
    image_login = ImageTk.PhotoImage(Image.open('login.png'))
    login_page_img = Label(lroot, image=image_login).place(x=0, y=0)
    login_inside = Label(lroot, text="Login Here", fg="blue", font=('Times New Roman', 20, "bold"), bg="white")
    login_inside.place(x=660, y=180)
    user_name_label = Label(lroot, text="User Name", font=('Times New Roman', 13), bg="white")
    user_name_label.place(x=600, y=250)
    user_name = Entry(lroot, width=16, font=('Times New Roman', 13))
    user_name.place(x=690, y=250)
    password_label = Label(lroot, text="Password", font=('Times New Roman', 13), bg="white")
    password_label.place(x=600, y=300)
    password = Entry(lroot, width=16, font=('Times New Roman', 13), show="*")
    password.place(x=690, y=300)

    def forget():
        global image_forget
        global login_email_btn
        froot = Toplevel()
        froot.title('Smartphone city')
        froot.iconbitmap('smartphone2.ico')
        # for making the full screen.
        froot.geometry("%dx%d+0+0" % (froot.winfo_screenwidth(), froot.winfo_screenheight()))
        # Login background image.
        image_forget = ImageTk.PhotoImage(Image.open('login.png'))
        forget_page_img = Label(froot, image=image_forget).place(x=0, y=0)
        forgpas = Label(froot, text="Forget Password??", font=('Times New Roman', 20, "bold"), fg="red", bg="white")
        forgpas.place(x=610, y=150)
        warning = Label(froot,
                        text="If you have forget the password \n please  enter the email address you \n have registered during registration.",
                        compound=CENTER, font=('Times New Roman', 13), bg="white")
        warning.place(x=600, y=190)
        warning_email = Label(froot, text="Registered Email", font=('Times New Roman', 15, "bold"), bg="white")
        warning_email.place(x=645, y=270)
        registered_email = Entry(froot, width=22, font=('Times New Roman', 13))
        registered_email.place(x=620, y=300)

        def send():
            submit_btn_img['state'] = NORMAL
            registered_email.delete(0, END)
            messagebox.showwarning("Email send", "5 digit code has ben sent to your email")

        forget_submit_btn = Button(froot, text="SEND", command=send, fg="white", bg="blue",
                                   font=('Times New Roman', 15, "bold"),
                                   borderwidth=0)
        forget_submit_btn.place(x=680, y=340)

        code = Label(froot, text="Enter the 5 digit code \n obtained in your email.",
                     font=('Times New Roman', 12, "bold"), bg="white")
        code.place(x=650, y=390)
        code_entry = Entry(froot, width=22, font=('Times New Roman', 13))
        code_entry.place(x=620, y=430)

        login_email_btn = PhotoImage(file='register.png')
        submit_btn_img = Button(froot, text="Login", bg="white", state=DISABLED, font=('Times New Roman', 15, "bold"),
                                image=login_email_btn, compound=CENTER, borderwidth=0)
        submit_btn_img.place(x=660, y=470)

    forget_btn = Button(lroot, text="Forget password?", command=forget, fg="red", bg="white",
                        font=('Times New Roman', 15, "bold"),
                        borderwidth=0)
    forget_btn.place(x=650, y=350)
    login1_btn = Button(lroot, text="Login", bg="white", font=('Times New Roman', 15, "bold"),
                        image=register, compound=CENTER, borderwidth=0)
    login1_btn.place(x=660, y=400)


login1 = Label(root, text="Login Here", font=('Times New Roman', 20, "bold"), bg="white")
login1.place(x=660, y=439)
offer = Label(root, text="(If you have already registered)", font=('Times New Roman', 12), bg="white")
offer.place(x=630, y=474)
login_btn = Button(root, text="Login", bg="white", font=('Times New Roman', 15, "bold"), command=login_fn,
                   image=register, compound=CENTER, borderwidth=0)
login_btn.place(x=660, y=496)
guest_login = Label(root, text="Login as guest", font=('Times New Roman', 20, "bold"), bg="white")
guest_login.place(x=645, y=545)
user_name_login = Label(root, text="(No information required)", font=('Times New Roman', 12), bg="white")
user_name_login.place(x=645, y=578)
guest = Button(root, command=mainpage, text="Guest Login", bg="white", font=('Times New Roman', 15, "bold"),
               image=register, compound=CENTER, borderwidth=0)
guest.place(x=660, y=600)

root.mainloop()
