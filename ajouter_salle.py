import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
app.geometry('850x600')
app.config(bg="#69F0F8")
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 13, 'bold')

def open_main():
    # Cancel all scheduled events
    for event_id in range(1, 1000):  # assuming maximum of 1000 scheduled events
        app.after_cancel(event_id)
    app.destroy()
    import main




def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        salle_nom_entry.insert(0, row[0])
        capacite_entry.insert(0, row[1])
        type_salle_entry.insert(0, row[2])
    else:
        pass

def add_to_treeview():
    Salles = database.select_salle()
    tree.delete(*tree.get_children())
    for Salle in Salles:
        tree.insert('', END, values=Salle)
    # Schedule the tree update event again
    app.cancel_event = app.after(1000, add_to_treeview)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    salle_nom_entry.delete(0, END)
    capacite_entry.delete(0, END)
    type_salle_entry.delete(0, END)

def delete():
    selected_salle = tree.focus()
    if not selected_salle:
        messagebox.showerror('Choose a salle')
    else:
        salle_nom = salle_nom_entry.get()
        database.delete_salle(salle_nom)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been deleted successfully')

def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Choose a salle')
    else:
        # Get the salle name from the selected item in the treeview
        salle_name = tree.item(selected_item)['values'][0]  # Assuming salle name is the first value

        # Retrieve the salle ID using the salle name
        salle_id = database.get_salle_id(salle_name)
        if salle_id is None:
            messagebox.showerror('Error', f'Salle ID not found for {salle_name}')
            return

        # Get other updated data
        nom = salle_nom_entry.get()
        capacite = capacite_entry.get()
        type_salle = type_salle_entry.get()

        # Update the salle using salle ID
        database.update_salle(nom, capacite, type_salle,salle_id)
        print(salle_name)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been updated')

def insert():
    salle_nom = salle_nom_entry.get()
    capacite = capacite_entry.get()
    type_salle = type_salle_entry.get()
    if not (salle_nom and capacite and type_salle):
        messagebox.showerror('Error', 'Enter all fields')
    else:
        database.insert_salle(salle_nom, capacite, type_salle)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been inserted successfully')

title_label = customtkinter.CTkLabel(app, font=font1, text='Salles Details', text_color='#fff', bg_color='#0A0B0C')
title_label.place(x=400, y=15)

Frame = customtkinter.CTkFrame(app, bg_color='#0AB0C0', fg_color='#1B1B21', corner_radius=10, border_width=2,
                                border_color='#fff', width=240, height=550)
Frame.place(x=25, y=15)

# Inputs entry
salle_nom_label = customtkinter.CTkLabel(Frame, font=font2, text='Nom salle', text_color='#fff', bg_color='#1B1B21')
salle_nom_label.place(x=30, y=100)

salle_nom_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                    border_width=2, width=160)
salle_nom_entry.place(x=40, y=140)

capacite_label = customtkinter.CTkLabel(Frame, font=font2, text='Capacité', text_color='#fff',
                                                bg_color='#1B1B21')
capacite_label.place(x=30, y=200)

capacite_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff',
                                                border_width=2, border_color='#B2016C', width=160)
capacite_entry.place(x=40, y=240)

type_salle_label = customtkinter.CTkLabel(Frame, font=font2, text='Type salle', text_color='#fff',
                                                bg_color='#1B1B21')
type_salle_label.place(x=30, y=290)

type_salle_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_width=2,
                                       border_color='#B2016C', width=160)
type_salle_entry.place(x=40, y=320)

# Buttons
add_button = customtkinter.CTkButton(Frame, command=insert, font=font2, text_color='#fff', text='Add', fg_color='#047E43',
                                     hover_color='#025B30', bg_color='#1B1B21', cursor='hand2', corner_radius=8,
                                     width=80)
add_button.place(x=108, y=380)

update_button = customtkinter.CTkButton(Frame, command=update, font=font2, text_color='#fff', text='Update',
                                        fg_color='#E93E05', hover_color='#BB8F2E', bg_color='#1B1B21',
                                        cursor='hand2', corner_radius=8, width=80)
update_button.place(x=15, y=380)

clear_button = customtkinter.CTkButton(Frame, command=clear, font=font2, text_color='#fff', text='Clear',
                                       fg_color='#F77F00', hover_color='#ADB548', bg_color='#1B1B21',
                                       cursor='hand2', corner_radius=8, width=80)
clear_button.place(x=15, y=430)

delete_button = customtkinter.CTkButton(Frame, command=delete, font=font2, text_color='#fff', text='Delete',
                                        fg_color='#F70000', hover_color='#E14545', bg_color='#1B1B21',
                                        cursor='hand2', corner_radius=8, width=80)
delete_button.place(x=108, y=430)

# Button to go back to main
main_button = customtkinter.CTkButton(app, command=open_main, font=font2, text_color='#fff', text='Back to Main',
                                      fg_color='#047E43', hover_color='#025B30', bg_color='#1B1B21', cursor='hand2',
                                      corner_radius=8, width=150)
main_button.place(x=25, y=570)

style = ttk.Style(app)

style.configure('treeview', font=font3, foreground='#fff', background='#0A0B0C', fieldbackground='#ffffff',
                width=200, bg_color='#2E1212')

style.map('Treeview', background=[('selected', '#AA04A7')])

tree = ttk.Treeview(app, height=19)

tree['columns'] = ('Nom', 'Capacité', 'Type salle')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Nom', anchor=tk.CENTER, width=130)
tree.column('Capacité', anchor=tk.CENTER, width=130)
tree.column('Type salle', anchor=tk.CENTER, width=130)

tree.heading('Nom', text='Nom')
tree.heading('Capacité', text='Capacité')
tree.heading('Type salle', text='Type salle')

tree.place(x=320, y=90)

tree.bind('<ButtonRelease>', display_data)
add_to_treeview()

app.mainloop()
