import lecture4

def collaborateur_en_commun(nom1, nom2, G):
    """
    Retourne la liste des collaborateurs communs entre deux gens
    """
    liste = []
    for nom in G[nom1]:
      if nom in G[nom2]:
        liste.append(nom)
    return liste

#print(collaborateur_en_commun("Núria Espert","Rosa Maria Sardà", lecture4.principal(lecture4.getData())[0]))

