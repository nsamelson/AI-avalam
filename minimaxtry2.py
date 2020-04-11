import json
import pprint
import time
from random import *
from sys import maxsize
from math import inf as infinity
import platform
from os import system
from copy import deepcopy
human = -1
computer = +1
temp_board = []
board= [
		[ [1],  [0],  [1]],
		[ [0],  [1],  [0]],
        [ [1],  [0],  [1]]
	]
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
# def game_over(state):
#     return wins(state,human) or wins(state, computer)

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
    points = 0
    poss_cells = []
    case = []
    for a, row in enumerate(state):
        for b, col in enumerate(row):
            if 0<len(col)<5:
                poss_cells.append([a,b])
    # print(usable_cells(state))
    if state == board:
        points = 2
    elif state == temp_board:
        points = 1

        
    for cell in usable_cells(state):       
        for  movingto in poss_cells:
            x=cell[0]
            y=cell[1]
            a=movingto[0]
            b=movingto[1]
            if valid_move(x,y,a,b,state):
                if state[x][y][-1]== 0:
                    if state[a][b][-1] ==0:
                        tempscore = points
                    elif state[a][b][-1] ==1:
                        tempscore = -points
                elif state[x][y][-1]== 1:
                    if state[a][b][-1] ==0:
                        tempscore = +points
                    elif state[a][b][-1] ==1:
                        tempscore = -points
                case.append({"from":cell, "to":movingto,"tscore": tempscore})
                
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

def profondeur(state):
    # global temp_board
    best = {"from":list,"to":list,"tscore":infinity}
    for move in possible_moves(state):
        temp_board = deepcopy(board)
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
        print('board',board)
        print("move",move)
        print("temp",temp_board)
        if best["tscore"]<= move["tscore"]:
            best = best
        elif best["tscore"]> move["tscore"]:
            best = move
    print("best :",best)
        
        


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

# minimax(board,2,computer)

# possible_moves(board)
profondeur(board)

# # print(board)
# set_move(1,1,2,2,player = computer)
# # print(board)
# # usable_cells(board)
# possible_moves(board)




