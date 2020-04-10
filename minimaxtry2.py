import json
import pprint
import time
from random import *
from sys import maxsize
from math import inf as infinity
import platform
from os import system

human = -1
computer = +1

board= [
		[ [1],  [0],  [1]],
		[ [0],  [1],  [0]],
        [ [1],  [0],  [1]]
	]

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
    print(cells)
    return cells
def valid_move(x,y,a,b):
    """
    it must move from one cell to one in row-1 to +1 and col -1 to +1
    the sum of the two cells can't be >5

    x y is row col from that i want to move to row a col b
    
    """
    if [x,y] in usable_cells(board) and [a,b] in usable_cells(board):
        if x-1 <= a <= x+1 and y-1 <= b <= y+1:
            if a == x and b == y:
                return False
            else :
                if len(board[a][b]) <= 5- len(board[x][y]):
                    return True
        else :
            return False
    else:
        return False


def set_move(x,y,a,b,player):
    """
    set the move on board if coordinates are valid
    param : player is the current playing (not sure if needed)
    parm x and y : row and col from
    param a and b : row and col to
    """
    if valid_move(x,y,a,b):
        board[a][b].extend(board[x][y])
        board[x][y].clear()
        # print(board)
        return True
    else:
        return False

def minimax(state,depth,player):
    """
    AI function that choose the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function) because it will choose
    a random coordinate if its the first in tic tac toe
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]

    """
    if player == computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    for cell in usable_cells(state):
        x,y = cell[0], cell[1]
        # print("x",x,"y",y)
        for proba in usable_cells(state):
            a,b = proba[0], proba[1]#it takes all the possibilities it has now i have to put a score for each
            # print("a",a,"b",b)
            # score = minimax(state, depth -1, -player)
            """

            c'est compliqué!!!!! 
            de base on met un state 0 pour dire que c'est encore à jouer, +1 pour l'humain
            et -1 pour l'ia mais ici on joue avec des 1 et 0 et il faut regarder la dernière pièce
            puis il faut faire en sorte que l'ia comprenne ce qu'elle doit faire

            """
            # state[x][y] = 0
            # score[0],score[1] = x,y
        # print("best" , best)

minimax(board,9,computer)



# print(board)
# set_move(1,1,2,2,player = computer)
# print(board)
# usable_cells(board)
