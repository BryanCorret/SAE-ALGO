import json
import networkx as nx
import lecture


dico_final = lecture.principal(lecture.getData())[0] # dico final avec les doublons en moins
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


