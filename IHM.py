from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json
import os
import Lecture

Acceuil= Tk()
fic_Choisi = ""
# Fenetre
Acceuil.title("Terrx")
Acceuil.geometry("1024x768")
Acceuil.minsize(1024, 768)
Acceuil.config(background='#262525', bd=0)
# Fenetre


def ChoixFic():
    print("La fenetre choix fichier à était créer")
    nouv = Tk()

    # Fenetre
    nouv.title("Terrx")
    nouv.geometry("900x280")
    nouv.config(background='#262525', bd=0)

    # text1
    Titre = Label(nouv, text="Terrx", font=("Arial", 35), bg='#262525', fg='#940000', ).pack(anchor="n")

    text = Label(nouv, text="Choisissez votre fichier (Attention plus le fichier contient des films plus l'execution sera longue)", font=("Arial", 15), bg='#262525', fg='#940000', ).place(x=25, y=100)

            
    def Quel_fichier(nbfichier):
        if nbfichier == "1":
            fic_Choisi = "data_exploitable.json"
            print(fic_Choisi)

        elif nbfichier == "2":
            fic_Choisi = "data2.json"
            print(fic_Choisi)
       
        elif nbfichier == "3":
            fic_Choisi = "data3.json"
            print(fic_Choisi)
 
        elif nbfichier == "4":
            fic_Choisi = "data4.json"
            print(fic_Choisi)

        elif nbfichier == "5":
            fic_Choisi = "data5.json"  
            print(fic_Choisi)

    
    Boutonf1 = Button(nouv, text="Data1.json (2 films )", font=("Arial", 12), bg='#262525', fg='#940000', command=lambda: Quel_fichier("1") ).place(x=25, y=160) # lambda permet de ne pas exécuter la fonction lors du démarage de la fênetre
    Boutonf2 = Button(nouv, text="Data2.json (4 films )", font=("Arial", 12), bg='#262525', fg='#940000',command=lambda: Quel_fichier("2") ).place(x=230, y=160)

    Boutonf3 = Button(nouv, text="Data3.json (2 films )", font=("Arial", 12), bg='#262525', fg='#940000',command=lambda: Quel_fichier("3") ).place(x=450, y=160)

    Boutonf4 = Button(nouv, text="Data4.json (2 films )", font=("Arial", 12), bg='#262525', fg='#940000', command=lambda :Quel_fichier("4")).place(x=650, y=160)


    stop = False
    while not stop :
        print("Bonjour, pour utiliser le programme, veuillez entrer le nom du fichier à ouvrir")
        print("Il y 4 fichiers possible à ouvrir, veuillez choisir lequel: ")
        num = input("1: data_exploitable.json (fichier de base modifié) \n2: data2.json (2 films) \n3: data3.json (12 films) \n4: data4.json (400 films)\n5: data5.json (1000 films \n") 
        
        if num == "1":
            filename = 'data_exploitable.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le chargement est terminé")
            messagebox.showinfo("Information", "Le chargement est terminé ")
            nouv.destroy()
            stop = True

        elif num == "2":
            filename = 'data2.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le chargement est terminé")
            messagebox.showinfo("Information", "Le chargement est terminé ")
            nouv.destroy()
            stop = True

        elif num == "3":
            filename = 'data3.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le chargement est terminé")
            messagebox.showinfo("Information", "Le chargement est terminé ")
            nouv.destroy()
            stop = True

        elif num == "4":
            filename = 'data4.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le chargement est terminé")
            messagebox.showinfo("Information", "Le chargement est terminé ")
            nouv.destroy()
            stop = True

        elif num == "5":
            filename = 'data5.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            print("Le chargement est terminé")
            messagebox.showinfo("Information", "Le chargement est terminé ")
            nouv.destroy()
            stop = True



def requete(nbrequete):
    def requete1():
        os.system('clear')
        print("Voici le graphe: ")
        lecture.dessiner()


    def requete2():
        os.system('clear')
        nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
        nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
        res = requete2.collaborateur_en_commun(nom1, nom2, resultat[0])
        print("Voici les collaborateurs en commun entre " + nom1 + " et " + nom2 + ": ")
        if res == None:
            print(nom1," ou ",nom2, "est un illustre inconnu ")
        else:
            print(res)
        print("\n")

    def requete3():
        os.system('clear')
        nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
        nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
        res = requete3.distance(resultat[1], nom1, nom2)
        if (res == -1):
            print(nom1," ou ",nom2," est un illustre inconnu")
        elif (res == None):
            print("Les deux acteurs ne sont pas relier par un quelconque chemin")    
        else:
            res = str(res)
            print("Voici la distance entre 2 acteurs: "+ res)
        print("\n")


    def requete4():
        os.system('clear')
        print("Voici l’acteur le plus central du graphe: ")
        res = requete4.centralite(resultat[0])
        print(res)     

    print("La fenetre de requete fichier à était créer")
    nouv = Tk()

    # Fenetre
    nouv.title("Terrx")
    nouv.geometry("800x200")
    nouv.config(background='#262525', bd=0)

    # text1
    Titre = Label(nouv, text="Terrx", font=("Arial", 35), bg='#262525', fg='#940000', ).pack(anchor="n")

    text = Label(nouv, text="Votre requête est en cours merci de Patienter .", font=("Arial", 15), bg='#262525', fg='#940000', ).place(x=25, y=100)
    text = Label(nouv, text="Merci de ne pas appyuer sur d'autre bouton de l'interface . ", font=("Arial", 15), bg='#262525', fg='#940000', ).place(x=25, y=125)
    text = Label(nouv, text="Vous serrez avertis quand le graph sera terminé .", font=("Arial", 15), bg='#262525', fg='#940000', ).place(x=25, y=150)

    if nbrequete == 1:
        requete1()
        nouv.destroy()
        tk.messagebox.showwarning("Requete", "La requête est fini")

    elif nbrequete == 2:
        requete2()
        nouv.destroy()
        tk.messagebox.showwarning("Requete", "La requête est fini")
    elif nbrequete == 3:
        requete3()
        nouv.destroy()
        tk.messagebox.showwarning("Requete", "La requête est fini")
    elif nbrequete == 4:
        requete4()
        nouv.destroy()
        tk.messagebox.showwarning("Requete", "La requête est fini")
    else:
        tk.messagebox.showwarning("Erreur 0001", "La Fonctionnalité n'a pas était encore implémenté")
    
    



# Titre
Titre1 = Label(Acceuil, text="Terrx  ", font=("Arial", 35), bg='#262525', fg='#940000').pack(anchor="n")

# Button requete 1
R1_button = Button(Acceuil, text=" Quelle fichier voulez-charger ?", font=('Arial', 15), bg='#940000',fg='#ECF0F1', width=25, height=3, relief='ridge', command= ChoixFic ,   bd=5).place(x="55", y="150") # Pas de () pour les function car sinon éxcuter au début

# Button requete 2
R2_button = Button(Acceuil, text="Colaborateur Commun", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=20, height=3, relief='ridge', bd=5, command= lambda : requete(2) ).place(x="95", y="350") 

# Button requete 3
R3_button = Button(Acceuil, text="Distance entre deux point", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=23, height=3, relief='ridge', bd=5, command=lambda : requete(3)).place(x="360", y="350") 

# Button requete 4
R4_button = Button(Acceuil, text="Les Points Centraux", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=17, height=3, relief='ridge', bd=5, command=lambda : requete(4)).place(x="650", y="350")

# Button requete 5
R5_button = Button(Acceuil, text="Voir le graphe", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=17, height=3, relief='ridge', bd=5, command=lambda : requete(1)).place(x="95", y="480") 

# Button requete 6
R5_button = Button(Acceuil, text="Le plus long chemin", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=17, height=3, relief='ridge', bd=5, command=lambda : requete(5)).place(x="360", y="480")

# Button requete 7
R6_button = Button(Acceuil, text="Bonus titre a changer", font=('Arial', 15), bg='#940000', fg='#ECF0F1', width=17, height=3, relief='ridge', bd=5, command=lambda : requete(5)).place(x="650", y="480")



Acceuil.mainloop()

