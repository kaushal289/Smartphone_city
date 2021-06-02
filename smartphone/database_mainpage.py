from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3



# Createating a databases
conn = sqlite3.connect('address_book2.db')
# Creatating a cursor
c = conn.cursor()
'''
# Create table
c.execute(""" CREATE TABLE addresses(
      smartphone_name text,
      brand text,
      processor text,
      GPU text,
      RAM text,
      storage text,
      price text,
      speciality text
) """)
'''


#creating a class
class log:
    def login12(self):
        #admin login function of database.
        def log1():
            if self.username_ent.get() == "kaushal"and self.pass_ent.get()=="123":
                login123(self)
            else:
                messagebox.showinfo("Login failed", "Enter correctly")

        root4.geometry("%dx%d+0+0" % (root4.winfo_screenwidth(), root4.winfo_screenheight()))
        login = ImageTk.PhotoImage(Image.open('login.png'))
        login_img = Label(root4, image=login).place(x=0, y=0)
        self.username_ent = Entry(root4, font=("times new roman", 14, "bold"),width=13)
        self.username_ent.place(x=710, y=300)
        self.pass_ent = Entry(root4, font=("times new roman", 14, "bold"), show="*",width=13)
        self.pass_ent.place(x=710, y=340)
        title_leb = Label(root4, text="Admin Login", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        title_leb.place(x=650, y=250)
        username_leb = Label(root4, text="User name", font=("times new roman", 16, "bold"), bg="white")
        username_leb.place(x=600, y=300)
        pass_leb = Label(root4, text="Password", font=("times new roman", 16, "bold"), bg="white")
        pass_leb.place(x=600, y=340)

        # function of the mainpage of database
        def login123(self):
            root = Toplevel()
            root.title('Database GUI')
            root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
            login = ImageTk.PhotoImage(Image.open('smartphone.png'))
            root.title('Smartphone management system(Database)')
            root.iconbitmap('smartphone2.ico')
            login_img = Label(root, image=login).place(x=0, y=0)

            frame = LabelFrame(root, text="", padx=10, pady=10, borderwidth=20, bg="lightblue")
            frame.place(x=260, y=20)
            frame1 = LabelFrame(root, text="", padx=10, pady=10, borderwidth=20, bg="lightblue")
            frame1.place(x=730, y=20)

            frame2 = LabelFrame(root, text="", padx=10, pady=10, borderwidth=20, bg="lightblue")
            frame2.place(x=730, y=250)

            def delete():
                # create database
                conn = sqlite3.connect('address_book2.db')
                # create cursor
                c = conn.cursor()
                # delete a record
                c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

                print('Deleted Successfully')
                # query of the database
                c.execute("SELECT *, oid FROM addresses")
                conn.commit()
                conn.close()

            # Creating an update function
            def update():
                # Create a databases or connect to one
                conn = sqlite3.connect('address_book2.db')
                # Create cursor
                c = conn.cursor()
                record_id = delete_box.get()

                c.execute(""" UPDATE addresses SET
                     smartphone_name = :smartphone,
                     brand = :brand,
                     processor = :processor,
                     GPU = :GPU,
                     RAM=:RAM,
                     storage = :storage,
                     price = :price,
                     speciality=:speciality
                     WHERE oid = :oid""",
                          {'smartphone': smartphone_editor.get(),
                           'brand': brand_editor.get(),
                           'processor': processor_editor.get(),
                           'GPU': GPU_editor.get(),
                           'RAM': RAM_editor.get(),
                           'storage': storage_editor.get(),
                           'price': price_editor.get(),
                           'speciality': speciality_editor.get(),
                           'oid': record_id
                           }
                          )
                conn.commit()
                conn.close()
                # Destroying all the data and closing window
                editor.destroy()

            # Create edit function to update a record
            def edit():
                global editor
                editor = Tk()
                editor.title('Update Data')
                editor.geometry('380x320')
                editor.config(bg="lightblue")
                # Create a databases or connect to one
                conn = sqlite3.connect('address_book2.db')
                # Create cursor
                c = conn.cursor()
                record_id = delete_box.get()
                # query of the database
                c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
                records = c.fetchall()
                # Creating global variable for all text boxes
                global smartphone_editor
                global brand_editor
                global processor_editor
                global GPU_editor
                global RAM_editor
                global storage_editor
                global price_editor
                global speciality_editor

                # Create text boxes
                smartphone_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                smartphone_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
                brand_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                brand_editor.grid(row=1, column=1)
                processor_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                processor_editor.grid(row=2, column=1)
                GPU_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                GPU_editor.grid(row=3, column=1)
                RAM_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                RAM_editor.grid(row=4, column=1)
                storage_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                storage_editor.grid(row=5, column=1)
                price_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                price_editor.grid(row=6, column=1)
                speciality_editor = Entry(editor, width=15, font=('Times New Roman', 14, 'bold'))
                speciality_editor.grid(row=7, column=1)

                # Create textbox labels
                smartphone_label = Label(editor, text="Smartphone name", font=('Times New Roman', 14, 'bold'),
                                         bg="lightblue")
                smartphone_label.grid(row=0, column=0, pady=(10, 0))
                brand_label = Label(editor, text="Brand Name", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                brand_label.grid(row=1, column=0)
                processor_label = Label(editor, text="Processor", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                processor_label.grid(row=2, column=0)
                GPU_label = Label(editor, text="GPU", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                GPU_label.grid(row=3, column=0)
                RAM_label = Label(editor, text="RAM", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                RAM_label.grid(row=4, column=0)
                storage_label = Label(editor, text="Storage", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                storage_label.grid(row=5, column=0)
                price_label = Label(editor, text="Price", font=('Times New Roman', 14, 'bold'), bg="lightblue")
                price_label.grid(row=6, column=0)
                speciality_label = Label(editor, text="Speciality", font=('Times New Roman', 14, 'bold'),
                                         bg="lightblue")
                speciality_label.grid(row=7, column=0)
                # loop through the results
                for record in records:
                    smartphone_editor.insert(0, record[0])
                    brand_editor.insert(0, record[1])
                    processor_editor.insert(0, record[2])
                    GPU_editor.insert(0, record[3])
                    RAM_editor.insert(0, record[4])
                    storage_editor.insert(0, record[5])
                    price_editor.insert(0, record[6])
                    speciality_editor.insert(0, record[7])

                # Create a update button
                edit_btn = Button(editor, text=" SAVE ", command=update, font=('Times New Roman', 20, 'bold'),
                                  bg="lightgreen")
                edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

            # Create submit button for databases
            def submit():
                # Connecting to database.
                conn = sqlite3.connect('address_book2.db')
                # Create cursor
                c = conn.cursor()
                # Insert into table
                c.execute(
                    "INSERT INTO addresses VALUES (:smartphone,:brand, :processor, :GPU,:RAM, :storage, :price,:speciality)",
                    {
                        'smartphone': smartphone.get(),
                        'brand': brand.get(),
                        'processor': processor.get(),
                        'GPU': GPU.get(),
                        'RAM': RAM.get(),
                        'storage': storage.get(),
                        'price': price.get(),
                        'speciality': speciality.get()
                    })
                # showinfo messagebox
                messagebox.showinfo("Adresses", "Inserted Successfully")
                conn.commit()
                conn.close()
                # clear the text boxes
                smartphone.delete(0, END)
                brand.delete(0, END)
                processor.delete(0, END)
                GPU.delete(0, END)
                RAM.delete(0, END)
                storage.delete(0, END)
                price.delete(0, END)
                speciality.delete(0, END)
            #desplays all the data present in database
            def display():
                root2 = Toplevel()
                root2.geometry("%dx%d+0+0" % (root2.winfo_screenwidth(), root2.winfo_screenheight()))
                root2.config(bg="lightblue")
                # Create a databases or connect to one
                conn = sqlite3.connect('address_book2.db')
                # Create cursor
                c = conn.cursor()
                # query of the database
                c.execute("SELECT *, oid FROM addresses")
                records = c.fetchall()

                oid_name = Label(root2, text="Oid ID", font=('Times New Roman', 16, 'bold'), bg="lightblue").place(x=80,
                                                                                                                   y=10)
                smartphonename = Label(root2, text='Samrtphone Name', font=('Times New Roman', 16, 'bold'),
                                       bg="lightblue").place(x=200, y=10)
                brandname = Label(root2, text='brand name', font=('Times New Roman', 16, 'bold'), bg="lightblue").place(
                    x=380,
                    y=10)
                processorname = Label(root2, text='processor name', font=('Times New Roman', 16, 'bold'),
                                      bg="lightblue").place(
                    x=500, y=10)
                GPUname = Label(root2, text='GPU', font=('Times New Roman', 16, 'bold'), bg="lightblue").place(x=660,
                                                                                                               y=10)
                RAMname = Label(root2, text='RAM', font=('Times New Roman', 16, 'bold'), bg="lightblue").place(x=750,
                                                                                                               y=10)
                storagename = Label(root2, text='storage', font=('Times New Roman', 16, 'bold'), bg="lightblue").place(
                    x=900,
                    y=10)
                price = Label(root2, text='price', font=('Times New Roman', 16, 'bold'), bg="lightblue").place(x=1050,
                                                                                                               y=10)
                specialtyname = Label(root2, text='speciality', font=('Times New Roman', 16, 'bold'),
                                      bg="lightblue").place(
                    x=1150, y=10)
                # Loop through the results
                print1 = ""
                print2 = ""
                print3 = ""
                print4 = ""
                print5 = ""
                print6 = ""
                print7 = ""
                print8 = ""
                print9 = ""

                for record in records:
                    print1 += str(record[8]) + "\n"
                    print2 += str(record[0]) + "\n"
                    print3 += str(record[1]) + "\n"
                    print4 += str(record[2]) + "\n"
                    print5 += str(record[3]) + "\n"
                    print6 += str(record[4]) + "\n"
                    print7 += str(record[5]) + "\n"
                    print8 += str(record[6]) + "\n"
                    print9 += str(record[7]) + "\n"
                oid_name = Label(root2, text=print1, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(x=100,
                                                                                                                 y=50)
                smartphonename = Label(root2, text=print2, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(
                    x=200,
                    y=50)
                brandname = Label(root2, text=print3, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(x=400,
                                                                                                                  y=50)
                processorname = Label(root2, text=print4, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(
                    x=500,
                    y=50)
                GPUname = Label(root2, text=print5, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(x=640,
                                                                                                                y=50)
                RAMname = Label(root2, text=print6, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(x=750,
                                                                                                                y=50)
                storagename = Label(root2, text=print7, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(
                    x=900, y=50)
                price = Label(root2, text=print8, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(x=1050,
                                                                                                              y=50)
                specialtyname = Label(root2, text=print9, font=('Times New Roman', 13, 'bold'), bg="lightblue").place(
                    x=1150,
                    y=50)

                conn.commit()
                conn.close()

            # Create text boxes
            smartphone = Entry(frame, font=('times new roman', 15), width=20)
            smartphone.grid(row=0, column=1, padx=20, pady=(10, 0))
            brand = Entry(frame, width=20, font=('times new roman', 15))
            brand.grid(row=1, column=1)
            processor = Entry(frame, width=20, font=('times new roman', 15))
            processor.grid(row=2, column=1)
            GPU = Entry(frame, width=20, font=('times new roman', 15))
            GPU.grid(row=3, column=1)
            RAM = Entry(frame, width=20, font=('times new roman', 15))
            RAM.grid(row=4, column=1)
            storage = Entry(frame, width=20, font=('times new roman', 15))
            storage.grid(row=5, column=1)
            price = Entry(frame, width=20, font=('times new roman', 15))
            price.grid(row=6, column=1)
            speciality = Entry(frame, width=20, font=('times new roman', 15))
            speciality.grid(row=7, column=1)
            delete_box = Entry(frame1, width=20, font=('times new roman', 15))
            delete_box.grid(row=0, column=1, pady=5)
            # Create textbox labels
            smartphone_label = Label(frame, text="Smartphone name", bg="lightblue", font=('times new roman', 15))
            smartphone_label.grid(row=0, column=0, pady=(10, 0))
            brand_label = Label(frame, text="Brand Name", bg="lightblue", font=('times new roman', 15))
            brand_label.grid(row=1, column=0)
            processor_label = Label(frame, text="Processor", bg="lightblue", font=('times new roman', 15))
            processor_label.grid(row=2, column=0)
            GPU_label = Label(frame, text="GPU", bg="lightblue", font=('times new roman', 15))
            GPU_label.grid(row=3, column=0)

            RAM_label = Label(frame, text="RAM", bg="lightblue", font=('times new roman', 15))
            RAM_label.grid(row=4, column=0)
            storage_label = Label(frame, text="Storage", bg="lightblue", font=('times new roman', 15))
            storage_label.grid(row=5, column=0)

            price_label = Label(frame, text="Price", bg="lightblue", font=('times new roman', 15))
            price_label.grid(row=6, column=0)
            speciality_label = Label(frame, text="Speciality", bg="lightblue", font=('times new roman', 15))
            speciality_label.grid(row=7, column=0)

            # Create submit button
            submit_btn = Button(frame, text="Add Records", bg="lightgreen", command=submit,
                                font=('times new roman', 15))
            submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
            # Create query button
            query_btn = Button(frame2, text="Show All Records", command=display, font=('times new roman', 15),
                               bg="lightgreen")
            query_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=75)

            delete_box_label = Label(frame1, text="Select ID", font=('times new roman', 15), bg="lightblue")
            delete_box_label.grid(row=0, column=0, pady=5)
            # Create a delete button
            delete_btn = Button(frame1, text="Delete", command=delete, font=('times new roman', 15), bg="lightgreen")
            delete_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=120)
            # Create a update button
            edit_btn = Button(frame1, text="Update", command=edit, font=('times new roman', 15), bg="lightgreen")
            edit_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

            # commit change
            conn.commit()
            # close connection
            conn.close()

            mainloop()


        loginbtn = Button(root4, text="Login", command=lambda: log1(),bg="lightblue", font=("times new roman", 16, "bold"))
        loginbtn.place(x=690, y=400)
        root4.mainloop()
#running the class function
a=log()
root4=Tk()
root4.title('Admin Login')
root4.iconbitmap('smartphone2.ico')
a.login12()
root4.mainloop()

