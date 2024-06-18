from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if UsenameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','All fields must be entered')
    elif UsenameEntry.get()=='Niroop' and PasswordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is Successfull')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid credentials')

#in login page we use the window as root.
root = CTk()

#To give the dimention of the window.
root.geometry('1100x580')
root.resizable(False,False)

image=CTkImage(Image.open('cover.jpg'),size=(1100,580))

#inorder to make the Label like to add text we use label
imageLablel=CTkLabel(root,image=image,text='')
imageLablel.place(x=0,y=0)

headingLabel=CTkLabel(root,text='Employee Management System',bg_color='black',font=('poppins',30,'bold'),text_color='white')
headingLabel.place(x=356,y=110)

#Like in order to enter into the box we use entry methods
UsenameEntry=CTkEntry(root,placeholder_text="Enter Your Username",width=220)
UsenameEntry.place(x=456,y=170)

PasswordEntry=CTkEntry(root,placeholder_text="Enter Your Password",width=220,show='*')
PasswordEntry.place(x=456,y=207)

#Button class is used to add buttons
LoginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
LoginButton.place(x=496,y=250)


#in order to display the window on the screen we use mainloop method for continuously.
root.mainloop()
