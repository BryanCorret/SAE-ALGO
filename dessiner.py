import lecture3
import networkx as nx

def get_graph():
  """
  Retourne le networkx graph
  """
  G = lecture3.principal(lecture3.data)
  return G


def dessiner(dico,G):
  """
  Dessine le graph
  """
  for elem in dico:
    for elem2 in dico[elem]:
      G.add_edge(elem,elem2)

  nx.draw(G,with_labels=True)
  #plt.show()
  return G      