# --------------- IMPORT ---------------

import json
import networkx as nx
import matplotlib.pyplot as plt
import lecture 

# ---------------  Fonction utiles pour les requetes  -----------------------------


G = nx.Graph() # Crée un graphe vide

def clearNom(nom):
  """
  Retourne le nom sans les caractères spéciaux(| [] <>)
  """
  if nom[0] == '[':
    nom = nom.replace("[","") # Ce code permet de supprimer le [
    nom = nom.replace("]","") # Ce code permet de supprimer le ]
  if "|" in nom:
    indice = nom.find("|") # Ce code permet de trouver le |
    indice+=1 # Ce code permet de décaler le curseur
    nom = nom[indice:] # Ce code permet de supprimer tt ce qui y'a avant le |  
  if "<" in nom:
    indice = nom.find("<") # Ce code permet de trouver le <
    indice-=1 # Ce code permet de décaler le curseur
    nom = nom[:indice] # Ce code permet de supprimer tt ce qui y'a après le <
  return nom  


def dessiner():
  try :
    nx.draw(G, with_labels=True)
    plt.show()
  except:
    print("Erreur dans le dessin du graph, si vous avez lancé le data_exploitable, le fichier étant trop lourd, le dessin n'est pas possible")



# ------------------- Fonction pour les requetes  ---------------------------------


#Q1
def json_vers_nx(la_data):
  """Retourne le dico avec qui chaque personne à travaillé et le graphe associé

  Args:
      la_data (json): fichier json chargé

  Returns:
      tuple: (dico, graphe)
  """
  dico_de_gens = dict() 
  dico_dacteur_de_chaque_film = dict()
  cpt=0
  for film in la_data:
    cpt+=1
    #print(cpt) # Pour voir le nombre de films chargés
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

#Q2
def collaborateur_en_commun(G, u, v):
    """
    Retourne la liste des collaborateurs communs entre deux gens

    :param u: le nom du premier collaborateur
    :param v: le nom du second collaborateur
    :param G: le graphe
    """
    liste = []
    if u not in G or v not in G:
      return None # Si u ou v n'est pas dans le graphe, on renvoie None
    for nom in G[u]:
      if nom in G[v]:
        liste.append(nom) # Si le nom est dans le graphe, on l'ajoute à la liste
    return liste


#Q3
def distance(G,u,v):
  """
  Fonction renvoyant la distance entre les deux acteurs u et v dans le graphe G. La fonction renvoie None si u est absent du graphe.
  """
  if u not in G.nodes or v not in G.nodes:
    return -1 # Si u ou v n'est pas dans le graphe, on renvoie -1

  chemin_le_plus_court = dict(nx.all_pairs_shortest_path_length(G)) # On récupère le chemin le plus cours entre u et v
  if v in chemin_le_plus_court[u]:
    val = chemin_le_plus_court[u][v] # On récupère la valeur de la distance entre u et v
  else:
    val = None # Si v n'est pas atteignable, on renvoie None
  return val    


#Q4
def centre_hollywood(dico_final):
  """

    Args:
        dico_final (dict): Dico qui contient tout les données du graphe

    Returns:
        List: Liste de le ou les personne qui sont au centre du graphe
    """
  dico_centralite = dict() # dico qui contient les centralites sous form Nom Prenom : [1 2 3  ....] 

  for elem in dico_final: # Pour chaque personne 
      for elem2 in dico_final[elem]: # Pour chaque personne qui a travaillé avec la personne
          dico_centralite[elem2] = []
          n = 2
          for elem3 in dico_final[elem2]:
              dico_centralite[elem2].append(1)
          for elem3 in dico_final[elem2]: 
              dico_centralite[elem2].append(n)
              n += 1


  dico_moy = dict()
  for key in dico_centralite: # Pour chaque personne 
      somme = 0 # Somme des centralites
      dico_moy[key] = 0
      for val in dico_centralite[key]: # On fait la somme du nombre de movement qu'on peut faire
          somme = somme + val
      moy = somme / len(dico_centralite[key]) # On fait la moyenne
      dico_moy[key]= moy
      somme = 0

  liste_point_centralite = []
  mini = min(dico_moy.values()) # On cherche la valeur minimale ( boucle car peut y avoir plusieurs personne avec la meme valeur)
  for key,values in dico_moy.items():  # Pour chaque personne de mon dico avec les moyennes 
      if mini == values: # Si la valeur est égale à la valeur minimale
          liste_point_centralite.append(key) # On ajoute la personne à la liste des personnes avec la meme valeur

  

  return liste_point_centralite # On retourne la liste des personnes 


    
# Q5
def eloignement_max(G):
    """Fonction permettant de determiner la distance maximum dans G entre deux acteurs.
    Parametres:
        G: le graphe
    return:
        int : la distance maximum
    """
    def distance_max(G,u,):
        """Fonction permettant de determiner la distance maximum dans G entre deux acteurs.
        Args:
            G: le graphe
            u: le premier acteur
        return:
            int : la distance maximum
        """ 
        L_distant = list()
        for sommet in G.nodes: # Pour chaque sommet du graphe
          L_distant.append(distance(G, u, sommet)) # On ajoute la distance entre u et le sommet dans la liste
        return max(L_distant) # On retourne la valeur maximale de la liste

  

    L_centralite = list()
    L_sommet = list()
    for sommet in G.nodes: # Pour chaque sommet du graphe
        L_centralite.append(distance_max(G, sommet)) # On ajoute la distance max entre le sommet et les autres dans la liste
        L_sommet.append(sommet) # On ajoute le sommet dans la liste

    return max(L_centralite) # On retourne la valeur maximale de la liste
   



