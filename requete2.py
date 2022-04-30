import lecture
import json
filename = 'data2.json' # Le nom du fichier
json_data = open(filename, encoding="utf8").read() # ouvre le fichier
data = json.loads(json_data) # charge le fichier json

def collaborateur_en_commun(nom1, nom2, G):
    """
    Retourne la liste des collaborateurs communs entre deux gens
    """
    liste = []
    for nom in G[nom1]:
      if nom in G[nom2]:
        liste.append(nom)
    return liste

#print(collaborateur_en_commun("Núria Espert","Rosa Maria Sardà", lecture.principal(data)))
