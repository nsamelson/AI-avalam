import json
import pprint
import time
from random import *
from sys import maxsize
from math import inf as infinity
import platform
from os import system
from copy import deepcopy

t0=time.time()
human = -1
computer = +1
temp_board = []
board= [
		[ [],  [],  [], [0], [1],  [],  [],  [],  []],
		[ [],  [],  [], [1], [0], [1], [0], [1],  []],
		[ [],  [], [1], [0], [1], [0], [1], [0], [1]],
		[ [],  [], [0], [1], [0], [1], [0], [1], [0]],
		[ [], [0], [1], [0],  [], [0], [1], [0],  []],
		[[0], [1], [0], [1], [0], [1], [0],  [],  []],
		[[1], [0], [1], [0], [1], [0], [1],  [],  []],
		[ [], [1], [0], [1], [0], [1],  [],  [],  []],
		[ [],  [],  [],  [], [1], [0],  [],  [],  []]
	]
counter = 0
best_board=[]
best_temp_board=[]
new_temp_board=[]
choosing_depth=2
score = []
# temp_board = board.copy()

"""balec de l'evaluation +win + game over je crois"""    
# def evaluate(state):
#     """ return +1 if comp wins, -1 if human wins, 0 if draw"""
#     if wins(state,computer):
#         score = +1
#     elif wins(state,human):
#         score = -1
#     else :
#         score = 0
#     return score
# def wins(state,player):
#     """checking the number of towers that the players have 
#     (having the last number in list his num)
#     """
#     win_state=[[state[0][0]],
#                 [state[0][1]],
#                 [state[1][0]],
#                 [state[1][1]]]
#     if [player] in win_state:
#         return True
#     else : 
#         return False
def game_over(state):
    if len(possible_moves(state))== 0:
        return True
    else:
        return False

def usable_cells(state):
    cells = []
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if 0<len(cell)<5:
                cells.append([x,y])
        
    # print(cells)
    return cells

def valid_move(x,y,a,b,state):
    """
    it must move from one cell to one in row-1 to +1 and col -1 to +1
    the sum of the two cells can't be >5

    x y is row col from that i want to move to row a col b
    
    """
    if [x,y] in usable_cells(state) and [a,b] in usable_cells(state):
        if x-1 <= a <= x+1 and y-1 <= b <= y+1:
            if a == x and b == y:
                return False
            else :
                if len(state[a][b]) <= 5- len(state[x][y]):
                    return True
        else :
            return False
    else:
        return False

def possible_moves(state):
    """
    possible cells are for the cells where we can go
    case is a list of dicts of all possible moves for each cell
    score is for the move score, -1 if favorable for IA, +1 favorable for human and 0 coussi coussa
    """
    
    poss_cells = []
    case = []
    
    for a, row in enumerate(state):
        for b, col in enumerate(row):
            if 0<len(col)<5:
                poss_cells.append([a,b])

    for cell in usable_cells(state):     
          
        for  movingto in poss_cells:
            x=cell[0]
            y=cell[1]
            a=movingto[0]
            b=movingto[1]
            if valid_move(x,y,a,b,state):        
                case.append({"from":cell, "to":movingto,"tscore": int})
                
    # print(pprint.pformat(case))
    return case
            



def set_move(x,y,a,b,state):
    """
    set the move on board if coordinates are valid
    param : player is the current playing (not sure if needed)
    parm x and y : row and col from
    param a and b : row and col to
    """
    
    
    if valid_move(x,y,a,b,state):
        
        state[a][b].extend(state[x][y])
        state[x][y].clear()
        # print("state :",state)
        return True
    else:
        return False

def profondeur(state,depth,player):
    global best_board
    global best_temp_board
    if player == computer:
        best = {"from":list,"to":list,"tscore":infinity}        # + inf because we want then a number smaller
    else :
        best = {"from":list,"to":list,"tscore":-infinity}

    if depth == 0 or game_over(state):
        return best
        
    for move in possible_moves(state):

        if depth ==choosing_depth:
            temp_board = deepcopy(board)
        else:
            temp_board = deepcopy(best_board)
        dscore = 0
        
                
        x= move["from"][0]
        y = move["from"][1]
        a = move["to"][0]
        b = move["to"][1]
        
        
        set_move(x,y,a,b,temp_board)
        for degree in possible_moves(temp_board):
            # print(degree)
            dscore += degree["tscore"]
        
        move.update(tscore = dscore + move["tscore"])
        # print('board',board)
        # print("move",move)
        # print("temp",temp_board)
        if player == computer:
            if best["tscore"]> move["tscore"]:
                best = move     #min value
                best_temp_board = deepcopy(temp_board)
                
            
        else :
            if best["tscore"]< move["tscore"]:
                best = move     #max value
                best_temp_board = deepcopy(temp_board)
        
    set_move(best["from"][0],best["from"][1],best["to"][0],best["to"][1],best_temp_board)
    best_board = deepcopy(best_temp_board)
    print("move",best)
    print("best_board",best_board)
    # print(" moves possibles",possible_moves(best_board))
    
    return minimax(temp_board,depth-1,-player)
    
def minimax(state,depth,player):
    global best_board
    global temp_board
    global new_temp_board
    global counter
    # global score
    
    if player == computer:
        best = {"from":list,"to":list,"tscore":infinity}        # + inf because we want then a number smaller
    else :
        best = {"from":list,"to":list,"tscore":-infinity}

    if depth == 0 or game_over(state):
        return best
    
    

    for move in possible_moves(state):
        # print(move, depth)
        x= move["from"][0]
        y = move["from"][1]
        a = move["to"][0]
        b = move["to"][1]
        
        
        temp_board = deepcopy(state)
        new_state = (temp_board)
        set_move(x,y,a,b,new_state)
        # print ("move",depth," : ",move)
        # print("state",depth," : ",new_state)
        # print ("state", state)
        # print("temp",temp_board)

        counter +=1
        
        minimax(new_state,depth-1,-player)
    
    """
    crate first a function to calculate the score in function of the numbers of 1 and 0 at the last depth
    
    1 == +1
    0 == -1
    if len(pile) == 5:
        1 == +3
        0 == -3

    if player == computer:
        if best["tscore"]> move["tscore"]:
            best = move     #min value
            best_temp_board = deepcopy(temp_board)
            
        
    else :
        if best["tscore"]< move["tscore"]:
            best = move     #max value
            best_temp_board = deepcopy(temp_board) 
    """
        
        

        
        


# def minimax(state,depth,player):
#     """
#     AI function that choose the best move
#     :param state: current state of the board
#     :param depth: node index in the tree (0 <= depth <= 9),
#     but never nine in this case (see iaturn() function) because it will choose
#     a random coordinate if its the first in tic tac toe
#     :param player: an human or a computer
#     :return: a list with [the best row, best col, best score]

#     """
#     if player == computer:
#         best = [-1, -1, -infinity]
#     else:
#         best = [-1, -1, +infinity]

#     for cell in usable_cells(state):
#         x,y = cell[0], cell[1]
#         # print("x",x,"y",y)
#         for proba in usable_cells(state):
#             a,b = proba[0], proba[1]    #it takes all the possibilities it has now i have to put a score for each
#             # print("a",a,"b",b)
#             # score = minimax(state, depth -1, -player)
#             """

#             c'est compliqué!!!!! 
#             de base on met un state 0 pour dire que c'est encore à jouer, +1 pour l'humain
#             et -1 pour l'ia mais ici on joue avec des 1 et 0 et il faut regarder la dernière pièce
#             puis il faut faire en sorte que l'ia comprenne ce qu'elle doit faire

#             """
#             # state[x][y] = 0
#             # score[0],score[1] = x,y
#         # print("best" , best)

# minimax(board,15,computer)

# possible_moves(board)
# profondeur(board)
minimax(board,choosing_depth,human)
print(time.time()-t0)
print(counter)
# # print(board)
# set_move(1,1,2,2,player = computer)
# # print(board)
# # usable_cells(board)
# possible_moves(board)




