import json
import pprint
import time
from random import *
from sys import maxsize
from math import inf as infinity
import platform
from os import system
from copy import deepcopy
"""
all variables :
    t0 for the time processing
    human for human turn(used in minimax) and comp for the ai
    temp_board is used to deepcopy the actual board without changing it
    board is the board we'll take from the json
    counter for the possibilities
    depth is the depth we want to check in advance = the numbers of moves checked in advance
"""
t0=time.time()
human = -1
computer = +1
temp_board = []
board= [
		[ [1],  [0]],
        [ [0],  [1]]
	]
counter = 0
choosing_depth=5
points = 0



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

def eval(state):
    """
    param: state is the catual board that will be evaluated
    here it's for the leaves
    for the moment 0 is for comp and 1 for human
    """
    points = 0
    for row in state: 
        for col in row:
            # if 0 is the color of computer and 1 for the human
            if len(col) == 0:
                pass
            elif 0<len(col)<5:
                if col[-1]==1:
                    points -= 1
                elif col[-1]==0:
                    points +=1
            elif len(col) == 5:
                if col[-1]==1:
                    points -= 5
                elif col[-1]==0:
                    points +=5
    # for i in range (len(state)):
    #     for j in range(len(state[i])):
    #         if 0<len(state[i][j])<5:
    #             for a in range (j-1,j+2):
    #                 for b in range(i-1,i+2):

    #                     if state[i][j][-1] == 0 and len(state[a][b]==0) :
    #                         if i==a and j ==b:
    #                             pass
    #                         else:
    #                             points +=3 
    # trying to check the cells all around the cell in question
    # if isolated from the other color then points +=3 for computer and -=3 for human
    #  but one main problem, I'm out of range when i and j are =0 and I check bellow or above the len of the col i have a and b inexistant
    # I should put a max and min that a and b shouldn't pass
                
    return points
def choose_depth(state):
    """
    param: state, checking all the movements we can still do
    and setting the max depth in the minimax
    """
    global choosing_depth
    all_movements = 0
    for x in state:
        for y in x:
            if len(y) !=0:
                all_movements+=1
    print(all_movements)
    
    if all_movements <= choosing_depth:
        choosing_depth = all_movements -1
    print(choosing_depth)
    




def minimax(state,depth,player):
    """
    param: state, the board, that changes further when we iterate it in the loop
    param: depth, it's the depth we chose outside the function and will decrease for each iteration we do
        the starting depth is for ex 4, it's the root, and 1 is the leaves. It can't go under 1
    param: player stands for human or computer turn, as it will maximize at comp turn and minimize at human turn
    return : returns the best move of its children
    """
    global temp_board
    global counter
    global points
    
    
    
    if player == computer:
        best = {"from":list,"to":list,"tscore":-infinity}        # - inf because we want the algo to maximize for the computer
    else :
        best = {"from":list,"to":list,"tscore":+infinity}

    if depth == 0 or game_over(state):          #when we're at the level under the leaves, leaves depth = 1
        return best
    
    

    for move in possible_moves(state):      #the loop that iterates itself when going inside it's children
        x= move["from"][0]
        y = move["from"][1]
        a = move["to"][0]
        b = move["to"][1]
        
        temp_board = deepcopy(state)    #deepcopying a new board with a first move
        new_state = (temp_board)        #and using this copy of board to re iterate itself and making a new board for each child
        set_move(x,y,a,b,new_state) 
        
        
        
        if depth == 1: # if leaf
            counter +=1
            move["tscore"] = eval(new_state) #it calls the evaluate to put score on the leaves

        else:       #we iterate the function minimax by taking the best score the children returned
            move["tscore"] = minimax(new_state,depth-1,-player)["tscore"] # = the best score from children
            
        
        # compare score with adjacent nodes
        if player == computer:
            if best["tscore"]< move["tscore"]:
                best = move     #max value
        else :
            if best["tscore"]> move["tscore"]:
                best = move     #min value

        
        # if depth!=1:    #just printing to see all the moves
        #     print("MOVE",depth," : ",move)
        # if depth ==1:
        #     print("move",depth," : ",move)
        # print("state",depth," : ",new_state)
        
           
    print("best",depth, ":", best)
    return best #returns only the best score of the children




choose_depth(board)
best_move = minimax(board,choosing_depth,computer)
print("best move to do :", best_move)
print("time processing the possibilities :",time.time()-t0,"seconds")
print("possibilities calculated :",counter)
# # print(board)
# set_move(1,1,2,2,player = computer)
# # print(board)
# # usable_cells(board)
# possible_moves(board)




