from tkinter import *  # From tkinter import everything
from tkinter import messagebox  # From tkinter import messagebox
import random  # To use random firstly we should import it
import json   # To use json firstly we should import it


window=Tk()  # To define tkinter
window.title("Password Manager")  # To determine window's title
window.minsize(800,600)  # To determine window's size
window.config(padx=20,pady=5)  # To create a user interface

# To create image and the path is special for mine computer that path is not gonna work in your computer
canvas=Canvas(width=200,height=200)
tomato_img=PhotoImage(file="C:/Users/CASPER/Desktop/python_projects/project 39/password-manager-start/logo.png")
canvas.create_image(110,120,image=tomato_img)
canvas.place(x=280,y=50)

website_label=Label(text="Website:",font=("Arial",15,"bold"))  # To create a text
website_label.place(x=80,y=300)  # To determine text's location

website_entry=Entry(width=50)  # To create an input
website_entry.place(x=200,y=305)  # To determine input's location
website_entry.focus()  # To add a blinking cursor

email_username_label=Label(text="Email/Username:",font=("Arial",15,"bold"))
email_username_label.place(x=5,y=350)

email_username_entry=Entry(width=50)
email_username_entry.place(x=200,y=358)
email_username_entry.insert(0,"Example@gmail.com")  # To create a default text

password_label=Label(text="Password:",font=("Arial",15,"bold"))
password_label.place(x=63,y=400)

password_entry=Entry(width=50)
password_entry.place(x=200,y=406)


def appending_to_text_file():
        
    website=website_entry.get() # To store input 
    username_email=email_username_entry.get() # To store input
    password=password_entry.get()  # To store input
    # To store informations in a dictioanary
    new_data={
        website:{
            "Username/email":username_email,
            "password":password
        }    
              }

    if len(website)==0 or len(password)==0:
        # To show a warning in the screen
        messagebox.showinfo(title="oopss",message="Please make sure you haven't left any fields empty") 
    else:
        try:  # Try this codes
            # The path is special for my computer it won't work in your computer
            # And the mode is read so we are going to oppen that file in reading mode
            with open("C:/Users/CASPER/Desktop/python_projects/project 39/password-manager-start/data.json","r") as data_file:
                data=json.load(data_file)  # To convert data to dict.
        except FileNotFoundError:  # If you see FileNotFoundError
            # The mode is w it means write mode
            with open("C:/Users/CASPER/Desktop/python_projects/project 39/password-manager-start/data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)  # to convert dict to json
        else:  # If you don't see any error
            data.update(new_data)
            with open("C:/Users/CASPER/Desktop/python_projects/project 39/password-manager-start/data.json","w") as data_file:
                json.dump(data,data_file,indent=4)

        finally:  # In the end
            # To clear all input's (Entry)
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            email_username_entry.delete(0,END)
           

# To create a button  
add_button=Button(text="Add",width=70,font=("Arial",9,"bold"),command=appending_to_text_file)
add_button.place(x=200,y=440)  # To determine button's location


letters=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["*","/","-","_","!","@","+","^","$","&","?","#"]

# To create a random password
new_password=[]
def generate_password():
    for i in range(3):
        random_letters=random.choice(letters)
        new_password.append(random_letters)
        random_numbers=random.choice(numbers)
        new_password.append(random_numbers)
        random_symbols=random.choice(symbols)
        new_password.append(random_symbols)

    new_password_str=""
    for i in new_password:
        new_password_str+=i

    password_entry.insert(0,new_password_str)  # To add password


generate_password_button=Button(text="Generate Password",width=25,font=("Arial",9,"bold"),command=generate_password)
generate_password_button.place(x=520,y=400)


# To find password
def find_password():
    website=website_entry.get()
    try:  # Try this codes
        with open("C:/Users/CASPER/Desktop/python_projects/project 39/password-manager-start/data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:  # If you see FileNotFoundError
            messagebox.showinfo(title="Eror",message="No Data File Found")  # Show a pop_up in the screen
    else:  # If you don't see any error
        if website in data:
            username_email=data[website]["Username/email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Username/Email: {username_email}\npassword: {password}")
        else:
            messagebox.showinfo(title="Eror",message=f"No details for {website} exists")

            
search_button=Button(text="Search",font=("Arial",9,"bold"),width=25,command=find_password)
search_button.place(x=520,y=303)

window.mainloop()  # If I don't click exit button the window won't close.