from tkinter import *
from tkinter import messagebox #we import it seperately bcoz ?* imports classes and this is not a class
from random import randint,choice,shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 

def password_generator():
    password_list = []
    for char in range(randint(8, 10)):
      password_list.append(choice(letters))

    for char in range(randint(2, 4)):
      password_list += choice(symbols)

    for char in range(randint(2, 4)):
      password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    input_password.insert(0,password)
    print(f"Your password is: {password}")
#----------------------------------------------Encrypting a File----------------------#
"""f = Fernet(key)
key = f.encrypt()
with open('password.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_password.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
"""


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    name_website = input_website.get()
    name_email = input_email.get()
    name_password = input_password.get()

    with open('password.txt','w') as data:
        if len(name_website)==0 or len(name_email)<=3 or len(name_password)==0:
            option = messagebox.showinfo(title="Uhh-ohh", message="Oops missed a field")
        else:
            option = messagebox.askokcancel(title="Confirm",
                                            message=f"Website: {name_website}\nEmail: {name_email}\nPassword: {name_password}\nSave?")
            if option:
                data.write(f"{name_website} || {name_email} || {name_password}\n")
                option = messagebox.showinfo(title="Success", message="Successfully Saved")
                input_password.delete(0, END)
                input_website.delete(0, END)
                data.close()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.config(padx=0, pady=0)
window.geometry('900x574')
"""load = Image.open('lock.png')
render =ImageTK.photoImage(load)"""
render = PhotoImage(file="fill.png")
img_1=PhotoImage(file="add1.png")
img = Label(window,image = render)
img=Label(image=img_1)
img_2=PhotoImage(file="web.png")
img=Label(image=img_2)
img_3=PhotoImage(file="email.png")
img=Label(image=img_3)
img_4=PhotoImage(file="pass.png")
img=Label(image=img_4)
img.place(x= 0,y= 0)
# ----------------------------------------------------------------------------------
canvas = Canvas(width=150, height=200)
timer_img=PhotoImage(file="lock5.png")
create_label=Label(image=timer_img)
create_label.place(x=0,y=0)
canvas.grid(row=0,column=1)

website_label= Label(image=img_2,bg="#075288",height=25,width=100)
#website_label.config(bg="#229954")#
website_label.grid(row=1,column=2)

input_website=Entry(width=25,borderwidth=4)
input_website.grid(row=1,column=3,columnspan=1)
input_website.insert(0,"xyz.com")
input_website.focus()   #Puts cursor in textbox.


email_label= Label(image=img_3,bg="#075288",height=25,width=100)
#email_label.config(bg="#229954")#
email_label.grid(row=2,column=2)

input_email=Entry(width=25,borderwidth=4)
input_email.grid(row=2,column=3,columnspan=1)
input_email.insert(0,"yourname@gmail.com")

password_label= Label(image=img_4,borderwidth=0,bg="#075288",height=25)
#password_label.config(bg="#229954")#
password_label.grid(row=3,column=2)

input_password=Entry(width=25,borderwidth=4)
input_password.grid(row=3,column=3,columnspan=1)
input_password.insert(0,"")

password_button=Button(image = render,command=password_generator,bg="#075288",borderwidth=0,height=30,width=180)
#password_button.config(bg="#229954")#
password_button.grid(row=3,column=4)


add_button=Button(image=img_1,command=save_data,borderwidth=0,width=180,bg="#075288")
#add_button.config(bg="#229954")#
add_button.grid(row=4,column=3,columnspan=1)

window.mainloop()
