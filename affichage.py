import lecture4
import json

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
            resultat = lecture4.principal(data)
            stop = True
        if num == "2":
            filename = 'data2.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture4.principal(data)
            stop = True
        if num == "3":
            filename = 'data3.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture4.principal(data)
            stop = True
        if num == "4":
            filename = 'data4.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = lecture4.principal(data)            
            stop = True

    fini = False
    while not fini:
        print("Le fichier étant chargé, veuillez choisir l'action que vous souhaitez effectuer: ")
        print("1: Afficher le graphe")
        print("2: Voir les collaborateur en commun")
        print("3: Voir la distance entre 2 acteurs")
        print("4: Voir la centralité d'un acteur")
        print("5: Quitter le programme")

        choix = input("Numéro de l'action que vous souhaitez effectuer: ")
        if choix == "1":
            print("Voici le graphe: ")
            print(resultat[1])
        if choix == "2":
            print("Voici les collaborateurs en commun: ")
            print(resultat[2])
        if choix == "3":
            print("Voici la distance entre 2 acteurs: ")
            print(resultat[3])
        if choix == "4":
            print("Voici la centralité d'un acteur: ")
            print(resultat[4])        
        if choix == "5":
            fini = True
            print("Au revoir!")    

print(affichage())            