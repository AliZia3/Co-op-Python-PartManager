from tkinter import *
from tkinter import messagebox
from info_db import Database

db = Database('store.db')


# Adds all the contents of the database into the listbox widget
def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


# Allows user to add items into the listbox widget and into the database
def add_item():
    texts = [part_entry.get(), customer_entry.get(), retailer_entry.get(), price_entry.get()]

    if texts[0] == '' or texts[1] == '' or texts[2] == '' or texts[3] == '':
        messagebox.showerror("Required Fields", "Please include all Fields")
        return

    db.insert(texts[0], texts[1], texts[2], texts[3])
    parts_list.delete(0, END)

    for i in texts:
        parts_list.insert(END, i)

    clear_input()
    populate_list()


# Used to select item from listbox widget
def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        entries = [part_entry, customer_entry, retailer_entry, price_entry]

        for i in range(len(entries)):
            entries[i].delete(0, END)
            entries[i].insert(END, selected_item[i + 1])
    except IndexError:
        pass


# Allows user to remove the selected item from listbox widget
def remove_item():
    db.remove(selected_item[0])
    clear_input()
    populate_list()


# Allows user to update the content of the item they selected
def update_item():
    db.update(selected_item[0], part_entry.get(), customer_entry.get(), retailer_entry.get(), price_entry.get())
    populate_list()


# Clears all entry fields
def clear_input():
    entries = [part_entry, customer_entry, retailer_entry, price_entry]
    for i in entries:
        i.delete(0, END)


def delete_table():
    db.delete()
    populate_list()


# ==================================================================================
# GUI
root = Tk()
root.geometry('700x350')
root.title('Part Manager')
root.iconbitmap('C:/Python_Projects/Part_Manager/App_Files/Icon.ico')
btn_bg = 'white'
bg = '#464a4d'

# btn_bg = '#30acbf'
# bg = '#1e808f'
fg = 'white'
font = 'Bold 11'

# ==================================================================================

# User-Entry Frame
user_frame = Frame(root, bg=bg)
user_frame.place(relwidth=1, relheight=0.3)

# Parts
part_label = Label(user_frame, text='PART NAME', font=font, anchor='w', bg=bg, fg=fg)
part_label.place(relheight=0.2, relwidth=0.15, rely=0.1)
part_entry = Entry(user_frame, font=font)
part_entry.place(relheight=0.2, relwidth=0.25, relx=0.2, rely=0.1)

# Customer
customer_label = Label(user_frame, text='CUSTOMER', font=font, anchor='w', bg=bg, fg=fg)
customer_label.place(relheight=0.2, relwidth=0.15, relx=0.5, rely=0.1)
customer_entry = Entry(user_frame, font=font)
customer_entry.place(relheight=0.2, relwidth=0.25, relx=0.7, rely=0.1)

# Retailer
retailer_label = Label(user_frame, text='RETAILER', font=font, anchor='w', bg=bg, fg=fg)
retailer_label.place(relheight=0.2, relwidth=0.15, rely=0.6)
retailer_entry = Entry(user_frame, font=font)
retailer_entry.place(relheight=0.2, relwidth=0.25, relx=0.2, rely=0.6)

# Price
price_label = Label(user_frame, text='PRICE', font=font, anchor='w', bg=bg, fg=fg)
price_label.place(relheight=0.2, relwidth=0.15, relx=0.5, rely=0.6)
price_entry = Entry(user_frame, font=font)
price_entry.place(relheight=0.2, relwidth=0.25, relx=0.7, rely=0.6)

# ==================================================================================
# Buttons Frame
btn_frame = Frame(root, bg=bg)
btn_frame.place(relwidth=1, relheight=0.2, rely=0.3)

add_btn = Button(btn_frame, text="Add Part", command=add_item, bg=btn_bg)
add_btn.place(relheight=0.5, relwidth=0.15, relx=0.05, rely=0.1)

remove_btn = Button(btn_frame, text="Remove Part", command=remove_item, bg=btn_bg)
remove_btn.place(relheight=0.5, relwidth=0.15, relx=0.3, rely=0.1)

update_btn = Button(btn_frame, text="Update Part", command=update_item, bg=btn_bg)
update_btn.place(relheight=0.5, relwidth=0.15, relx=0.55, rely=0.1)

clear_btn = Button(btn_frame, text="Clear Input", command=clear_input, bg=btn_bg)
clear_btn.place(relheight=0.5, relwidth=0.15, relx=0.8, rely=0.1)

# ==================================================================================
# Output Frame
output_frame = Frame(root, bg=bg)
output_frame.place(relwidth=1, relheight=0.5, rely=0.5)

parts_list = Listbox(output_frame, font=font)
parts_list.place(relheight=0.9, relwidth=0.7, relx=0.05)

parts_list.bind('<<ListboxSelect>>', select_item)  # Bind select

delete_btn = Button(output_frame, text="Delete Table", command=delete_table, bg=btn_bg)
delete_btn.place(relheight=0.5, relwidth=0.15, relx=0.8, rely=0.2)

populate_list()

root.mainloop()
