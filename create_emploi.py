from customtkinter import *
from database import *
from tkinter import *
from tkinter import ttk ,messagebox
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from PIL import Image, ImageTk
import os

# New elegant color scheme
app_color = "#F0E5CF"
menu_color = "#B38867"
menu_text_clr = "#1C1C1C"

app = CTk()
app.title("creation d'emploi")
app.geometry("1000x570+200+80")
app.config(bg=app_color)
app.resizable(False ,False)
app.iconbitmap("calendar.ico")

def open_main():
    # Cancel all scheduled events
    for event_id in range(1, 1000):  # assuming maximum of 1000 scheduled events
        app.after_cancel(event_id)
    app.destroy()
    import main




def open_main():
    app.destroy()
    import main

def inserer_donner():
    group11 = group1.get()
    id_groupe = group11.split()[0]
    if id_groupe=="GROUPE":
        messagebox.showwarning("Warning" ,"Choisis une groupe")
        return

    jour11 = jour1.get()

    if jour11=="Jour":
        messagebox.showwarning("Warning" ,"Choisis un Jour")
        return
    
    formateur11 = formateur1.get()
    id_formateur = formateur11.split()[0]
    
    salle11 = salle1.get()
    id_salle = salle11.split()[0]

    Houraire = Houraire1.get()
    id_Houraire = Houraire.split()[0]

    if formateur11=="FORMATEUR" or salle11=="SALLE" or Houraire == "Houraire":
        messagebox.showwarning("Warning" ,f"Tous les champs sont obligatoires sur {jour11}")
        return

    if int(id_Houraire) == gestion_conflits_houraire(jour11, id_Houraire ,id_salle): 
        messagebox.showwarning("Warning", f"L'heure choisie est déjà occupée. Veuillez en choisir une autre.")
        return
    if int(id_formateur) == gestion_conflits_formateur(jour11, id_Houraire ,id_formateur) or int(id_Houraire) == gestion_conflits_houraire(jour11, id_Houraire ,id_salle): 
        messagebox.showwarning("Warning", f"Le formateur {formateur11[1:]} a un autre groupe de {Houraire[1:7]} à {Houraire[10:16]}")
        return
    if int(id_salle) == gestion_conflits_salle(jour11, id_Houraire,id_salle):
        messagebox.showwarning("Warning", f"La salle {salle11[1:]} est pleine de {Houraire[1:7]} à {Houraire[10:16]}")
        return

    ajouter_à_jour(jour11,id_Houraire ,id_formateur ,id_salle ,id_groupe)
    
    table_emploi.delete(*table_emploi.get_children())

    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Lundi",id_groupe))
    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Mardi",id_groupe))
    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Mercredi",id_groupe))
    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Jeudi",id_groupe))
    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Vendredi",id_groupe))
    table_emploi.insert(parent='' ,index="end" ,values=get_jour("Samedi",id_groupe))

def download_pdf():
    get_groupe = groupe_id.get()
    id_groupe = get_groupe.split()[0]
    if get_groupe=="GROUPE":
        messagebox.showwarning("Warning" ,"choisi une groupe")
        return

    file_name = "emploi_du_temps.pdf"

    pdf = SimpleDocTemplate(file_name ,pagesizes =letter)
    data = [["Jour/Horaire" ,'08:00 - 10:00' ,'10:00 - 12:00','13:00 - 16:00','16:00 - 18:00']]
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    for jour in jours_semaine:
        if get_jour(jour ,id_groupe):
            data.append(get_jour(jour,id_groupe))

    table_width = 500  

    table = Table(data, colWidths=[table_width / len(data[0])] * len(data[0]))

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (1, 1), (-1, -1),12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 18),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)
    elems = [table]
    pdf.build(elems)
    os.system("start emploi_du_temps.pdf")

# Frame for title
frame_title = CTkFrame(app ,height=100 ,width=1000 ,fg_color=app_color)
frame_title.pack()

title = CTkLabel(frame_title,text="Emploi de Temps du" ,font=("Georgia", 27, "bold") ,text_color="#4B0082" ,fg_color=app_color ,bg_color=app_color)
title.place(x=300,y=35) 


group = Groupe()
group1 = CTkOptionMenu(app ,fg_color="white",values=group[1:],text_color="#000")
group1.set("GROUPE")
group1.place(x=620 ,y=40)

# Frame for emploi
emploi_frame_color = "#D7CCC8"
emploi_frame = CTkFrame(app,border_color="#a6b9bd",border_width=1,fg_color=emploi_frame_color,corner_radius=10,height=500 ,width=300)
emploi_frame.place(x=0,y=100)

line=40

jours = ['Lundi' ,'Mardi' ,'Mercredi' ,'Jeudi' ,'Vendredi' ,'Samedi']
jour1 = CTkOptionMenu(emploi_frame ,fg_color=menu_color,values=jours,text_color=menu_text_clr)
jour1.set("Jour")
jour1.place(x=line ,y= 10)

Houraire = Houraire()
Houraire1 = CTkOptionMenu(emploi_frame ,fg_color=menu_color,values=Houraire[1:],text_color=menu_text_clr)
Houraire1.set("Houraire")
Houraire1.place(x=line ,y= 80)

formateur = Formateur()
formateur1 = CTkOptionMenu(emploi_frame ,fg_color=menu_color,values=formateur[1:],text_color=menu_text_clr)
formateur1.set("FORMATEUR")
formateur1.place(x=line ,y= 150)

salle = Salle()
salle1 = CTkOptionMenu(emploi_frame ,fg_color=menu_color,values=salle[1:],text_color=menu_text_clr ,width=140)
salle1.set("SALLE")
salle1.place(x=line ,y= 220)

btn_insert = CTkButton(
    emploi_frame ,
    text="Envoyer",
    fg_color="#1c2f3f" ,
    text_color="#84c7e8" ,
    font=("arial" ,18),
    hover_color="#3c4649",
    command=inserer_donner,
)
btn_insert.place(x=line ,y=290)
main_button = CTkButton(emploi_frame, command=open_main, font=("arial" ,18), text_color='#fff', text='Back to Main',
                                      fg_color='#047E43', hover_color='#025B30', bg_color='#1B1B21', cursor='hand2',
                                      corner_radius=8, width=150)
main_button.place(x=line, y=360)



table_emploi = ttk.Treeview(app ,columns=("Jour/Horaire" ,'08:00 - 10:00' ,'10:00 - 12:00','13:00 - 16:00','16:00 - 18:00') ,show='headings')

table_emploi.heading("Jour/Horaire",text="Jour/Horaire")
table_emploi.heading('08:00 - 10:00',text='08:00 - 10:00')
table_emploi.heading('10:00 - 12:00',text='10:00 - 12:00')
table_emploi.heading('13:00 - 16:00',text='13:00 - 16:00')
table_emploi.heading('16:00 - 18:00',text='16:00 - 18:00')
table_emploi.place(x=300 ,y=250)
table_emploi.column("Jour/Horaire", width=150)
table_emploi.column('08:00 - 10:00', width=130)
table_emploi.column('10:00 - 12:00', width=130)
table_emploi.column('13:00 - 16:00', width=130)
table_emploi.column('16:00 - 18:00', width=130)

frame_pdf = CTkFrame(
    app,
    border_color="#a6b9bd",
    border_width=0,
    fg_color=app_color,
    corner_radius=0,
    height=50,
    width=360
)
frame_pdf.place(x=500 ,y=500)

groupe = Groupe()
groupe_id = CTkOptionMenu(frame_pdf ,fg_color=menu_color,values=groupe[1:],text_color=menu_text_clr,width=40)
groupe_id.set("GROUPE")
groupe_id.place(x=10 ,y=10)



download_img = CTkImage(
    light_image= Image.open('PDF_icon.png'),
    dark_image= Image.open('PDF_icon.png')
)

btn_afficher_pdf = CTkButton(
    frame_pdf,
    image=download_img,
    height=35,
    width=110,
    text="Télecharger PDF",
    fg_color="red",
    hover_color="#c4081b",
    command=download_pdf,
    font=("arial" ,18 ,"bold"),
)

btn_afficher_pdf.place(x=120, y=8)

app.mainloop()
