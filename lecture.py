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

def principal(la_data):
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
  return dico_de_gens 
  
def dessiner(dico,G):
  """
  Dessine le graph
  """
  for elem in dico:
    for elem2 in dico[elem]:
      G.add_edge(elem,elem2)

  nx.draw(G,with_labels=True)
  plt.show()
  # return G      

def lancer(data):
  dico_final = principal(data) # On récupère le dico
  dessiner(dico_final,G)
  # return dico_final

print(lancer(data))