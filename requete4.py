import json
import networkx as nx

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

  for elem in dico_de_gens:
    for elem2 in dico_de_gens[elem]:
      G.add_edge(elem,elem2)
  return (dico_de_gens,G)

G = nx.Graph() 

dico_final = principal(data)[0] # dico final avec les doublons en moins
# renvoie le nom des gens avec qui il on travailler



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

