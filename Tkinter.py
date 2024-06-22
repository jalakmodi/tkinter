import tkinter as tk
from tkinter import messagebox
import mysql.connector


def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Registration Form" )

def submit_form():
    name = entry_name.get()
    contact = entry_contact.get()
    email = entry_email.get()
    gender = gender_var.get()
    city = city_var.get()

    # Basic validation
    if name == "" or contact == "" or email == "":
        messagebox.showerror("Error", "Please fill in all required fields")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "insert into form(Name,Contact,Email,Gender,City) values(%s,%s,%s,%s,%s)"
        args = (entry_name.get(), entry_contact.get(), entry_email.get(), gender_var.get(),city_var.get(),)
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        entry_name.delete(0, tk.END)
        entry_contact.delete(0, tk.END)
        entry_email.delete(0, tk.END)


        # Optional: You can process or save the data here
        message = f"Registration Successful!\n\nName: {name}\nEmail: {email}\nGender: {gender}\nCity: {city}"
        messagebox.showinfo("Success", message)

def search_form():
    entry_contact.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    if entry_name.get()=="":
        messagebox.showerror("Error", "Please fill required fields")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from form where Name=%s"
        args = (entry_name.get(),)
        cursor.execute(query, args)
        data = cursor.fetchall()
        if data:
            for i in data:
                entry_contact.insert(0,i[2])
                entry_email.insert(0,i[3])
                gender_var.set(i[4])
                city_var.set(i[5])
                conn.close()
        else:
            messagebox.showinfo("info", "Data Not Found Please Enter Correct Name")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")

# Define variables for dropdowns
gender_options = ["Male", "Female", "Other"]
city_options = ["Ahmedabad", "Baroda", "Rajkot", "Gandhinagar", "Surat"]

# Create and place labels and entry fields
label_name = tk.Label(root, text="Please Fill in All Required Fields",bg="light blue", fg="black" , font=("Helvetica", 10))
label_name.grid(row=0, column=0, padx=10, pady=5)


label_name = tk.Label(root, text="Name:")
label_name.grid(row=2, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=2, column=1, padx=10, pady=5)

label_contact = tk.Label(root, text="Contact:")
label_contact.grid(row=3, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root,)
entry_contact.grid(row=3, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=4, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=4, column=1, padx=10, pady=5)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=5, column=0, padx=10, pady=5)
gender_var = tk.StringVar(root)
gender_var.set(gender_options[0])  # Default value
gender_dropdown = tk.OptionMenu(root, gender_var, *gender_options)
gender_dropdown.grid(row=5, column=1, padx=10, pady=5)

label_city = tk.Label(root, text="City:")
label_city.grid(row=6, column=0, padx=10, pady=5)
city_var = tk.StringVar(root)
city_var.set(city_options[0])  # Default value
city_dropdown = tk.OptionMenu(root, city_var, *city_options)
city_dropdown.grid(row=6, column=1, padx=10, pady=5)


# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=9, columnspan=2, pady=10)

submit_button = tk.Button(root, text="Search", command=search_form)
submit_button.grid(row=11, columnspan=2, pady=10)

# Start the main tkinter loop
root.mainloop()
