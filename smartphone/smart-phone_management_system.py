from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3

root = Tk()
# Title of project with icon picture.
root.title('Smartphone management system(Registration and login)')
root.iconbitmap('smartphone2.ico')
# for making the full screen.
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
# Login background image.
login = ImageTk.PhotoImage(Image.open('login_im.png'))
login_img = Label(root, image=login).place(x=0, y=0)

# Databases
# Create a databases for user login.
conn = sqlite3.connect('login_sqlite.db')
# Create cursor
c = conn.cursor()
'''
# Create table
c.execute(""" CREATE TABLE login(
      user_name text,
      password text,
      email text
) """)
'''

# commit change
conn.commit()
# close connection
conn.close()


# This is the function of the page after you login or register.
def mainpage():
    root.withdraw()
    mroot = Toplevel()
    mroot.title('Smartphone Management System')
    mroot.iconbitmap('smartphone2.ico')
    mroot.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    background_img = PhotoImage(file='background1.png')
    # creating a canvas
    my_canvas = Canvas(mroot)
    my_canvas.pack(fill="both", expand=True)
    # setting background image in canvas.
    my_canvas.create_image(0, 0, image=background_img, anchor="nw")
    # Images that you can change by pressing button.
    my_img1 = PhotoImage(file='mobile1.png')
    my_img2 = PhotoImage(file='mobile2.png')
    my_img3 = PhotoImage(file='mobile3.png')
    my_img4 = PhotoImage(file='mobile4.png')
    my_img5 = PhotoImage(file='mobile5.png')
    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
    next = ImageTk.PhotoImage(Image.open('next.png'))
    back1 = ImageTk.PhotoImage(Image.open('back.png'))
    my_label = Label(mroot, image=my_img3).place(x=890, y=240)
    my_canvas.create_text(1080, 210, text="Some pictures of smartphones:", font=('Times New Roman', 18, "bold"))

    # Function for changing image forward or backward.
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

    # Function for changing image forward or backward.
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

    # function for the smartphone to search by its name.
    def info_page():
        global smartphone_search_page_img
        iroot = Toplevel()
        iroot.geometry("%dx%d+0+0" % (iroot.winfo_screenwidth(), iroot.winfo_screenheight()))
        iroot.title('Smartphone Management System')
        iroot.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(iroot, image=smartphone_search_page_img).place(x=0, y=0)

        # Connect to userdatabase
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c = conn.cursor()
        # query of the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        # Loop through the results
        global go_backimg
        for record in records:
            if str(record[0]) == (smartphone_entry.get()).lower():
                try:
                    sm_name = Label(iroot, text=str(record[0]), font=("Times New Roman", 14))
                    sm_name.place(x=210, y=220)

                    sm_brand = Label(iroot, text=str(record[1]), font=("Times New Roman", 14))
                    sm_brand.place(x=430, y=220)

                    sm_chipset = Label(iroot, text=str(record[2]), font=("Times New Roman", 14))
                    sm_chipset.place(x=520, y=220)

                    sm_GPU = Label(iroot, text=str(record[3]), font=("Times New Roman", 14))
                    sm_GPU.place(x=690, y=220)

                    sm_RAM = Label(iroot, text=str(record[4]), font=("Times New Roman", 14))
                    sm_RAM.place(x=860, y=220)

                    sm_storage = Label(iroot, text=str(record[5]), font=("Times New Roman", 14))
                    sm_storage.place(x=930, y=220)

                    sm_price = Label(iroot, text="Rs" + str(record[6]), font=("Times New Roman", 14))
                    sm_price.place(x=1010, y=220)

                    sm_speciality = Label(iroot, text=str(record[7]), font=("Times New Roman", 14))
                    sm_speciality.place(x=1115, y=220)



                except:
                    pass
        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(iroot, image=go_backimg, borderwidth=5, command=iroot.destroy)
        go_back.place(x=610, y=550)
        conn.commit()
        conn.close()

        smartphone_name1 = Label(iroot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(iroot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(iroot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(iroot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                            y=177)
        RAM1 = Label(iroot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                            y=177)

        storage1 = Label(iroot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(iroot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                y=177)

        speciality1 = Label(iroot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)

    # function to check if the smartphone entered by user matches to the database or not.
    def samrtphone_name_search():
        # Connecring to database
        conn = sqlite3.connect('address_book2.db')
        # Creating  cursor
        c = conn.cursor()
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        # Loop through the results
        for record in records:
            if str(record[0]) == (smartphone_entry.get()).lower():
                try:
                    return info_page()

                except:
                    pass
            elif smartphone_entry.get() == "":
                try:
                    return messagebox.showinfo("Sorry", "Please enter name of mobile", parent=mroot)
                except:
                    pass

        return messagebox.showinfo("Sorry", "No such smartphone was found.", parent=mroot)

        a = 1

        conn2.commit()
        conn2.close()

    button_back = Button(mroot, borderwidth=10, image=back1, command=lambda: back(1), state=DISABLED)
    button_forward = Button(mroot, borderwidth=10, image=next, command=lambda: forward(1))
    button_back.place(x=1010, y=570)
    button_forward.place(x=1090, y=570)
    my_canvas.create_text(240, 210, text="Search smart-phone by its name.", font=('Times New Roman', 18, "bold"))
    my_canvas.create_text(130, 240, text="Smart-phone name:", font=('Times New Roman', 14))

    smartphone_entry = Entry(mroot, width=17, font=('Times New Roman', 15))
    smartphone_entry.place(x=210, y=230)
    search_img = PhotoImage(file='search.png')
    smartphone_search_btn = Button(mroot, text="Search", command=samrtphone_name_search, image=search_img,
                                   borderwidth=0, compound=CENTER, fg="white",
                                   font=('Times New Roman', 14, "bold"))
    smartphone_search_btn.place(x=440, y=225)

    my_canvas.create_text(250, 290, text="Search smart-phone by its brand.", font=('Times New Roman', 17, "bold"))

    my_canvas.create_text(130, 320, text="Smart-phone brand:", font=('Times New Roman', 14))

    # function to search smartphone by its brand using database.
    def brand_page():
        global smartphone_search_page_img
        global go_backimg
        broot = Toplevel()
        broot.geometry("%dx%d+0+0" % (broot.winfo_screenwidth(), broot.winfo_screenheight()))
        broot.title('Smartphone Management System')
        broot.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(broot, image=smartphone_search_page_img).place(x=0, y=0)

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()
        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""
        # Loop through the results
        for record in records:
            try:
                if str(record[1]) == c.get():
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"
                sm_label = Label(broot, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(broot, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(broot, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(broot, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(broot, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(broot, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(broot, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(broot, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)

            except:
                pass

        smartphone_name1 = Label(broot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(broot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(broot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(broot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                            y=177)
        RAM1 = Label(broot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                            y=177)

        storage1 = Label(broot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(broot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                y=177)

        speciality1 = Label(broot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)

        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(broot, image=go_backimg, borderwidth=5, command=broot.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    # function to check if user has selected any brand or not.
    def brand_name_search():
        # Connecting to database
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        co = conn.cursor()
        # query of the database
        co.execute("SELECT *, oid FROM addresses")
        records = co.fetchall()
        # Loop through the results

        for record in records:
            if str(record[1]) == c.get():
                try:
                    return brand_page()

                except:
                    pass

        return messagebox.showinfo("Sorry", "Plese select brand", parent=mroot)
        a = 1

        conn2.commit()
        conn2.close()

    # list
    brand_list = ['Samsung', 'Oppo', 'Vivo', 'Oneplus', 'Apple', 'Xiaomi']
    c = StringVar()
    droplist = OptionMenu(mroot, c, *brand_list)
    droplist.config(width=14, bg="white", font=('Times New Roman', 13), borderwidth=0)
    c.set('Select brand')
    droplist.place(x=215, y=305)
    brand_search_btn = Button(mroot, text="Search", image=search_img, borderwidth=0, compound=CENTER, fg="white",
                              command=brand_name_search,
                              font=('Times New Roman', 14, "bold"))
    brand_search_btn.place(x=440, y=310)
    my_canvas.create_text(270, 370, text="Search smart-phone by the budget category.",
                          font=('Times New Roman', 17, "bold"))
    my_canvas.create_text(115, 500, text="Budget catogeries:", font=('Times New Roman', 13))

    # Function to search smartphone by the user budget using database.
    def radio_page():
        global smartphone_search_page_img
        global go_backimg
        rroot = Toplevel()
        rroot.geometry("%dx%d+0+0" % (rroot.winfo_screenwidth(), rroot.winfo_screenheight()))
        rroot.title('Smartphone Management System')
        rroot.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(rroot, image=smartphone_search_page_img).place(x=0, y=0)

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()

        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""
        # Loop through the results
        for record in records:
            try:
                if (var1.get() == "Entry level(10,000-25,000)" and int("10000") < int(record[6]) < int("25000")) or \
                        (var1.get() == "Lower mid-range(25,000-35,000)" and int("25000") < int(record[6]) < int(
                            "35000")) or \
                        (var1.get() == "Mid-range(35,000-45,000)" and int("35000") < int(record[6]) < int("45000")) or \
                        (var1.get() == "Upper mid-range(45,000-60,000)" and int("45000") < int(record[6]) < int(
                            "60000")) or \
                        (var1.get() == "Lower flag-ship(60,000-80,000)" and int("60000") < int(record[6]) < int(
                            "80000")) or \
                        (var1.get() == "Flag-ship(80,000-1,00,000)" and int("80000") < int(record[6]) < int(
                            "100000")) or \
                        (var1.get() == "Killer flag-ship(1,00,000-so on)" and int("100000") < int(record[6]) < int(
                            "300000")):
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"
                sm_label = Label(rroot, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(rroot, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(rroot, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(rroot, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(rroot, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(rroot, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(rroot, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(rroot, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)




            except:
                pass
        smartphone_name1 = Label(rroot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(rroot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(rroot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(rroot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                            y=177)
        RAM1 = Label(rroot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                            y=177)

        storage1 = Label(rroot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(rroot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                y=177)

        speciality1 = Label(rroot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)
        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(rroot, image=go_backimg, borderwidth=5, command=rroot.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    # function to check if user has selescted any budget or not.
    def radio_name_search():
        # Create a databases or connect to one
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        co = conn.cursor()
        # query of the database
        co.execute("SELECT *, oid FROM addresses")
        records = co.fetchall()
        # Loop through the results
        for record in records:
            if (var1.get() == "Entry level(10,000-25,000)" and int("10000") < int(record[6]) < int("25000")) or \
                    (var1.get() == "Lower mid-range(25,000-35,000)" and int("25000") < int(record[6]) < int("35000")) or \
                    (var1.get() == "Mid-range(35,000-45,000)" and int("35000") < int(record[6]) < int("45000")) or \
                    (var1.get() == "Upper mid-range(45,000-60,000)" and int("45000") < int(record[6]) < int("60000")) or \
                    (var1.get() == "Lower flag-ship(60,000-80,000)" and int("60000") < int(record[6]) < int("80000")) or \
                    (var1.get() == "Flag-ship(80,000-1,00,000)" and int("80000") < int(record[6]) < int("100000")) or \
                    (var1.get() == "Killer flag-ship(1,00,000-so on)" and int("100000") < int(record[6]) < int(
                        "300000")):
                try:

                    return radio_page()

                except:
                    pass

        return messagebox.showinfo("Sorry", "Please choose the budget", parent=mroot)
        a = 1

        conn2.commit()
        conn2.close()

    # list
    brand_list = ['Samsung', 'Oppo', 'Vivo', 'Oneplus', 'Apple', 'Xiaomi']
    c = StringVar()
    droplist = OptionMenu(mroot, c, *brand_list)
    droplist.config(width=14, bg="white", font=('Times New Roman', 13), borderwidth=0)
    c.set('Select brand')
    droplist.place(x=215, y=305)
    brand_search_btn = Button(mroot, text="Search", image=search_img, borderwidth=0, compound=CENTER, fg="white",
                              command=brand_name_search,
                              font=('Times New Roman', 14, "bold"))
    brand_search_btn.place(x=440, y=310)
    my_canvas.create_text(270, 370, text="Search smart-phone by the budget category.",
                          font=('Times New Roman', 17, "bold"))
    my_canvas.create_text(115, 500, text="Budget catogeries:", font=('Times New Roman', 13))

    MODES = [
        ("Entry level(10,000-25,000)", "Entry level(10,000-25,000)"),
        ("Lower mid-range(25,000-35,000)", "Lower mid-range(25,000-35000)"),
        ("Mid-range(35,000-45,000)", "Mid-range(35,000-45,000)"),
        ("Upper mid-range(45,000-60,000)", "Upper mid-range(45,000-60,000)"),
        ("Lower flag-ship(60,000-80,000)", "Lower flag-ship(60,000-80,000)"),
        ("Flag-ship(80,000-1,00,000)", "Flag-ship(80,000-1,00,000)"),
        ("Killer flag-ship(1,00,000-so on)", "Killer flag-ship(1,00,000-so on)")

    ]
    var1 = StringVar()
    var1.set("0")
    frame = LabelFrame(mroot, text="", padx=7, pady=10, bg='lightblue', borderwidth=5)
    frame.place(x=180, y=400)
    for text, mode in MODES:
        Radiobutton(frame, text=text, font=('times new roman', 12), bg="lightblue", variable=var1, value=mode).pack(
            anchor=W)

    budget_search_btn = Button(mroot, text="Search", command=radio_name_search, image=search_img, borderwidth=0,
                               compound=CENTER, fg="white",
                               font=('Times New Roman', 14, "bold"))
    budget_search_btn.place(x=440, y=490)
    my_canvas.create_text(680, 225, text="Click smart-phone by your \n            requirement.",
                          font=('Times New Roman', 17, "bold"))

    my_canvas.create_rectangle(540, 180, 825, 670, width=4, outline="lightBLUE")
    my_canvas.create_line(540, 530, 825, 530, width=4, fill="lightblue")
    my_canvas.create_rectangle(20, 180, 525, 670, width=4, outline="lightBLUE")
    my_canvas.create_rectangle(840, 180, 1325, 670, width=4, outline="lightBLUE")
    my_canvas.create_line(20, 270, 525, 270, width=4, fill="lightblue")
    my_canvas.create_line(20, 350, 525, 350, width=4, fill="lightblue")

    # Function for searching camera smartphone by clicking the camera button.
    def image_camera_page():
        global smartphone_search_page_img
        global go_backimg
        imroot = Toplevel()
        imroot.geometry("%dx%d+0+0" % (imroot.winfo_screenwidth(), imroot.winfo_screenheight()))
        imroot.title('Smartphone Management System')
        imroot.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(imroot, image=smartphone_search_page_img).place(x=0, y=0)

        # Connecting to database
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()
        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""
        # Loop through the results
        for record in records:
            try:
                if str(record[7]) == "Camera":
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"

                sm_label = Label(imroot, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(imroot, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(imroot, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(imroot, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(imroot, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(imroot, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(imroot, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(imroot, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)

            except:
                pass
        smartphone_name1 = Label(imroot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(imroot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(imroot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(imroot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                             y=177)
        RAM1 = Label(imroot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                             y=177)

        storage1 = Label(imroot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(imroot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                 y=177)

        speciality1 = Label(imroot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)
        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(imroot, image=go_backimg, borderwidth=5, command=imroot.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    var12 = StringVar()
    camera_img = PhotoImage(file='camera.png')
    camera_img_btn = Button(mroot, text="Camera", command=image_camera_page, variable=var12.set(""),
                            font=('Times New Roman', 14), image=camera_img, borderwidth=5,
                            compound="top")
    camera_img_btn.place(x=580, y=270)

    # Function for searching gaming smartphone by clicking the game button.
    def image_Gaming_page():
        global smartphone_search_page_img
        global go_backimg
        groot = Toplevel()
        groot.geometry("%dx%d+0+0" % (groot.winfo_screenwidth(), groot.winfo_screenheight()))
        groot.title('Smartphone Management System')
        groot.iconbitmap('smartphone2.ico')

        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(groot, image=smartphone_search_page_img).place(x=0, y=0)

        # Connecting to database
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()
        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""
        # Loop through the results
        for record in records:
            try:
                if str(record[7]) == "Gaming":
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"

                sm_label = Label(groot, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(groot, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(groot, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(groot, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(groot, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(groot, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(groot, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(groot, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)

            except:
                pass
        smartphone_name1 = Label(groot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(groot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(groot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(groot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                            y=177)
        RAM1 = Label(groot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                            y=177)

        storage1 = Label(groot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(groot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                y=177)

        speciality1 = Label(groot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)
        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(groot, image=go_backimg, borderwidth=5, command=groot.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    game_img = ImageTk.PhotoImage(Image.open('game.png'))
    game_img_btn = Button(mroot, text="Game", command=image_Gaming_page, font=('Times New Roman', 14), image=game_img,
                          borderwidth=5,
                          compound="top")

    game_img_btn.place(x=700, y=270)

    # Function for searching battery efficient smartphone by clicking the battery button.
    def image_battery_page():
        global smartphone_search_page_img
        global go_backimg
        broot = Toplevel()
        broot.geometry("%dx%d+0+0" % (broot.winfo_screenwidth(), broot.winfo_screenheight()))
        broot.title('Smartphone Management System')
        broot.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(broot, image=smartphone_search_page_img).place(x=0, y=0)

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()
        # print(records)
        # Loop through the results
        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""

        for record in records:
            try:
                if str(record[7]) == "Battery":
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"

                sm_label = Label(broot, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(broot, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(broot, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(broot, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(broot, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(broot, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(broot, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(broot, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)
            except:
                pass
        smartphone_name1 = Label(broot, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(broot, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(broot, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(broot, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                            y=177)
        RAM1 = Label(broot, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                            y=177)

        storage1 = Label(broot, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(broot, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                y=177)

        speciality1 = Label(broot, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)
        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(broot, image=go_backimg, borderwidth=5, command=broot.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    battery_img = PhotoImage(file='battery.png')
    battery_img_btn = Button(mroot, text="Battery", command=image_battery_page, font=('Times New Roman', 14),
                             image=battery_img, borderwidth=5,
                             compound="top")

    battery_img_btn.place(x=580, y=400)

    # Function for searching 5G smartphone by clicking the 5G button.
    def G5():
        global go_backimg
        global smartphone_search_page_img
        g5root = Toplevel()
        g5root.geometry("%dx%d+0+0" % (g5root.winfo_screenwidth(), g5root.winfo_screenheight()))
        g5root.title('Smartphone Management System')
        g5root.iconbitmap('smartphone2.ico')
        smartphone_search_page_img = ImageTk.PhotoImage(Image.open('smartphone2.png'))
        login_img = Label(g5root, image=smartphone_search_page_img).place(x=0, y=0)

        # Create a databases or connect to one
        conn = sqlite3.connect('address_book2.db')
        # Create cursor
        c1 = conn.cursor()
        # query of the database
        c1.execute("SELECT *, oid FROM addresses")
        records = c1.fetchall()
        print_smartphone = ""
        print_brand = ""
        print_processor = ""
        print_GPU = ""
        print_RAM = ""
        print_storage = ""
        print_price = ""
        print_speciality = ""
        # Loop through the results
        for record in records:
            try:
                if str(record[7]) == "5G":
                    print_smartphone += str(record[0]) + "\n"
                    print_brand += str(record[1]) + "\n"
                    print_processor += str(record[2]) + "\n"
                    print_GPU += str(record[3]) + "\n"
                    print_RAM += str(record[4]) + "\n"
                    print_storage += str(record[5]) + "\n"
                    print_price += "Rs" + str(record[6]) + "\n"
                    print_speciality += str(record[7]) + "\n"

                sm_label = Label(g5root, text=print_smartphone, font=('times new roman', 14))
                sm_label.place(x=210, y=220)
                bd_label = Label(g5root, text=print_brand, font=('times new roman', 14))
                bd_label.place(x=430, y=220)
                pro_label = Label(g5root, text=print_processor, font=('times new roman', 14))
                pro_label.place(x=520, y=220)
                GU_label = Label(g5root, text=print_GPU, font=('times new roman', 14))
                GU_label.place(x=690, y=220)
                RM_label = Label(g5root, text=print_RAM, font=('times new roman', 14))
                RM_label.place(x=860, y=220)
                storage_label = Label(g5root, text=print_storage, font=('times new roman', 14))
                storage_label.place(x=930, y=220)
                pri_label = Label(g5root, text=print_price, font=('times new roman', 14))
                pri_label.place(x=1010, y=220)
                speciality_label = Label(g5root, text=print_speciality, font=('times new roman', 14))
                speciality_label.place(x=1115, y=220)

            except:
                pass
        smartphone_name1 = Label(g5root, text="Smartphone name", fg="white", bg="black",
                                 font=('Times New Roman', 16, 'bold')).place(x=220, y=177)
        smartphone_brand1 = Label(g5root, text="Brand", fg="white", bg="black",
                                  font=('Times New Roman', 16, 'bold')).place(x=430, y=177)

        processor_name1 = Label(g5root, text="Chipset", fg="white", bg="black",
                                font=('Times New Roman', 16, 'bold')).place(x=560, y=177)

        GPU1 = Label(g5root, text="GPU", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=750,
                                                                                                             y=177)
        RAM1 = Label(g5root, text="RAM", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=860,
                                                                                                             y=177)

        storage1 = Label(g5root, text="Storage", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(
            x=925, y=177)

        price1 = Label(g5root, text="Price", fg="white", bg="black", font=('Times New Roman', 16, 'bold')).place(x=1025,
                                                                                                                 y=177)

        speciality1 = Label(g5root, text="Speciality", fg="white", bg="black",
                            font=('Times New Roman', 16, 'bold')).place(x=1105, y=177)

        go_backimg = ImageTk.PhotoImage(Image.open('back1.png'))
        go_back = Button(g5root, image=go_backimg, borderwidth=5, command=g5root.destroy)
        go_back.place(x=610, y=550)

        conn.commit()
        conn.close()

    G5_img = ImageTk.PhotoImage(Image.open('5G.png'))
    G5_img_btn = Button(mroot, text="5G", command=G5, font=('Times New Roman', 14), image=G5_img, borderwidth=5,
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

# registration submit function
def submit():
    if user_name.get() == "" or address.get() == "" or email.get() == "" or password.get() == "" or var.get() == "4" or car.get() == 'Select District' or var123.get() == 'off':
        messagebox.showinfo("Incomplete registration", "Please fill the form completely")
    else:
        conn = sqlite3.connect('login_sqlite.db')
        # Create cursor
        c = conn.cursor()
        # Insert into table
        c.execute("INSERT INTO login VALUES (:user_name,:password, :email)", {
            'user_name': user_name.get(),
            'password': password.get(),
            'email': email.get(),
        })
        conn.commit()
        conn.close()
        messagebox.showinfo("Register", "You have successfully registered")
        mainpage()


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
var.set("4")
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

password = Entry(root, width=16, font=('Times New Roman', 13), show="*")
password.place(x=695, y=348)

var123 = StringVar()
agreement = Checkbutton(root, text="I agree the terms and conditions.", font=('Times New Roman', 12, "bold"),
                        variable=var123, onvalue="on", offvalue="off", bg="white")
agreement.deselect()
agreement.place(x=600, y=370)
# create submit button
register = PhotoImage(file='register.png')
submit_btn = Button(root, text="Register", bg="white", font=('Times New Roman', 15, "bold"), command=submit,
                    image=register, compound=CENTER, borderwidth=0)
submit_btn.place(x=660, y=395)

#Login function
def login_fn():
    global image_login
    lroot = Toplevel()
    lroot.title('Smartphone city')
    lroot.iconbitmap('smartphone2.ico')
    # for making the full screen.
    lroot.geometry("%dx%d+0+0" % (lroot.winfo_screenwidth(), lroot.winfo_screenheight()))
    lroot.title('Login page')
    lroot.iconbitmap('smartphone2.ico')
    # Login background image.

    image_login = ImageTk.PhotoImage(Image.open('login.png'))
    login_page_img = Label(lroot, image=image_login).place(x=0, y=0)
    login_inside = Label(lroot, text="Login Here", fg="blue", font=('Times New Roman', 20, "bold"), bg="white")
    login_inside.place(x=660, y=180)
    #If user forgets password function
    def forget():
        global image_forget
        global login_email_btn
        froot = Toplevel()
        froot.title('Smartphone city')
        froot.iconbitmap('smartphone2.ico')
        # for making the full screen.
        froot.geometry("%dx%d+0+0" % (froot.winfo_screenwidth(), froot.winfo_screenheight()))
        froot.title('Forget password page')
        froot.iconbitmap('smartphone2.ico')
        # Login background image.
        image_forget = ImageTk.PhotoImage(Image.open('login.png'))
        forget_page_img = Label(froot, image=image_forget).place(x=0, y=0)
        forgpas = Label(froot, text="Forget Password??", font=('Times New Roman', 20, "bold"), fg="red", bg="white")
        forgpas.place(x=610, y=150)
        warning = Label(froot,
                        text="If you have forget the password \n please  enter the email address you \n have registered during registration.",
                        compound=CENTER, font=('Times New Roman', 13), bg="white")
        warning.place(x=600, y=190)

        def send():
            # Connecting to database
            conn = sqlite3.connect('login_sqlite.db')
            # Create cursor
            c = conn.cursor()
            # query of the database
            c.execute("SELECT *, oid FROM login")
            records = c.fetchall()
            # Loop through the results

            for record in records:
                if str(record[2]) == registered_email.get():
                    try:
                        submit_btn_img['state'] = NORMAL
                        return messagebox.showinfo("Email", "5 digit code has been sent to your mobile", parent=froot)


                    except:
                        pass

            messagebox.showinfo("Email", "Please enter registered email correctly", parent=froot)

            conn.commit()
            conn.close()

        def code():
            if code_entry.get() == "12345":
                froot.withdraw()
                lroot.withdraw()
                mainpage()
            else:
                messagebox.showinfo("Core error", "Enter code correctly", parent=froot)

        warning_email = Label(froot, text="Registered Email", font=('Times New Roman', 15, "bold"), bg="white")
        warning_email.place(x=645, y=270)
        registered_email = Entry(froot, width=22, font=('Times New Roman', 13))
        registered_email.place(x=620, y=300)
        forget_submit_btn = Button(froot, text="SEND", command=send, fg="white", bg="blue",
                                   font=('Times New Roman', 15, "bold"),
                                   borderwidth=0)
        forget_submit_btn.place(x=680, y=340)
        login_email_btn = PhotoImage(file='register.png')
        submit_btn_img = Button(froot, text="Login", bg="white", command=code, state=DISABLED,
                                font=('Times New Roman', 15, "bold"),
                                image=login_email_btn, compound=CENTER, borderwidth=0)
        submit_btn_img.place(x=660, y=470)

        code = Label(froot, text="Enter the 5 digit code \n obtained in your email.",
                     font=('Times New Roman', 12, "bold"), bg="white")
        code.place(x=650, y=390)
        code_entry = Entry(froot, width=22, font=('Times New Roman', 13))
        code_entry.place(x=620, y=430)

    forget_btn = Button(lroot, text="Forget password?", command=forget, fg="red", bg="white",
                        font=('Times New Roman', 15, "bold"),
                        borderwidth=0)
    forget_btn.place(x=650, y=350)

    def login_main_fn():
        # Connecting to database.
        conn = sqlite3.connect('login_sqlite.db')
        # Creating cursor
        c = conn.cursor()
        c.execute("SELECT *, oid FROM login")
        records = c.fetchall()
        # Loop through the results
        for record in records:
            if str(record[0]) == user_name_entry.get() and str(record[1]) == password_entry.get():
                try:
                    messagebox.showinfo("login", "login successful", parent=lroot)
                    lroot.withdraw()
                    mainpage()
                except:
                    pass
            elif user_name_entry.get() == "" or password_entry.get() == "":
                try:
                    return messagebox.showinfo("login", "Please fill completely.", parent=lroot)
                except:
                    pass
        messagebox.showinfo("login", "Your username and password do not match.", parent=lroot)
        conn.commit()
        conn.close()

    user_name_label = Label(lroot, text="User Name", font=('Times New Roman', 13), bg="white")
    user_name_label.place(x=600, y=250)
    user_name_entry = Entry(lroot, width=16, font=('Times New Roman', 13))
    user_name_entry.place(x=690, y=250)
    password_label = Label(lroot, text="Password", font=('Times New Roman', 13), bg="white")
    password_label.place(x=600, y=300)
    password_entry = Entry(lroot, width=16, font=('Times New Roman', 13), show="*")
    password_entry.place(x=690, y=300)
    login1_btn = Button(lroot, text="Login", command=login_main_fn, bg="white", font=('Times New Roman', 15, "bold"),
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
