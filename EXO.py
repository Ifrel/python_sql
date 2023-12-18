from colorama import Fore, Style

import sqlite3
connection = sqlite3.connect("database.db")
conn = connection.cursor()

#Fonction poue création tableau de base de données SQL
def create_table():
    print(Fore.MAGENTA + "Bienvenue, Nous alons procéder à la création de la TABLE base de données SQL" + Style.RESET_ALL)
    print(Fore.RED + "--> Suivez les instructions:" + Style.RESET_ALL + "\n")
    
    #Demande le Nom de la Table base de données SQL
    name = input("Nom de la table : ")
    
    #Demande le nombre d'éléments de la table
    nombre_elements = int(input("Nombre de lignes : "))
    
    #Consignes
    print("\nParfait, Vous allez à present donner les noms des " + Fore.MAGENTA + str(nombre_elements) + " colonnes " + Style.RESET_ALL + " de la table et leurs type :")
    list_type = ["TEXT", "INTEGER", "REAL",]
    list_elements = []
    
    #Demande les noms des éléments de la table et leurs type :
    for i in range(1, nombre_elements + 1):
        element = input("Colonne "+ str(i) + " : ")
        type_element = input("Type: ")
        print()
            
        #Si le type de l'élément n'est pas valide
        if type_element not in list_type:
            print(Fore.RED + "Echec !" + Style.RESET_ALL + " Le type de l'élément " + str(i) + " n'est pas valide")
            exit()      
        
        #On ajoute l'élément et le type de l'élément dans la liste des éléments de la table
        list_elements.append((element, type_element))
    
    # Création de la table
    columns = ', '.join(f"{name} {typ}" for name, typ in list_elements)
    create_table_query = f"CREATE TABLE {name} ({columns})"
    conn.execute(create_table_query)

    print(Fore.GREEN + "Succès" + Style.RESET_ALL + " La table " + name + " a bien été créée")
  
create_table()

all_table = [
    ('Rinel', 20, 1.82, '07 rue René FERNANDAT, 38100, Grenoble.', 'rhinelmak@gmail.com'),
    ('Ifrel', 20, 1.82, '07 rue René FERNANDAT, 38100, Grenoble.', 'rhinelmak@gmail.com'),
    ('MAKOUNDIKA', 20, 1.82, '07 rue René FERNANDAT, 38100, Grenoble.', 'rhinelmak@gmail.com'),
    ('KIDZOUNOU', 20, 1.82, '07 rue René FERNANDAT, 38100, Grenoble.', 'rhinelmak@gmail.com'),
]

conn.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", all_table)

conn.execute("SELECT * FROM students")
val = conn.fetchall()
for i in val:
    print(i)


connection.commit()
connection.close()
