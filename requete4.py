import json
from math import degrees
import networkx as nx
import matplotlib.pyplot as plt

filename = 'data2.json'
json_data = open(filename, encoding="utf8").read()
data = json.loads(json_data)


def clearNom(nom):
    if nom[0] == '[':
        nom = nom.replace("[","")
        nom = nom.replace("]","")
    if "|" in nom:
        indice = nom.find("|")
        indice+=1
        nom = nom[indice:]
    return nom

def clearDoublon(dico):
  for cle in dico:
    dico[cle] = list(set(dico[cle])) # On supprime les doublons
  return dico

def tout_les_gens_du_film(titre):
  list=[]
  for film in range(len(data)):
    if data[film]["title"] == titre:
      for gens in data[film]["cast"]:
        gens = clearNom(gens) 
        
        list.append(gens) 
  return list

def principal(la_data):
  dico_de_gens = dict() 
  for film in range(len(la_data)):
    liste = tout_les_gens_du_film(la_data[film]["title"])
    for gens in liste:
      if gens not in dico_de_gens:
        dico_de_gens[gens] = []
      for personne in liste:
        if personne != gens:
          dico_de_gens[gens].append(personne)
  return dico_de_gens  


dico_final = clearDoublon(principal(data)) # dico final avec les doublons en moins
# renvoie le nom des gens avec qui il on travailler


G = nx.Graph() 

# Centralité IL faut
# calucle l'élgoinement de chaque point
# ex
# u1 - u2 - u3
# [u1 1 2]
# Faire ça pour tout les points et trouver u2 (voir possible moyenne des arrette [u2 1 1])
# ensuite si graphe paire
# u1 - u2 - u3 - u4 
# u2 et u3 sont paire
dico_centralite = dict()

for elem in dico_final:
    for elem2 in dico_final[elem]:
        dico_centralite[elem2] = []
        n = 2
        for elem3 in dico_final[elem2]:
            dico_centralite[elem2].append(1)
        for elem3 in dico_final[elem2]:
            dico_centralite[elem2].append(n)
            n += 1
print(dico_centralite)

dico_moy = dict()
for key in dico_centralite:
    somme = 0
    dico_moy[key] = 0
    for val in dico_centralite[key]:
        somme = somme + val
    moy = somme / len(dico_centralite[key])
    dico_moy[key]= moy
    somme = 0

liste_point_centralite = []
for key,values in dico_moy.items(): 
    mini = min(dico_moy.values())
    if mini == values:
        liste_point_centralite.append(key)
print(f"Le ou les points centralites sont : {liste_point_centralite}")

        

        




for elem in dico_final:
  for elem2 in dico_final[elem]:
    G.add_edge(elem,elem2)

nx.draw(G,with_labels=True)

