from tkinter import *
from backend import Database

database = Database("books.db")

def get_selected_row(event):
    global selected_tuple
    if len(list1.curselection()) > 0:
        index=list1.curselection()[0]
        selected_tuple = list1.get(index)
        e_title.delete(0, END)
        e_title.insert(END, selected_tuple[1])
        e_author.delete(0, END)
        e_author.insert(END, selected_tuple[2])
        e_year.delete(0, END)
        e_year.insert(END, selected_tuple[3])
        e_date.delete(0, END)
        e_date.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(),  year_text.get(),  date_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(),  year_text.get(),  date_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),  year_text.get(),  date_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(),  year_text.get(),  date_text.get())


# UI

window = Tk()
window.title('PyReadingList')
#window.configure(bg='floral white')

frame = Frame(window)
frame.grid(padx=20, pady=20)


# Labels

l_title = Label(frame, text="Title")
l_title.grid(row=0, column=0)

l_author = Label(frame, text="Author")
l_author.grid(row=0, column=2)

l_year = Label(frame, text="Year")
l_year.grid(row=1, column=0)

l_date = Label(frame, text="Date")
l_date.grid(row=1, column=2)


# Entries

title_text=StringVar()
e_title = Entry(frame,textvariable=title_text)
e_title.grid(row=0, column=1)

author_text=StringVar()
e_author = Entry(frame,textvariable=author_text)
e_author.grid(row=0, column=3)

year_text=StringVar()
e_year = Entry(frame,textvariable=year_text)
e_year.grid(row=1, column=1)

date_text=StringVar()
e_date = Entry(frame,textvariable=date_text)
e_date.grid(row=1, column=3)


# List and Scrollbar

list1 = Listbox(frame, height=8, width=25)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1= Scrollbar(frame)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# Buttons

b1 = Button(frame, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(frame, text="Search", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(frame, text="Add", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(frame, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(frame, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(frame, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()