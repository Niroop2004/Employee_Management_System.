from customtkinter import *
from PIL import Image
from tkinter import ttk , messagebox
import database

#Function to add employee

def delete_all():
    result=messagebox.askyesno('confirm','Do you want to delete all the records?')
    if result:
        database.delete_all_records()
    else:
        pass



def show_all():
    treeview_data()
    searchentry.delete(0,END)
    searchBox.set('Search by')


def search_employee():
    if searchentry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        searched_data=database.search(searchBox.get(),searchentry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete(identry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Your data is deleted')


def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(identry.get(),nameentry.get(),phoneentry.get(),roleBox.get(),genderBox.get(),salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data Updated')


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        identry.insert(0,row[0])
        nameentry.insert(0,row[1])
        phoneentry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryentry.insert(0,row[5])

#in this by default this will now take false value, but if a value is passes to this clear like thta lamda function clear(True) then true is stored in the clear function
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)
    nameentry.delete(0,END)
    phoneentry.delete(0,END)
    roleBox.set('Web developer')
    genderBox.set('Male')
    salaryentry.delete(0,END)



def treeview_data():
    employees=database.fetch_employees ()
    # here, below code means all the children data means previous data that are already printed will be deleated and new added data will be displayed if we dont add this then once again all the data that are printed earlier will again print. to understand that comment out this and run this code
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employee():
    if identry.get()=='' or phoneentry.get()=='' or nameentry.get()=='' or salaryentry.get()=='':
        messagebox.showerror('Error','All Fields are required')

    elif database.id_exists(identry.get()):
        messagebox.showerror('Error','Id already Exists')

    else:
        database.insert(identry.get(),nameentry.get(),phoneentry.get(),roleBox.get(),genderBox.get(),salaryentry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data entered sucessfully')

#In login page we use the window as root here we use it as Window
Window = CTk()
Window.title("Employee Management System")
Window.geometry('1100x580')
Window.configure(fg_color='black')

logo=CTkImage(Image.open('emp.png'),size=(1100,158))
logolabel=CTkLabel(Window,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)
# logolabel.place(x=0,y=0)

leftframe=CTkFrame(Window,fg_color='black')
leftframe.grid(row=1,column=0)

#Id
idlabel=CTkLabel(leftframe,text='Employee_Id',font=('poppins',18,'bold'),text_color='white')
idlabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

identry=CTkEntry(leftframe,font=('poppins',18,'bold'),width=180)
identry.grid(row=0,column=1)
#Name
namelabel=CTkLabel(leftframe,text='Employee_Name',font=('poppins',18,'bold'),text_color='white')
namelabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameentry=CTkEntry(leftframe,font=('poppins',18,'bold'),width=180)
nameentry.grid(row=1,column=1)
#Phone
phonelabel=CTkLabel(leftframe,text='Employee_Phone',font=('poppins',18,'bold'),text_color='white')
phonelabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneentry=CTkEntry(leftframe,font=('poppins',18,'bold'),width=180)
phoneentry.grid(row=2,column=1)

#Role
rolelabel=CTkLabel(leftframe,text='Employee_Role',font=('poppins',18,'bold'),text_color='white')
rolelabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer','Ml Engineer','Data Analyst','Security_analyst','Ai Engineer','Software Developer','Ui/Ux Designer','Network Engineer']
roleBox=CTkComboBox(leftframe,values=role_options,width=180,font=('poppins',15),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

#Gender
genderlabel=CTkLabel(leftframe,text='Employee_Gender',font=('poppins',18,'bold'),text_color='white')
genderlabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options = ['Male','Female','others']
genderBox=CTkComboBox(leftframe,values=gender_options,width=180,font=('poppins',15),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

#salary
salarylabel=CTkLabel(leftframe,text='Employee_Salary',font=('poppins',18,'bold'),text_color='white')
salarylabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryentry=CTkEntry(leftframe,font=('poppins',18,'bold'),width=180)
salaryentry.grid(row=5,column=1)


#START OF RIGHT FRAME
rightframe=CTkFrame(Window)
rightframe.grid(row=1,column=1)


Search_options=['Id','Name','Phone','Gender','Salary']
searchBox=CTkComboBox(rightframe,values=Search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set("Search By")

searchentry=CTkEntry(rightframe)
searchentry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text='Search',width=100,cursor='hand2',command=search_employee)
searchButton.grid(row=0,column=2)

showButton=CTkButton(rightframe,text='Show all',width=100,cursor='hand2',command=show_all)
showButton.grid(row=0,column=3,pady=5)


tree=ttk.Treeview(rightframe,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['column']=('Employee_Id','Employee_Name','Employee_Phone','Employee_Role','Employee_Gender','Employee_Salary')
tree.heading('Employee_Id',text='Id')
tree.heading('Employee_Name',text='Name')
tree.heading('Employee_Phone',text='Phone')
tree.heading('Employee_Role',text='Role')
tree.heading('Employee_Gender',text='Gender')
tree.heading('Employee_Salary',text='Salary')

tree.configure(show='headings')
tree.column('Employee_Id',width=100)
tree.column('Employee_Name',width=100)
tree.column('Employee_Phone',width=100)
tree.column('Employee_Role',width=100)
tree.column('Employee_Gender',width=100)
tree.column('Employee_Salary',width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('popppins',10,'bold')) 
style.configure('Treeview',font=('popppins',9,'bold'))


scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')
tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(Window,fg_color='black')
buttonFrame.grid(row=2,column=0,columnspan=2)

#Here we use lamda function because in this if we press new employee button it will clear but if one data is selected then again it will re enter the data to the boxes in the left frame so in order to solve that we use lamda fuc where some parameteres are passed to the inside function
newbutton = CTkButton(buttonFrame,text='New Employee',font=('poppins',15,'bold'),command=lambda:clear(True))
newbutton.grid(row=0,column=0,pady=5,padx=5)

addbutton = CTkButton(buttonFrame,text='Add Employee',font=('poppins',15,'bold'),command=add_employee)
addbutton.grid(row=0,column=1,pady=5,padx=5)

updatebutton = CTkButton(buttonFrame,text='Update Employee',font=('poppins',15,'bold'),command=update_employee)
updatebutton.grid(row=0,column=2,pady=5,padx=5)

deletebutton = CTkButton(buttonFrame,text='Delete Employee',font=('poppins',15,'bold'),command=delete_employee)
deletebutton.grid(row=0,column=3,pady=5,padx=5)

delete_allbutton = CTkButton(buttonFrame,text='Delete_All Employee',font=('poppins',15,'bold'),command=delete_all)
delete_allbutton.grid(row=0,column=4,pady=5,padx=5)



treeview_data()
#in order to display the window on the screen we use mainloop method.
Window.bind('<ButtonRelease>',selection)

Window.mainloop()

