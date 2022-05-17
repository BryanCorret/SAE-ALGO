import requetes
import json
import os

def affichage():
    os.system('clear||cls')
    stop=False
    while not stop:
        print("Bonjour, pour utiliser le programme, veuillez entrer le nom du fichier à ouvrir")
        print("Il y 4 fichiers possible à ouvrir, veuillez choisir lequel: ")
        num = input("1: data_exploitable.json (fichier de base modifié) \n2: data2.json (2 films) \n3: data3.json (12 films) \n4: data4.json (400 films)\n5: data5.json (1000 films) \n") 

        if num == "1":
            filename = 'data_exploitable.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = requetes.json_vers_nx(data)
            stop = True

        if num == "2":
            filename = 'data2.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = requetes.json_vers_nx(data)
            stop = True

        if num == "3":
            filename = 'data3.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = requetes.json_vers_nx(data)
            stop = True

        if num == "4":
            filename = 'data4.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = requetes.json_vers_nx(data)            
            stop = True

        if num == "5":
            filename = 'data5.json'
            json_data = open(filename, encoding="utf8").read() 
            data = json.loads(json_data) 
            print("Le fichier est en cours de lecture, Veuillez patienter...")
            resultat = requetes.json_vers_nx(data)
            stop = True

    os.system('clear||cls')
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
            os.system('clear||cls')
            print("Voici le graphe: ")
            requetes.dessiner()



        if choix == "2":
            os.system('clear||cls')
            nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
            nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
            res = requetes.collaborateur_en_commun(nom1, nom2, resultat[0])
            print("Voici les collaborateurs en commun entre " + nom1 + " et " + nom2 + ": ")
            if res == None:
                print(nom1," ou ",nom2, "est un illustre inconnu ")
            else:
                print(res)
            print("\n")


        if choix == "3":
            os.system('clear||cls')
            nom1 = input("Veuillez entrer le nom de l'acteur 1: ")
            nom2 = input("Veuillez entrer le nom de l'acteur 2: ")
            res = requetes.distance(resultat[1], nom1, nom2)
            if (res == -1):
                print(nom1," ou ",nom2," est un illustre inconnu")
            elif (res == None):
                print("Les deux acteurs ne sont pas relier par un quelconque chemin")    
            else:
                res = str(res)
                print("Voici la distance entre 2 acteurs: "+ res)
            print("\n")



        if choix == "4":
            os.system('clear||cls')
            print("Voici l’acteur le plus central du graphe: ")
            res = requetes.centre_hollywood(resultat[0])
            print(res)    
            
                
        if choix == "5":
            os.system('clear||cls')
            fini = True
            print("Au revoir !")    

affichage()      