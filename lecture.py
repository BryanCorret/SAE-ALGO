import json
import networkx as nx
import matplotlib.pyplot as plt

filename = 'data2Modifie.json' # Le nom du fichier
json_data = open(filename, encoding="utf8").read() # ouvre le fichier
data = json.loads(json_data) # charge le fichier json

G = nx.Graph() # Crée un graphe vide

def getData():
  return data

def clearNom(nom):
  """
  Retourne le nom sans les caractères spéciaux(| et [])
  """
  if nom[0] == '[':
    nom = nom.replace("[","") # Ce code permet de supprimer le [
    nom = nom.replace("]","") # Ce code permet de supprimer le ]
  if "|" in nom:
    indice = nom.find("|") # Ce code permet de trouver le |
    indice+=1 # Ce code permet de décaler le curseur
    nom = nom[indice:] # Ce code permet de supprimer tt ce qui y'a avant le |  
  return nom  

def principal(la_data):
  """
  Retourne le dico avec qui chaque personne à travaillé
  """
  dico_de_gens = dict() 
  dico_dacteur_de_chaque_film = dict()
  for film in la_data:
    if film["title"] not in dico_dacteur_de_chaque_film:
      dico_dacteur_de_chaque_film[film["title"]] = [] # Si le film n'est pas dans le dico, on l'ajoute
    for acteur in film["cast"]:
      dico_dacteur_de_chaque_film[film["title"]].append(clearNom(acteur)) # On ajoute l'acteur à la liste du film
    for gens in dico_dacteur_de_chaque_film[film["title"]]:
      if gens not in dico_de_gens:
        dico_de_gens[gens] = [] # Si la personne(gens) n'est pas dans le dico, on l'ajoute
      for personne in dico_dacteur_de_chaque_film[film["title"]]:
        G.add_node(personne) # On ajoute la personne à la liste des nodes
        if personne != gens:
          dico_de_gens[gens].append(personne) # On ajoute la personne à la liste des collaborateurs de la personne

  for elem in dico_de_gens:
    for elem2 in dico_de_gens[elem]:
      G.add_edge(elem,elem2)
  return (dico_de_gens,G)

def dessiner():
  nx.draw(G,with_labels=True)
  plt.show()

def lancer(data):
  """
  Lance le programme
  """
  
  dico_final = principal(getData())[0] # On récupère le dico
  dessiner() # On dessine le graphe
  return dico_final

print(lancer(data))