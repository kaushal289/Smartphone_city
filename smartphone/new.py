from tkinter import *
from PIL import ImageTk,Image
import sqlite3
root=Tk()
#Title of project with icon picture.
root.title('Smartphone city')
root.iconbitmap('smartphone2.ico')
#for making the full screen.
root.geometry("%dx%d+0+0"%(root.winfo_screenwidth(),root.winfo_screenheight()))
#Login background image.
login = ImageTk.PhotoImage(Image.open('login_im.jpg'))
login_img=Label(root,image=login).place(x=0,y=0)
# creating a database or connect to one
conn=sqlite3.connect('address_book.db')
# creating cursor
# cursor class is an instance using which you can invoke methods that
# execute SQLITE statements,fetch data from the result sets of the queries
c=conn.cursor()
# create table
'''c.execute("""CREATE TABLE addresses(
           user_name text,
            city text,
            state text,
            zipcode integer
)
""")'''

def submit():
# create a database or connect to one
    conn=sqlite3.connect('address_book.db')
    # create cursor
    c=conn.cursor()

    # insert into table
    c.execute("INSERT INTO addresses VALUES(:user_name,:city,:state,:zipcode)",{
        'user_name':user_name.get(),
        'city':city.get(),
        'zipcode':password.get()
    })
    print('address inserted successfully')

    conn.commit()

    conn.close()

    # clear the text boxes
    user_name.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    conn=sqlite3.connect('address_book.db')

    c=conn.cursor()
    c.execute("SELECT *,oid FROM addresses")

    records=c.fetchall()
    print(records)

    print_record=''
    for record in records:
        print_record +=str(record[0])+ " "+str(record[1])+' '+'\t'+str(record[6])+ "\n"

    query_label=Label(root,text=print_record)
    query_label.grid(row=8,column=0,columnspan=2)

    conn.commit()
    conn.close()

# create textbox labels
register_name = Label(root, text="Registration", font=('Times New Roman', 20, "bold"),bg="white")
register_name.place(x=650, y=142)
offer = Label(root, text="(Register and get exciting offer)", font=('Times New Roman', 12),bg="white")
offer.place(x=625, y=180)

user_name_label=Label(root,text="User Name", font=('Times New Roman', 13),bg="white")
user_name_label.place(x=600,y=210)

gender_label=Label(root,text="Gender", font=('Times New Roman', 13),bg="white")
gender_label.place(x=600,y=240)


district_label=Label(root,text="District", font=('Times New Roman', 13),bg="white")
district_label.place(x=600,y=270)

city_label=Label(root,text="City", font=('Times New Roman', 13),bg="white")
city_label.place(x=600,y=300)

email_label=Label(root,text="Email", font=('Times New Roman', 13),bg="white")
email_label.place(x=600,y=330)

password_label=Label(root,text="Set password", font=('Times New Roman', 13),bg="white")
password_label.place(x=600,y=360)



# create text box

user_name=Entry(root, width=25)
user_name.place(x=690,y=210)

var=IntVar()
Radiobutton(root,text="Male",variable=var,value=1).place(x=670,y=240)
Radiobutton(root,text="Female",variable=var,value=2).place(x=725,y=240)
Radiobutton(root,text="Other",variable=var,value=3).place(x=790,y=240)

district_list=['Kathmandu','Pokhara','Biratnagar','Kavre','Dhankuta','other'];
c=StringVar()
droplist=OptionMenu(root,c,*district_list)
droplist.config(width=15)
c.set('Select district')
droplist.place(x=690,y=270)


city=Entry(root,width=25)
city.place(x=690,y=300)


email=Entry(root,width=25)
email.place(x=690,y=330)

password=Entry(root,width=25)
password.place(x=690,y=360)



# create submit button
submit_btn=Button(root,text="add records",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2)

print("Table created successfully")
# commit change
conn.commit()
# close connection
conn.close()


mainloop()