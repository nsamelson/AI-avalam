import json
import pprint
import time
from random import *

row = 0
col = 4
count =0
output_file = open('move.json').read()
output_json = json.loads(output_file) 


print(pprint.pformat(output_json))

""" ici on check si on peut ajouter ou pas une pile sur une autre """


def gamerules():

    for a in range(row-1,row+2) :
        if a >= 0:    
            for b in range(col-1,col+2):
                if b>=0:
                
                    if 0< len(output_json["game"][row][col]) <5 \
                        and 0 < len(output_json["game"][a][b])  <= 5 - len(output_json["game"][row][col]) :
                        if a == row and b== col:
                            print(a,b,"false")
                        else:
                            
                            output_json["game"][a][b].extend(output_json["game"][row][col]) #on ajoute a la suite de la liste la pile qu'on bouge
                            output_json["game"][row][col].clear()    #on clear la liste de la pile qu'on a bougé
                            output_json["moves"].append({
                                                            "move": {
                                                                "from": [row, col],
                                                                "to": [a, b]
                                                            },
                                                            "message": "I'm Smart"
                                                        })
                            break
                    else:
                        print("false")
                            
    print(pprint.pformat(output_json))

# for c in range (0,3):

#     row = randint(0,8)
#     col = randint(0,8)
#     gamerules()
# for c in range(0,8):
#     for d in range(0,8):
#         row = c
#         col = d
#         gamerules()

gamerules()
with open("move.json","w") as outfile:
    json.dump(output_json,outfile)  #dump le json
print(outfile)