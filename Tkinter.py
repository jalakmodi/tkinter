from tkinter import messagebox

#import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.messagebox
root = tk.Tk()
root.title("Registration Form")
root.geometry("350x400")
root.resizable(width=False, height=False)
root.config(bg="LightSteelBlue")
def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sgvp temple" )
def submit():
    address = add_txt.get("1.0", tk.END)
    if fn_entry.get() =="" or ln_entry.get() =="" or mob_entry.get() =="" or address.strip()=="":
       messagebox.showinfo("Warning", "All fields are required.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into members(Fname,Lname,Mobile,Addressh) values(%s,%s,%s,%s)"
        args = (fn_entry.get(),ln_entry.get(),mob_entry.get(),address.strip())
        cursor.execute(query,args)
        conn.commit()
        id_entry.delete(0,END)
        fn_entry.delete(0,END)
        ln_entry.delete(0,END)
        mob_entry.delete(0,END)
        add_txt.delete("1.0", tk.END)
        messagebox.showinfo("Information", "Your Data Has Been Submitted.")
def search():
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    mob_entry.delete(0, END)
    add_txt.delete("1.0", tk.END)
    if id_entry.get() =="":
        messagebox.showinfo("Warning", "Please Enter Id ")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from members where Mem_Id=%s"
        args = (id_entry.get(),)
        cursor.execute(query,args)
        rows = cursor.fetchall()
        conn.close()
        if rows:
            fn_entry.insert([0],rows[0][1])
            ln_entry.insert([0],rows[0][2])
            mob_entry.insert([0],rows[0][3])
            add_txt.insert([0],rows[0][4])
        else:
            messagebox.showinfo("Information", "Enter Id Not Found")

#[(1, 'Jalak',
# 'Modi',
#  9327016414,
# 'I- 403 Anand Vihar Flat Tragad Road ,Tragad Chandkheda')]



lb1 =Label(root, text="Member Registration Form", font=("Helvetica",16,"bold"),bg="Black", fg="Yellow")
lb1.pack()

id_lbl =Label(root, text="Member Id : ",font=("Helvetica"),bg="LightSteelBlue", fg="Black")
id_lbl.place(x=10,y=50)
id_entry = Entry(root, font=("Helvetica",15,"bold"),width=19)
id_entry.place(x=125,y=50)

fn_lbl =Label(root, text="First Name : ",font=("Helvetica"),bg="LightSteelBlue", fg="Black")
fn_lbl.place(x=10,y=100)
fn_entry = Entry(root, font=("Helvetica",15,"bold"),width=19)
fn_entry.place(x=125,y=100)
ln_lbl =Label(root, text="Last Name : ",font=("Helvetica"),bg="LightSteelBlue", fg="Black")
ln_lbl.place(x=10,y=150)
ln_entry = Entry(root, font=("Helvetica",15,"bold"),width=19)
ln_entry.place(x=125,y=150)

mod_lbl=Label(root, text="Mobile       : ",font=("Helvetica"),bg="LightSteelBlue", fg="Black")
mod_lbl.place(x=10,y=200)
mob_entry = Entry(root, font=("Helvetica",15,"bold"),width=19)
mob_entry.place(x=125,y=200)

add_lbl =Label(root, text="Addressh   : ",font=("Helvetica"),bg="LightSteelBlue", fg="Black")
add_lbl.place(x=10,y=250)
add_txt = Text(root, font=("Helvetica",15,"bold"),width=19,height=3)
add_txt.place(x=125,y=250)

sub_btn = Button(root, text="Submit",font=("Helvetica",15,"bold"),command=submit)
sub_btn.place(x=15, y=340)
sub_btn = Button(root, text="Serch",font=("Helvetica",15,"bold"),command=search)
sub_btn.place(x=100, y=340)
sub_btn = Button(root, text="Update",font=("Helvetica",15,"bold"))
sub_btn.place(x=175, y=340)
sub_btn = Button(root, text="Delete",font=("Helvetica",15,"bold"))
sub_btn.place(x=262, y=340)

root.mainloop()