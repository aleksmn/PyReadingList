from tkinter import *

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


# Buttons

b1 = Button(frame, text="View all", width=12)
b1.grid(row=2, column=3)

b2 = Button(frame, text="Search", width=12)
b2.grid(row=3, column=3)

b3 = Button(frame, text="Add", width=12)
b3.grid(row=4, column=3)

b4 = Button(frame, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(frame, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(frame, text="Close", width=12)
b6.grid(row=7, column=3)


window.mainloop()