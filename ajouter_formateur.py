import customtkinter
from tkinter import*
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
        CIN_entry.insert(0, row[0])
        nom_entry.insert(0, row[1])
        specialite_entry.insert(0, row[2])
    else:
        pass


def add_to_treeview():
    Formateurs = database.select_formateur()
    tree.delete(*tree.get_children())
    for Formateur in Formateurs:
        tree.insert('', END, values=Formateur)


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    CIN_entry.delete(0, END)
    nom_entry.delete(0, END)
    specialite_entry.delete(0, END)


def delete():
    selected_formateur = tree.focus()
    if not selected_formateur:
        messagebox.showerror('Choose a formateur')
    else:
        CIN = CIN_entry.get()
        database.delete_formateur(CIN)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been deleted successfully')


def update():
    selected_formateur = tree.focus()
    if not selected_formateur:
        messagebox.showerror('Choose a formateur')
    else:
        CIN = CIN_entry.get()
        nom = nom_entry.get()
        specialite = specialite_entry.get()
        formateur_id = database.get_formateur_id(nom)  # Get formateur ID
        if formateur_id is not None:
            database.update_formateur(CIN,nom,specialite,formateur_id)  # Update using formateur ID
            add_to_treeview()
            clear()
            messagebox.showinfo('Data has been updated')
        else:
            messagebox.showerror('Error', 'Formateur ID not found')


def insert():
    CIN = CIN_entry.get()
    Nom = nom_entry.get()
    specialite = specialite_entry.get()
    if not (CIN and Nom and specialite):
        messagebox.showerror('Error', 'Enter all fields')
    elif database.formateur_exists(CIN):
        messagebox.showerror('Error', 'CIN already exists')
    else:
        database.insert_formateur(CIN, Nom, specialite)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been inserted successfully')


title_label = customtkinter.CTkLabel(app, font=font1, text='Formateurs Details', text_color='#fff', bg_color='#0A0B0C')
title_label.place(x=400, y=15)

Frame = customtkinter.CTkFrame(app, bg_color='#0AB0C0', fg_color='#1B1B21', corner_radius=10, border_width=2,
                                border_color='#fff', width=240, height=500)
Frame.place(x=25, y=15)

CIN_label = customtkinter.CTkLabel(Frame, font=font2, text='CIN formateur', text_color='#fff', bg_color='#1B1B21')
CIN_label.place(x=30, y=100)

CIN_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                    border_width=2, width=160)
CIN_entry.place(x=40, y=140)

nom_label = customtkinter.CTkLabel(Frame, font=font2, text='Nom formateur', text_color='#fff', bg_color='#1B1B21')
nom_label.place(x=30, y=200)

nom_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_width=2,
                                   border_color='#B2016C', width=160)
nom_entry.place(x=40, y=240)

specialite_label = customtkinter.CTkLabel(Frame, font=font2, text='Specialite', text_color='#fff', bg_color='#1B1B21')
specialite_label.place(x=30, y=290)

specialite_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_width=2,
                                          border_color='#B2016C', width=160)
specialite_entry.place(x=40, y=320)

add_button = customtkinter.CTkButton(Frame, command=insert, font=font2, text_color='#fff', text='Add', fg_color='#047E43',
                                     hover_color='#025B30', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
add_button.place(x=108, y=380)

update_button = customtkinter.CTkButton(Frame, command=update, font=font2, text_color='#fff', text='Update', fg_color='#E93E05',
                                        hover_color='#BB8F2E', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
update_button.place(x=15, y=380)

clear_button = customtkinter.CTkButton(Frame, command=clear, font=font2, text_color='#fff', text='Clear', fg_color='#F77F00',
                                       hover_color='#ADB548', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
clear_button.place(x=15, y=430)

delete_button = customtkinter.CTkButton(Frame, command=delete, font=font2, text_color='#fff', text='Delete', fg_color='#F70000',
                                        hover_color='#E14545', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=80)
delete_button.place(x=108, y=430)

style = ttk.Style(app)

style.configure('treeview', font=font3, foreground='#fff', background='#0A0B0C', fieldbackground='#ffffff', width=200,
                bg_color='#2E1212')

style.map('Treeview', background=[('selected', '#AA04A7')])

tree = ttk.Treeview(app, height=19)

tree['columns'] = ('CIN', 'Nom', 'Specialite')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('CIN', anchor=tk.CENTER, width=150)
tree.column('Nom', anchor=tk.CENTER, width=150)
tree.column('Specialite', anchor=tk.CENTER, width=150)

tree.heading('CIN', text='CIN')
tree.heading('Nom', text='Nom')
tree.heading('Specialite', text='Specialite')

tree.place(x=350, y=90)

tree.bind('<ButtonRelease>', display_data)
add_to_treeview()

# Button to go back to main
main_button = customtkinter.CTkButton(app, command=open_main, font=font2, text_color='#fff', text='Back to Main',
                                      fg_color='#047E43', hover_color='#025B30', bg_color='#1B1B21', cursor='hand2',
                                      corner_radius=8, width=150)
main_button.place(x=25, y=570)


app.mainloop()
