import collaborateurs
import lecture
import networkx as nx

def distance(G,u,v):
  """
  Fonction renvoyant la distance entre les deux acteurs u et v dans le graphe G. La fonction renvoie None si u est absent du graphe.
  """
  if u not in G.nodes or v not in G.nodes:
    print(u," ou ",v," est un illustre inconnu")
    return None

  chemin_le_plus_court = dict(nx.all_pairs_shortest_path_length(G)) # On récupère le chemin le plus cours entre u et v
  val = chemin_le_plus_court[u][v] # On récupère la valeur de la distance entre u et v
  return val

  collab1 = collaborateurs.collaborateurs_proches(G,u,val)
  if v in collab1:
    return val


print(distance(lecture4.principal(lecture4.getData())[1],"Rosa Maria Sardà","Bryan C"))

