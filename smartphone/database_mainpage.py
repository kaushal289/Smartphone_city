from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
root = Tk()
root.title('Database GUI')
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
login = ImageTk.PhotoImage(Image.open('smartphone.png'))
login_img = Label(root, image=login).place(x=0, y=0)

frame=LabelFrame(root,text="",padx=10,pady=10)
frame.place(x=500,y=10)
#Databases
# Create a databases or connect to one
conn = sqlite3.connect('address_book2.db')
# Create cursor
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

# Creating a function to delete a record
def delete():
    # create database
    conn = sqlite3.connect('address_book2.db')
    #create cursor
    c = conn.cursor()
    #delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    print('Deleted Successfully')
    # query of the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    # Loop through the results
    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + '       ' + str(record[1]) + '      ' + '\t' + str(record[8]) + "\n"
    query_label = Label(frame, text=print_record)
    query_label.grid(row=0, column=4,rowspan=50)
    conn.commit()
    conn.close()
#Creating an update function
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
          'speciality':speciality_editor.get(),
          'oid': record_id
               }
    )
    conn.commit()
    conn.close()
    #Destroying all the data and closing window
    editor.destroy()


# Create edit function to update a record
def edit():
    global editor
    editor = Tk()
    editor.title('Update Data')
    editor.geometry('350x250')
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book2.db')
    # Create cursor
    c = conn.cursor()
    record_id = delete_box.get()
    # query of the database
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
    records = c.fetchall()
    # print(records)
    #Creating global variable for all text boxes
    global smartphone_editor
    global brand_editor
    global processor_editor
    global GPU_editor
    global RAM_editor
    global storage_editor
    global price_editor
    global speciality_editor

    # Create text boxes
    smartphone_editor = Entry(editor, width=30)
    smartphone_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    brand_editor = Entry(editor, width=30)
    brand_editor.grid(row=1, column=1)
    processor_editor = Entry(editor, width=30)
    processor_editor.grid(row=2, column=1)
    GPU_editor = Entry(editor, width=30)
    GPU_editor.grid(row=3, column=1)
    RAM_editor = Entry(editor, width=30)
    RAM_editor.grid(row=4, column=1)
    storage_editor= Entry(editor, width=30)
    storage_editor.grid(row=5, column=1)
    price_editor = Entry(editor, width=30)
    price_editor.grid(row=6, column=1)
    speciality_editor = Entry(editor, width=30)
    speciality_editor.grid(row=7, column=1)

    # Create textbox labels
    smartphone_label = Label(editor, text="Smartphone name")
    smartphone_label.grid(row=0, column=0, pady=(10, 0))
    brand_label = Label(editor, text="Brand Name")
    brand_label.grid(row=1, column=0)
    processor_label = Label(editor, text="Processor")
    processor_label.grid(row=2, column=0)
    GPU_label = Label(editor, text="GPU")
    GPU_label.grid(row=3, column=0)
    RAM_label = Label(editor, text="RAM")
    RAM_label.grid(row=4, column=0)
    storage_label = Label(editor, text="Storage")
    storage_label.grid(row=5, column=0)
    price_label = Label(editor, text="Price")
    price_label.grid(row=6, column=0)
    speciality_label = Label(editor, text="Speciality")
    speciality_label.grid(row=7, column=0)
    # loop through the results
    for record in records:
        smartphone_editor.insert(0, record[0])
        brand_editor.insert(0, record[1])
        processor_editor.insert(0, record[2])
        GPU_editor.insert(0, record[3])
        RAM_editor.insert(0, record[4])
        storage_editor.insert(0,record[5])
        price_editor.insert(0, record[6])
        speciality_editor.insert(0, record[7])



    # Create a update button
    edit_btn = Button(editor, text=" SAVE ", command=update)
    edit_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


# Create submit button for databases
def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book2.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:smartphone,:brand, :processor, :GPU,:RAM, :storage, :price,:speciality)",{
        'smartphone': smartphone.get(),
        'brand': brand.get(),
        'processor': processor.get(),
        'GPU': GPU.get(),
        'RAM': RAM.get(),
        'storage': storage.get(),
        'price': price.get(),
        'speciality':speciality.get()
    })
    # showinfo messagebox
    messagebox.showinfo("Adresses", "Inserted Successfully")
    conn.commit()
    conn.close()
    # clear the text boxes
    smartphone.delete(0,END)
    brand.delete(0,END)
    processor.delete(0,END)
    GPU.delete(0, END)
    RAM.delete(0, END)
    storage.delete(0, END)
    price.delete(0, END)
    speciality.delete(0,END)

def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book2.db')
    # Create cursor
    c = conn.cursor()
    # query of the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
   # print(records)
    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + '' + str(record[5]) + ''+ '\t' + str(record[8]) + "\n"
    query_label = Label(frame, text=print_record)
    query_label.grid(row=0, column=4, rowspan=50)

    conn.commit()
    conn.close()


# Create text boxes
smartphone = Entry(frame, width=30)
smartphone.grid(row=0, column=1, padx=20, pady=(10,0))
brand = Entry(frame, width=30)
brand.grid(row=1, column=1)
processor= Entry(frame, width=30)
processor.grid(row=2, column=1)
GPU= Entry(frame, width=30)
GPU.grid(row=3, column=1)
RAM= Entry(frame, width=30)
RAM.grid(row=4, column=1)
storage = Entry(frame, width=30)
storage.grid(row=5, column=1)
price= Entry(frame, width=30)
price.grid(row=6, column=1)
speciality= Entry(frame, width=30)
speciality.grid(row=7, column=1)
delete_box = Entry(frame, width=30)
delete_box.grid(row=10, column=1, pady=5)
# Create textbox labels
smartphone_label = Label(frame, text="Smartphone name")
smartphone_label.grid(row=0, column=0, pady=(10,0))
brand_label = Label(frame, text="brand name")
brand_label.grid(row=1, column=0)
processor_label = Label(frame, text="processor")
processor_label.grid(row=2, column=0)
GPU_label = Label(frame, text="GPU")
GPU_label.grid(row=3, column=0)

RAM_label = Label(frame, text="RAM")
RAM_label.grid(row=4, column=0)
storage_label = Label(frame, text="Storage")
storage_label.grid(row=5, column=0)

price_label = Label(frame, text="price")
price_label.grid(row=6, column=0)
speciality_label = Label(frame, text="Speciality")
speciality_label.grid(row=7, column=0)
delete_box_label = Label(frame, text="Select ID")
delete_box_label.grid(row=10, column=0, pady=5)

# Create submit button
submit_btn = Button(frame, text="Add Records", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
# Create query button
query_btn = Button(frame, text="Show Records", command=query)
query_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a delete button
delete_btn = Button(frame, text="Delete", command=delete)
delete_btn.grid(row=15, column=0, columnspan=2, pady=10, padx =10, ipadx=120)
# Create a update button
edit_btn = Button(frame, text="Update", command=edit)
edit_btn.grid(row=17, column=0, columnspan=2, pady=10, padx =10, ipadx=120)

# commit change
conn.commit()
# close connection
conn.close()


mainloop()