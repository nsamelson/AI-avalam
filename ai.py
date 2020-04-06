import json
import pprint
import time
from random import *

row = 0
col = 4
count =0
# output_file = open('move.json').read()
# output_json = json.loads(output_file) 
# print(pprint.pformat(output_json))

""" ici on check si on peut ajouter ou pas une pile sur une autre en checkant chaque position si oui ou non """


# def gamerules():
#     global output_json

#     for a in range(row-1,row+2) :
#         if a >= 0:    
#             for b in range(col-1,col+2):
#                 if b>=0:
                
#                     if 0< len(output_json["game"][row][col]) <5 \
#                         and 0 < len(output_json["game"][a][b])  <= 5 - len(output_json["game"][row][col]) :
#                         if a == row and b== col:
#                             print(a,b,"false")
#                         else:
                            
#                             output_json["game"][a][b].extend(output_json["game"][row][col]) #on ajoute a la suite de la liste la pile qu'on bouge
#                             output_json["game"][row][col].clear()    #on clear la liste de la pile qu'on a bougé
#                             output_json["moves"].append({
#                                                             "move": {
#                                                                 "from": [row, col],
#                                                                 "to": [a, b]
#                                                             },
#                                                             "message": "I'm Smart"
#                                                         })
#                             break
#                     else:
#                         print("false")
                            
#     print(pprint.pformat(output_json))

# for c in range (0,3):

#     row = randint(0,8)
#     col = randint(0,8)
#     gamerules()
# for c in range(0,8):
#     for d in range(0,8):
#         row = c
#         col = d
#         gamerules()

# gamerules()



""" On va creer une class avec tout
1. on va chercher le json et extraire les données importantes(game, move (col,row),players)
2 l'ia va checker le meilleur move à faire dans une boucle (while true et appele la fonction "gamerules" pour checker si le move est accepté ou pas)
3. la focntion gamerules va checker si le move demandé est ok, si oui il return un false
4. on modifie le dic (game, move (col,row),message,players,you)
5. on renvoie le json
"""
class Avalam:
    def __init__(self,colfrom,rowfrom,colto,rowto,players = str):
        self.colfrom = colfrom
        self.rowfrom = rowfrom
        self.colto = colto
        self.rowto = rowto
        self.jfile = open('move.json').read()
        self.injson = json.loads(self.jfile)
        print("test")
        self.jsonextract()
    def jsonextract(self):
        
        print(pprint.pformat(self.injson))
        self.ai()
    def ai(self):
        
        while True:
            print("test 1")
            self.gamerules()
            print("test 2 ")
            break
            
    def gamerules(self):
        
                        
        if self.rowfrom -1 <= self.rowto <= self.rowfrom +1 and 0<= self.rowto <= 8 and \
            self.colfrom -1 <= self.colto <= self.colfrom +1 and 0<= self.colto <= 8 :
            if self.rowto == self.rowfrom and self.colto == self.colfrom:
                print("erreur 2")
            else:
                 
                if 0< len(self.injson["game"][self.rowfrom][self.colfrom]) <5\
                    and 0 < len(self.injson["game"][self.rowto][self.colto])  <= 5 - len(self.injson["game"][self.rowfrom][self.colfrom]) :
                        self.moving() 
                else :
                    print("erreur 3")
        else:
            print("erreur 1")

                        
    def moving(self):
        self.injson["game"][self.rowto][self.colto].extend(self.injson["game"][self.rowfrom][self.colfrom]) #on ajoute a la suite de la liste la pile qu'on bouge
        self.injson["game"][self.rowfrom][self.colfrom].clear()    #on clear la liste de la pile qu'on a bougé
        self.injson["moves"].append({
                                        "move": {
                                            "from": [self.rowfrom, self.colfrom],
                                            "to": [self.rowto, self.colto]
                                        },
                                        "message": "I'm Smart"
                                    })
        print(pprint.pformat(self.injson))


class AI:
    def testing(self):
        avalam.__init__(colfrom =3 ,rowfrom= 0,colto = 4,rowto=2)

avalam = Avalam(colfrom =3 ,rowfrom= 0,colto = 4,rowto=2)
avalam



# with open("move.json","w") as outfile:
#     json.dump(self.injson,outfile)  #dump le json
# print(outfile)