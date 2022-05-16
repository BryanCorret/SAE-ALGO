import lecture

def collaborateur_en_commun(nom1, nom2, G):
    """
    Retourne la liste des collaborateurs communs entre deux gens

    :param nom1: le nom du premier collaborateur
    :param nom2: le nom du second collaborateur
    :param G: le graphe
    """
    liste = []
    for nom in G[nom1]:
      if nom in G[nom2]:
        liste.append(nom)
    return liste

#print(collaborateur_en_commun("Núria Espert","Rosa Maria Sardà", lecture.principal(lecture.getData())[0]))

