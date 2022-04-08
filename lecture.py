import json

filename = 'data2.json'
json_data = open(filename).read()
data = json.loads(json_data)

dico_de_gens = dict() 

def clearNom(nom):
  if nom[0] == '[':
    nom = nom.replace("[","") # Ce code permet de supprimer le [
    nom = nom.replace("]","") # Ce code permet de supprimer le ]
  if "|" in nom:
    indice = nom.find("|") # Ce code permet de trouver le |
    indice+=1 # Ce code permet de décaler le curseur
    nom = nom[indice:] # Ce code permet de supprimer tt ce qui y'a avant le |  
  return nom  


def tout_les_gens_du_film(titre):
  list= []
  for film in range(len(data)):
    if data[film]["title"] == titre:
      for gens in data[film]["cast"]:
        gens = clearNom(gens) 
        gens = gens.encode('latin1').decode('utf8') 
        list.append(gens) 
  return list

for film in range(len(data)):
  titre = data[film]["title"]
  for gens in data[film]["cast"]:
    gens = clearNom(gens) # On supprime les [] et le |
    gens = gens.encode('latin1').decode('utf8') # Ce code permet de convertir les caractères spéciaux en utf8


    liste_de_gens_du_film = tout_les_gens_du_film(titre)
    if gens not in dico_de_gens:
      dico_de_gens[gens] = []
    for personne in liste_de_gens_du_film:
      if personne != gens:
        dico_de_gens[gens].append(personne) 


def clearDoublon(dico):
  for cle in dico:
    dico[cle] = list(set(dico[cle])) # On supprime les doublons
  return dico

dico_final = clearDoublon(dico_de_gens) # dico final avec les doublons en moins

print(dico_final)

