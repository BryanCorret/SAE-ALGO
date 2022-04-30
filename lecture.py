import json
import networkx as nx
import matplotlib.pyplot as plt

filename = 'data2.json' # Le nom du fichier
json_data = open(filename, encoding="utf8").read() # ouvre le fichier
data = json.loads(json_data) # charge le fichier json

G = nx.Graph() # Crée un graphe vide

def clearNom(nom):
  if nom[0] == '[':
    nom = nom.replace("[","") # Ce code permet de supprimer le [
    nom = nom.replace("]","") # Ce code permet de supprimer le ]
  if "|" in nom:
    indice = nom.find("|") # Ce code permet de trouver le |
    indice+=1 # Ce code permet de décaler le curseur
    nom = nom[indice:] # Ce code permet de supprimer tt ce qui y'a avant le |  
  return nom  


def tout_les_gens_du_film(titre):
  list=[] 
  for film in range(len(data)):
    if data[film]["title"] == titre:
      for gens in data[film]["cast"]:
        gens = clearNom(gens)  # On supprime les [] et le |
        list.append(gens) # On ajoute le gens à la liste
  return list

def principal(la_data):
  dico_de_gens = dict() 
  for film in range(len(la_data)):
    liste = tout_les_gens_du_film(la_data[film]["title"])
    for gens in liste:
      if gens not in dico_de_gens:
        dico_de_gens[gens] = [] # Si la personne(gens) n'est pas dans le dico, on l'ajoute
      for personne in liste:
        G.add_node(personne) # On ajoute la personne à la liste des nodes
        if personne != gens:
          dico_de_gens[gens].append(personne) # On ajoute la personne à la liste des collaborateurs de la personne
  return dico_de_gens        


def lancer():
  dico_final = principal(data) # On récupère le dico
