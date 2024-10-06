import sqlite3

conn = sqlite3.connect('schedule.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Formateurs (
                 id_formateur INTEGER PRIMARY KEY,
                 cin text,
                 nom TEXT,
                 specialite TEXT)
'''
)


cursor.execute('''CREATE TABLE IF NOT EXISTS Salles (
             id_salle INTEGER PRIMARY KEY,
             salle_nom TEXT,
             capacite INTEGER,
             type_salle text
)'''
)


cursor.execute('''CREATE TABLE IF NOT EXISTS Groupes (
             id_groupe INTEGER PRIMARY KEY,
             groupe_nom TEXT,
             nombre_etudiants INTEGER,
             filiere text,
             niveau_formation text
)'''
)


cursor.execute('''CREATE TABLE IF NOT EXISTS jour(
             id_jour INTEGER PRIMARY KEY,
             nom TEXT,
             id_Houraire INTEGER,
             id_formateur INTEGER,
             id_salle INTEGER,
             id_groupe INTEGER,
             FOREIGN KEY(id_formateur) REFERENCES Formateurs(id),
             FOREIGN KEY(id_salle) REFERENCES Salles(id),
             FOREIGN KEY(id_groupe) REFERENCES Groupes(id),
             FOREIGN KEY(id_Houraire) REFERENCES Houraire(id_Houraire)
)

''')

cursor.execute('''create table if not exists Houraire(
    id_Houraire INTEGER PRIMARY KEY,
    Houraire text
)
''')
def Houraire():
    result = cursor.execute("select * from Houraire")
    Houraire_list = [""]
    m=0
    for row in result:
        m+=1
        Houraire_list.append(f"{m} "+row[1])
    return Houraire_list



# ! ajouter
def ajouter_à_jour( nom ,id_Houraire  ,id_formateur ,id_salle ,id_groupe):
    sql = """insert into jour(nom ,id_Houraire  ,id_formateur ,id_salle ,id_groupe)
    values(? ,? ,? ,? ,?)"""
    val = (nom ,id_Houraire  ,id_formateur ,id_salle ,id_groupe)
    cursor.execute(sql ,val)
    conn.commit()
    
def ajouter_à_Formateurs(cin ,nom ,specialite):
    sql = """insert into Formateurs(cin ,nom ,specialite)
    values(?,? ,? )"""
    val = (cin, nom  ,specialite)
    cursor.execute(sql ,val)
    conn.commit()

def ajouter_à_Salles(salle_nom ,capacite ,type_salle):
    sql = """insert into Salles(salle_nom ,capacite ,type_salle)
    values(? ,? ,?)"""
    val = (salle_nom ,capacite ,type_salle)
    cursor.execute(sql ,val)
    conn.commit()
def ajouter_à_Groupes(nom ,nombre_etudiants ,filiere ,niveau_formation):
    sql = """insert into Groupes(groupe_nom ,nombre_etudiants ,filiere ,niveau_formation)
    values(? ,? ,? ,?)"""
    val = (nom ,nombre_etudiants ,filiere ,niveau_formation)
    cursor.execute(sql ,val)
    conn.commit()
    





def insert():

    ajouter_à_Formateurs("A1","nom1", "Informatique")
    ajouter_à_Formateurs("A2","nom1", "Informatique")
    ajouter_à_Formateurs("A3","nom2", "Informatique")
    ajouter_à_Formateurs("A4","nom3", "reseau")
    ajouter_à_Formateurs("A5","nom4", "Anglais")
    ajouter_à_Formateurs("A6","nom5", "economie")
    ajouter_à_Formateurs("A7","nom6", "economie")


    ajouter_à_Salles("SC1", 30,"d'apprentissage")
    ajouter_à_Salles("SC2", 30,"Laboratoire")
    ajouter_à_Salles("SC3", 30,"salle TP")
    ajouter_à_Salles("SC4", 30,"d'apprentissage")
    ajouter_à_Salles("SC5", 30,"Laboratoire")
    ajouter_à_Salles("SC6", 30,"salle TP")
    ajouter_à_Salles("SS3", 30,"d'apprentissage")
    ajouter_à_Salles("SS2", 28,"Laboratoire")
    ajouter_à_Salles("FAD", 43,"salle TP")

    ajouter_à_Groupes("DEV101", 25,"DD","1er année")
    ajouter_à_Groupes("DEV102", 30,"DD","1er année")
    ajouter_à_Groupes("GE101", 20,"GE","1er année")
    ajouter_à_Groupes("GE102", 20,"GE","1er année")
    ajouter_à_Groupes("GE201", 20,"GE","2me année")
    ajouter_à_Groupes("ID101", 20,"ID","1er année")
    ajouter_à_Groupes("ID102", 20 ,"ID","1er année")

    cursor.execute('''insert into Houraire(Houraire) values('08:00 -> 10:00')''')
    cursor.execute('''insert into Houraire(Houraire) values('10:00 -> 12:00')''')
    cursor.execute('''insert into Houraire(Houraire) values('13:00 -> 14:00')''')
    cursor.execute('''insert into Houraire(Houraire) values('14:00 -> 18:00')''')

#insert()


# ! get
def gestion_conflits_houraire(jour ,id_Houraire ,id_salle):
    result = cursor.execute('''select h.id_Houraire from jour j 
    join Houraire h on j.id_Houraire = h.id_Houraire
    join Salles s on s.id_salle = j.id_salle
    where j.nom = ? and h.id_Houraire = ? and s.id_salle = ?''',(jour ,id_Houraire ,id_salle))
    result =cursor.fetchall()
    for row in result:
        return row[0]

def gestion_conflits_formateur(jour ,id_Houraire ,id_formateur):
    result = cursor.execute('''select f.id_formateur from jour j 
    join Formateurs f on f.id_formateur = j.id_formateur
    join Houraire h on j.id_Houraire = h.id_Houraire
    where j.nom = ? and h.id_Houraire = ? and f.id_formateur = ?''',(jour ,id_Houraire ,id_formateur))
    result =cursor.fetchall()
    for row in result:
        return row[0]
def gestion_conflits_salle(jour ,id_Houraire ,id_salle):
    result = cursor.execute('''select s.id_salle from jour j 
    join salles s on s.id_salle = j.id_salle
    join Houraire h on j.id_Houraire = h.id_Houraire
    where j.nom = ? and h.id_Houraire = ? and s.id_salle = ?''',(jour ,id_Houraire ,id_salle))
    result =cursor.fetchall()
    for row in result:
        return row[0]




# Formateur

def insert_formateur(cin,nom,specialite):
    cursor.execute("INSERT INTO FORMATEURS (cin,nom,specialite)values(?,?,?)",(cin,nom,specialite))
    conn.commit()

def select_formateur():
    cursor.execute("SELECT cin ,nom ,specialite FROM Formateurs")
    info = cursor.fetchall()
    return info
def delete_formateur(cin):
    cursor.execute("DELETE  FROM Formateurs where cin=?", ( cin,))
    conn.commit()
def update_formateur(cin ,nom ,specialite,id_formateur):
    cursor.execute("UPDATE Formateurs set nom = ? ,specialite = ? ,cin = ? where id_formateur=?",(nom ,specialite,cin,id_formateur))
    conn.commit()

def formateur_exists(cin):
    conn = sqlite3.connect('schedule')
    conn = conn.cursor()
    cursor.execute('select count(*) from Formateurs where CIN=?',(cin,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def get_formateur_id(formateur_name):
    cursor.execute("SELECT id_formateur FROM Formateurs WHERE nom=?", (formateur_name,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Return the formateur ID if found
    else:
        return None  # Return None if formateur not found



def Formateur():
    result = cursor.execute("select * from Formateurs")
    Formateur_list = [""]
    m=0
    for row in result:
        m+=1
        Formateur_list.append(f"{row[0]} "+row[1])
    return Formateur_list





def select_salle():
    cursor.execute("SELECT salle_nom ,capacite ,type_salle  FROM salles")
    info = cursor.fetchall()
    return info
def delete_salle(salle_nom):
    cursor.execute("DELETE FROM salles WHERE salle_nom = ?", (salle_nom,))
    conn.commit()

def update_salle(salle_nom ,capacite ,type_salle,id_salle):
    cursor.execute("UPDATE salles set capacite = ? , type_salle = ? ,salle_nom = ? where id_salle=?",(capacite ,type_salle,salle_nom,id_salle))
    conn.commit()

def get_salle_id(salle_name):
    cursor.execute("SELECT id_salle FROM Salles WHERE salle_nom=?", (salle_name,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Return the salle ID if found
    else:
        return None  # Return None if salle not found

def insert_salle(salle_nom, capacite, type_salle):
    cursor.execute("INSERT INTO Salles (salle_nom, capacite, type_salle) VALUES (?, ?, ?)",
                   (salle_nom, capacite, type_salle))
    conn.commit()


def Salle():
    result = cursor.execute("select * from Salles")
    Salle_list = [""]
    m=0
    for row in result:
        m+=1
        Salle_list.append(f"{m} "+row[1])
    return Salle_list



# CRUD Groupes
def insert_groupe(groupe_nom, nombre_etudiants, filiere, niveau_formation):
    cursor.execute("INSERT INTO Groupes (groupe_nom, nombre_etudiants, filiere, niveau_formation) VALUES (?, ?, ?, ?)",
                   (groupe_nom, nombre_etudiants, filiere, niveau_formation))
    conn.commit()
def select_groupe():
    cursor.execute("SELECT groupe_nom, nombre_etudiants ,filiere ,niveau_formation FROM Groupes")
    return cursor.fetchall()
def delete__groupe(id_groupe):
    cursor.execute("DELETE FROM Groupes WHERE id_groupe=?", (id_groupe,))
    conn.commit()
def update__groupe(id_groupe, new_groupe_nom, nombre_etudiants, filiere, niveau_formation):
    cursor.execute("UPDATE Groupes SET groupe_nom = ?, nombre_etudiants = ?, filiere = ?, niveau_formation = ? WHERE id_groupe = ?",
                   (new_groupe_nom, nombre_etudiants, filiere, niveau_formation, id_groupe))
    conn.commit()
def get_group_id(group_name):
    cursor.execute("SELECT id_groupe FROM Groupes WHERE groupe_nom=?", (group_name,))
    result = cursor.fetchone()
    if result:
        return result[0]  # Return the group ID if found
    else:
        return None  # Return None if group not found

def Groupe():
    result = cursor.execute("select * from Groupes")
    Groupe_list = [""]
    m=0
    for row in result:
        m+=1
        Groupe_list.append(f"{m} "+row[1])
    return Groupe_list




    
def get_jour(jour ,groupe):
    info_jour = [jour]
    for i in range(1,5):
        result = cursor.execute("""SELECT f.nom ,salle_nom 
        FROM jour j join formateurs f on j.id_formateur = f.id_formateur
        join salles s on j.id_salle = s.id_salle
        join Houraire h on h.id_Houraire = j.id_Houraire
        join Groupes g on g.id_groupe = j.id_groupe
        where j.nom = ? and h.id_Houraire = ? and g.id_groupe = ?""",(jour, i ,groupe))
        result =cursor.fetchall()
        if result:
            for row in result:
                result1 = f"{row[0]}/{row[1]}"
                info_jour.append(result1)
        else:
            info_jour.append("")

    return info_jour
# print(get_jour("Lundi" ,1))

conn.commit()