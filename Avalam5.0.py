import socket
import sys
import json
import time
import cherrypy
import webbrowser
from random import *
from sys import maxsize
from math import inf as infinity
from os import system
import msgpack
import pprint
"""
all variables :
    t0 : for the time processing
    human : it's pawns are 1
    computer : pawns are 0
    temp_board : used to copy the actual board without changing it
    board : the board we'll take from the body
    counter : counts the possibilities
    choosing_depth : the depth we want to check in advance = the numbers of moves checked in advance
    FORMAT : format to encode messages and sending with socket module
    Server : the address (localhost when local) will change with 127.0.0.1
    PORT : ports in link with the address (8080 for sending ping and 3001 for the gamerunner)
    Header : max size of the text (must be a tuple of 2)
"""
HEADER = 4096
PORT = 3001
FORMAT = 'utf-8'
SERVER = "localhost"
ADDR = (SERVER, PORT)
human = -1
computer = +1
name = "Jack Uzi"
board = []
counter = 0
choosing_depth=4
points = 0
randomtext = ["C'est moi le plus fort dans ma forme","J'vais au casino en claquettes","02 880","C'est Jack, Jack Uzi",
            "Tu vas moins faire le malin","T'es dans ta jalousie","Nous on joue pas de la flute","Les oreilles ont des murs",
            "Ici c'est nous les meilleurs","Au jour d'aujourd'hui","Ils voyent bien qu'on va tout péter",
            "Persone ne gagne ici","Moi j'ai peur de personne","J'me lève à 14h du matin","On fait du vélo sans les mains",
            "Maintenant tu fais moins le malin", "Nous on fait pas de calin","Pan Pan!","Y'en a qu'ont le mental et y'en a qu'on que l'emmental",
            "Jack septe pas le pardon","Jack septe les chèques","Jack célère"]


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def game_over(state):
    """
    cheking if the game is over
    State: board
    """
    if len(all_moves(state))== 0:
        return True
    else:
        return False

def eval_cell(cell):
    """
    evaluates the new cell that received the pawns from another cell 
    return : 0 if nothing, 1 or -1 if not a full tower and 5 or -5 if full tower
    """
    if not cell: return 0
    x = 1 if len(cell) < 5 else 5
    return x if not cell[-1] else -x
    
def diff(x, y, a, b, state):
    """
    Calculate the difference in points caused by set_move
    """
    return eval_cell(state[a][b] + state[x][y]) - eval_cell(state[x][y])  - eval_cell(state[a][b])

    
def all_moves(state):
    """
    param: state, it takes the actual board and will check all possible moves
    return : case, returns a list of dicts with all the possible moves
    """
    case = []
    cells = set()
    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if 0 < len(cell) < 5:
                cells.add((x, y))
    for x,y in cells:
        for a,b in cells:   
            if x-1 <= a <= x+1 and y-1 <= b <= y+1:
                if a == x and b == y:
                    pass
                else :
                    if len(state[a][b]) <= 5- len(state[x][y]):
                        case.append({"from":(x,y), "to":(a,b),"tscore": int})
    return case

def set_move(x,y,a,b,state):
    """
    set the move on board if coordinates are valid
    param : player is the current playing (not sure if needed)
    parm x and y : row and col from
    param a and b : row and col to
    """
    state[a][b].extend(state[x][y])
    state[x][y].clear()


def eval(state):
    """
    param: state is the actual board that will be evaluated
    here it's for the leaves
    0 is for comp and 1 for human
    return : points is the score for each board corresponding to the leaves
    """
    points = 0
    for row in state: 
        for col in row:
            length = len(col)

            if length == 0:
                pass
            else :
                count0= col.count(0)
                count1 = col.count(1)
                if 0<length<5:
                    if col[-1]==1:
                        points -= 1
                    elif col[-1]==0:
                        points += 1
                elif length == 5:
                    if col[-1]==1:
                        points -= 5
                    
                    elif col[-1]==0:
                        points +=5 
    return points
def choose_depth(state):
    """
    param: state = board, checking all the remaining cells that can be used
    and setting the max depth in the minimax
    """
    global choosing_depth
    pile_count = 0
    for x in state:
        for y in x:
            if len(y) ==1:
                pile_count +=1
    if pile_count >= 14:
        choosing_depth = 3
    elif 10<= pile_count<14:
        choosing_depth = 4
    elif 8<= pile_count<10:
        choosing_depth = 5
    elif 6<= pile_count<8:
        choosing_depth = 3
    elif pile_count <=4:
        choosing_depth = 1
    else:
        choosing_depth =2
def minimax(state,depth,alpha,beta,player):
    """
    param: state, the board, that changes further when we iterate it in the loop
    param: depth, it's the depth we chose outside the function and will decrease for each iteration we do
        the starting depth is for ex 4, it's the root, and 1 is the leaves. It can't go under 1
    param: alpha and beta for pruning useless branches and optimizing
    param: player stands for human or computer turn, as it will maximize at comp turn and minimize at human turn
    return : returns the best move of its children
    """
    
    temp_board = msgpack.packb(state)
    base_eval = eval(state)     #basic evaluation of the board

    if player == computer:
        best = {"from":list,"to":list,"tscore":-infinity}        # - inf because we want the algo to maximize for the computer
    else :
        best = {"from":list,"to":list,"tscore":+infinity}

    if depth == 0 or game_over(state):          #when we're at the level under the leaves, leaves depth = 1
        return best

    for move in all_moves(state):      #the loop that iterates itself when going inside it's children
        x, y = move["from"]
        a,b = move["to"]
        
        new_state = msgpack.unpackb(temp_board)
        set_move(x,y,a,b,new_state)     #creating a copy and setting a new move in the copy
        
        if depth == 1: # if leaf
            move["tscore"] = base_eval + diff(x, y, a, b, new_state)    #checks the base evaluation from parent and adding the difference with the child

        else:       #we iterate the function minimax by taking the best score the children returned
            move["tscore"] = minimax(new_state,depth-1,alpha,beta,-player)["tscore"] # = the best score from children
                
        
        # compare score with adjacent nodes
        if player == computer:  #maximize
            
            if best["tscore"]< move["tscore"]:
                best = move     #max value
            alpha = max(alpha,best["tscore"])
        else :
            if best["tscore"]> move["tscore"]:
                best = move     #min value
            beta = min(beta,best["tscore"])
            
        if beta <= alpha:
            break
        
    return best #returns only the best score of the children

def send ():
    """
    Opening the json : matricules.json and sending it 
    to the server
    """
    with open("matricules.json") as file:
        msg = json.loads(file.read())
    
    msg.update(port = port) #change the port when launching the file
    msg = json.dumps(msg)       #transforing the dict into a string
    message = msg.encode(FORMAT)    #encoding in utf8
    msg_length = len(message)   
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(message)    #sending
    
    
class Server:
    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @cherrypy.expose
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        body = cherrypy.request.json

        board = body["game"]
        player1 = body["you"]
        
        t0=time.time()

        choose_depth(board) #choose the depth
        print(choosing_depth)
        if player1 == name:  #playing with 0 as it's pawns
            best_move = minimax(board,choosing_depth,-infinity,infinity,computer)
        else:
            best_move = minimax(board,choosing_depth,-infinity,infinity,human)

        x,y = best_move["from"]
        a,b = best_move["to"]
        print("time processing the possibilities :",time.time()-t0,"seconds")
        
        return {
                "move": {
                    "from": [x, y],
                    "to": [a, b]
                },
                "message": choice(randomtext)
            }

    @cherrypy.expose
    def ping(self):
        send()
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080
    site = f"http://localhost:{port}/ping"

    webbrowser.open(site)
    print('browser started !')

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())