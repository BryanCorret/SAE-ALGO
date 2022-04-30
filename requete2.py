
def collaborateur_en_commun(nom1, nom2,G):
    """
    Retourne la liste des collaborateurs communs entre deux gens
    """
    liste = []
    for nom in G.adj[nom1]:
      if nom in G.adj[nom2]:
        liste.append(nom) # On ajoute la personne à la liste des collaborateurs communs
    return liste    
