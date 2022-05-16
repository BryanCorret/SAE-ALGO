import lecture
import json
import requete2
import requete3

def affichage():
    stop=False
    while not stop:
        print("Bonjour, pour utiliser le programme, veuillez entrer le nom du fichier à ouvrir")
        print("Il y 4 fichiers possible à ouvrir, veuillez choisir lequel: ")
        num = input("1: data_exploitable.json (fichier de base modifié) \n2: data2.json \n3: data3.json \n4: data4.json \n")
        if num == "1":
            filename = 'data_exploitable.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture.principal(data)
            stop = True
        if num == "2":
            filename = 'data2.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture.principal(data)
            stop = True
        if num == "3":
            filename = 'data3.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture.principal(data)
            stop = True
        if num == "4":
            filename = 'data4.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture.principal(data)            
            stop = True

    fini = False
    print("Le fichier étant chargé, veuillez choisir l'action que vous souhaitez effectuer: ")
    while not fini:
        print("Veuillez choisir l'action que vous souhaitez effectuer: ")
        print("1: Afficher le graphe")
        print("2: Voir les collaborateur en commun")
        print("3: Voir la distance entre 2 acteurs")
        print("4: Voir la centralité d'un acteur")
        print("5: Quitter le programme")

        choix = input("Numéro de l'action que vous souhaitez effectuer: ")
        if choix == "1":
            print("Voici le graphe: ")
            lecture.dessiner()
        if choix == "2":
            nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
            nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
            res = requete2.collaborateur_en_commun(nom1, nom2, resultat[0])
            print("Voici les collaborateurs en commun entre " + nom1 + " et " + nom2 + ": ")
            print(res)
            print("\n")
        if choix == "3":
            nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
            nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
            res = requete3.distance(resultat[1], nom1, nom2)
            res = str(res)
            print("Voici la distance entre 2 acteurs: "+ res)
            print("\n")
        if choix == "4":
            print("Voici la centralité d'un acteur: ")
            print(resultat[4])        
        if choix == "5":
            fini = True
            print("Au revoir!")    

print(affichage())            