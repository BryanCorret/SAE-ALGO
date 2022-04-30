import collaborateurs
import lecture4


def distance(G,u,v):
    """
    Fonction renvoyant la distance entre les deux acteurs u et v dans le graphe G. La fonction renvoie None si u est absent du graphe.
    """
    if u not in G.nodes or v not in G.nodes:
      print(u," ou ",v," est un illustre inconnu")
      return None
    distance = 1
    
    while True:
      collab1 = collaborateurs.collaborateurs_proches(G,u,distance)
      collab2 = collaborateurs.collaborateurs_proches(G,v,distance)
      for elem in collab1:
        if elem in collab2:
          return distance*2
      distance += 1

#print(distance(lecture4.principal(lecture4.getData())[1],"NOM1","NOM2"))

