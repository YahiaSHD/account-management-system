from tkinter import *
from tkinter import messagebox
import account_management

window = Tk()
window.title("Account Management System")
window.config(bg="navajo white")
window.geometry('1350x750')
s=()
def clear():
    EntryFirstName.delete(0,END)
    EntryLastName.delete(0,END)
    EntryUserName.delete(0,END)
    EntryPassword.delete(0,END)
    EntryPosition.delete(0,END)
    EntryDate.delete(0,END)
    lb.delete(0,END)

def view():
    lb.delete(0,END)
    for row in account_management.viewall():
        lb.insert(END, row)
def search():
    lb.delete(0,END)
    for row in account_management.search(firstname=EntryFirstName.get(),lastname=EntryLastName.get(),username=EntryUserName.get(),password=EntryPassword.get(),position=EntryPosition.get()):
        lb.insert(END, row)
def add():
    account_management.add(EntryFirstName.get(),EntryLastName.get(),EntryUserName.get(),EntryPassword.get(),EntryPosition.get(),EntryDate.get())
    messagebox.showinfo("ADD","New Account is Added Successfully")
    lb.delete(0,END)
    lb.insert(END,EntryFirstName.get(),EntryLastName.get(),EntryUserName.get(),EntryPassword.get(),EntryPosition.get(),EntryDate.get())

def get_selected_row(events):
    try:
        global slected_tuple,s
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        EntryFirstName.delete(0,END)
        EntryFirstName.insert(END,selected_tuple[1])

        EntryLastName.delete(0, END)
        EntryLastName.insert(END, selected_tuple[2])

        EntryUserName.delete(0, END)
        EntryUserName.insert(END, selected_tuple[3])

        EntryPassword.delete(0, END)
        EntryPassword.insert(END, selected_tuple[4])

        EntryPosition.delete(0, END)
        EntryPosition.insert(END, selected_tuple[5])

        EntryDate.delete(0, END)
        EntryDate.insert(END, selected_tuple[6])
        s=selected_tuple
    except IndexError:
        pass
def update():
    account_management.update(s[0],EntryFirstName.get(),EntryLastName.get(),EntryUserName.get(),EntryPassword.get(),EntryPosition.get(),EntryDate.get())
    messagebox.showinfo("Update", "Account Has Been Updated Successfully")
    view()
def delete():
    account_management.delete(s[0])
    view()
#Labels
label0=Label(window,text="FirstName")
label0.grid(row=0,column=0)
label1=Label(window,text="LastName")
label1.grid(row=1,column=0)
label2=Label(window,text="UserName")
label2.grid(row=2,column=0)
label3=Label(window,text="Password")
label3.grid(row=3,column=0)
label4=Label(window,text="Position")
label4.grid(row=4,column=0)
label5=Label(window,text="Date")
label5.grid(row=5,column=0)
#Entery
EntryFirstName=Entry(window)
EntryFirstName.grid(row=0,column=1)
EntryLastName=Entry(window)
EntryLastName.grid(row=1,column=1)
EntryUserName=Entry(window)
EntryUserName.grid(row=2,column=1)
EntryPassword=Entry(window)
EntryPassword.grid(row=3,column=1)
EntryPosition=Entry(window)
EntryPosition.grid(row=4,column=1)
EntryDate=Entry(window)
EntryDate.grid(row=5,column=1)
#Buttons
btn0=Button(window,text="Clear",command=clear)
btn0.grid(row=1,column=2)
btn1=Button(window,text="View_All",command=view)
btn1.grid(row=1,column=3)
btn2=Button(window,text="Search",command=search)
btn2.grid(row=1,column=4)
btn3=Button(window,text="Update",command=update)
btn3.grid(row=4,column=2)
btn4=Button(window,text="Add",command=add)
btn4.grid(row=4,column=3)
btn5=Button(window,text="Delete",command=delete)
btn5.grid(row=4,column=4)
#lb
lb=Listbox(window,height=20,width=95)
lb.grid(row=6,columnspan=5)
lb.bind("<<ListboxSelect>>",get_selected_row)

window.mainloop()