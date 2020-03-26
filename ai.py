import json
import pprint
import time




output_file = open('move.json').read()
output_json = json.loads(output_file) 


print(pprint.pformat(output_json))

""" ici on check si on peut ajouter ou pas une pile sur une autre """

if 0< len(output_json["game"][0][3]) <5 \
    and 0 < len(output_json["game"][0][4])  <= 5 - len(output_json["game"][0][3]):
    
    output_json["game"][0][4].extend(output_json["game"][0][3]) #on ajoute a la suite de la liste la pile qu'on bouge
    output_json["game"][0][3].clear()    #on clear la liste de la pile qu'on a bougé
    print(pprint.pformat(output_json))      #formater visuellement quand on print (pas faire dans le json)
    
else:
    print("false")

with open("move.json","w") as outfile:
    json.dump(output_json,outfile)  #dump le json
print(outfile)
