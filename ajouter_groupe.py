import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import database

app = customtkinter.CTk()
# app.title('Ajouter groupe')
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
        nom_entry.insert(0, row[0])
        nombre_etudiants_entry.insert(0, row[1])
        filiere_entry.insert(0, row[2])
        niveau_formation_entry.insert(0, row[3])
    else:
        pass


def add_to_treeview():
    Groupes = database.select_groupe()
    tree.delete(*tree.get_children())
    for Groupe in Groupes:
        tree.insert('', END, values=Groupe)


def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    nom_entry.delete(0, END)
    nombre_etudiants_entry.delete(0, END)
    filiere_entry.delete(0, END)
    niveau_formation_entry.delete(0, END)


def delete():
    selected_groupe = tree.focus()
    if not selected_groupe:
        messagebox.showerror('Choose a group')
    else:
        nom = nom_entry.get()
        database.delete__groupe(nom)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been deleted successfully')


def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Choose a group')
    else:
        # Get the group name from the selected item in the treeview
        group_name = tree.item(selected_item)['values'][0]  # Assuming group name is the first value

        # Retrieve the group ID using the group name
        group_id = database.get_group_id(group_name)
        if group_id is None:
            messagebox.showerror('Error', f'Group ID not found for {group_name}')
            return

        # Get other updated data
        nom = nom_entry.get()
        nombre_etudiants = nombre_etudiants_entry.get()
        filiere = filiere_entry.get()
        niveau_formation = niveau_formation_entry.get()

        # Update the group using group ID
        database.update__groupe(group_id, nom, nombre_etudiants, filiere, niveau_formation)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been updated')




def insert():
    nom = nom_entry.get()
    nombre_etudiants = nombre_etudiants_entry.get()
    filiere = filiere_entry.get()
    niveau_formation = niveau_formation_entry.get()
    if not (nom and nombre_etudiants and filiere and niveau_formation):
        messagebox.showerror('Error', 'Enter all fields')
    else:
        database.insert_groupe(nom, nombre_etudiants, filiere, niveau_formation)
        add_to_treeview()
        clear()
        messagebox.showinfo('Data has been inserted successfully')


title_label = customtkinter.CTkLabel(app, font=font1, text='Groupes Details', text_color='#fff', bg_color='#0A0B0C')
title_label.place(x=400, y=15)

Frame = customtkinter.CTkFrame(app, bg_color='#0AB0C0', fg_color='#1B1B21', corner_radius=10, border_width=2,
                                border_color='#fff', width=240, height=550)
Frame.place(x=25, y=15)

# Inputs entry
nom_label = customtkinter.CTkLabel(Frame, font=font2, text='Nom groupe', text_color='#fff', bg_color='#1B1B21')
nom_label.place(x=30, y=100)

nom_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_color='#B2016C',
                                    border_width=2, width=160)
nom_entry.place(x=40, y=140)

nombre_etudiants_label = customtkinter.CTkLabel(Frame, font=font2, text='Nombre étudiants', text_color='#fff',
                                                bg_color='#1B1B21')
nombre_etudiants_label.place(x=30, y=200)

nombre_etudiants_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff',
                                                border_width=2, border_color='#B2016C', width=160)
nombre_etudiants_entry.place(x=40, y=240)

filiere_label = customtkinter.CTkLabel(Frame, font=font2, text='Filière', text_color='#fff', bg_color='#1B1B21')
filiere_label.place(x=30, y=290)

filiere_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff', border_width=2,
                                       border_color='#B2016C', width=160)
filiere_entry.place(x=40, y=320)

niveau_formation_label = customtkinter.CTkLabel(Frame, font=font2, text='Niveau formation', text_color='#fff',
                                                bg_color='#1B1B21')
niveau_formation_label.place(x=30, y=370)

niveau_formation_entry = customtkinter.CTkEntry(Frame, font=font2, text_color='#000', fg_color='#fff',
                                                border_width=2, border_color='#B2016C', width=160)
niveau_formation_entry.place(x=40, y=400)

# Buttons
add_button = customtkinter.CTkButton(Frame, command=insert, font=font2, text_color='#fff', text='Add', fg_color='#047E43',
                                     hover_color='#025B30', bg_color='#1B1B21', cursor='hand2', corner_radius=8,
                                     width=80)
add_button.place(x=108, y=460)

update_button = customtkinter.CTkButton(Frame, command=update, font=font2, text_color='#fff', text='Update',
                                        fg_color='#E93E05', hover_color='#BB8F2E', bg_color='#1B1B21',
                                        cursor='hand2', corner_radius=8, width=80)
update_button.place(x=15, y=460)

clear_button = customtkinter.CTkButton(Frame, command=clear, font=font2, text_color='#fff', text='Clear',
                                       fg_color='#F77F00', hover_color='#ADB548', bg_color='#1B1B21',
                                       cursor='hand2', corner_radius=8, width=80)
clear_button.place(x=15, y=510)

delete_button = customtkinter.CTkButton(Frame, command=delete, font=font2, text_color='#fff', text='Delete',
                                        fg_color='#F70000', hover_color='#E14545', bg_color='#1B1B21',
                                        cursor='hand2', corner_radius=8, width=80)
delete_button.place(x=108, y=510)

style = ttk.Style(app)

style.configure('treeview', font=font3, foreground='#fff', background='#0A0B0C', fieldbackground='#ffffff',
                width=200, bg_color='#2E1212')

style.map('Treeview', background=[('selected', '#AA04A7')])

tree = ttk.Treeview(app, height=19)

tree['columns'] = ('Nom', 'Nombre Étudiants', 'Filière', 'Niveau Formation')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Nom', anchor=tk.CENTER, width=130)
tree.column('Nombre Étudiants', anchor=tk.CENTER, width=130)
tree.column('Filière', anchor=tk.CENTER, width=130)
tree.column('Niveau Formation', anchor=tk.CENTER, width=130)

tree.heading('Nom', text='Nom')
tree.heading('Nombre Étudiants', text='Nombre Étudiants')
tree.heading('Filière', text='Filière')
tree.heading('Niveau Formation', text='Niveau Formation')

tree.place(x=320, y=90)

tree.bind('<ButtonRelease>', display_data)
add_to_treeview()

# Button to go back to main
main_button = customtkinter.CTkButton(app, command=open_main, font=font2, text_color='#fff', text='Back to Main',
                                      fg_color='#047E43', hover_color='#025B30', bg_color='#1B1B21', cursor='hand2',
                                      corner_radius=8, width=150)
main_button.place(x=25, y=570)


app.mainloop()
