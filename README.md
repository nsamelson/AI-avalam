# AI Project AVALAM

Samelson Nicolas - 17288  
Roquero Pedro - 17010

## Programming language used :

Python 3.7.5

## Libraries used :

* cherrypy
* json
* socket
* sys
* math 
* os
* msgpack
* random 
* pprint
* time
* webbrowser

## AI strategy:

Before playing, the AI will choose a depth of moves ahead of the current game (depth) 
depending on the advancement of the game. Starting by a depth of 3, going up to 5 (in the middle of the game)
and then when there isn't a lot of possibilities, it will decrease.

After choosing it's depth it will choose the best move to do for the AI to mark the best score.
For it to happen, we used minimax and alpha beta prunning:

- If we consider the algorithm as a tree and the root is the shallowest depth and the leaves are the deepest depth.
At each depth (except the leaves), it will check the state of the board and
calculate a score. For each pawn tower, it will add an amount of points :  
  -  If the height is between 1 and 4 then the score will be of 1 point ;
  -  If the height is 5, then it will be of 5 points;
  -  Depending on the top pawn of the tower, the score will be positive for the colour of the AI and negative if it's the colour of the ennemy;  
   

- At the leaves, or the deepest depth, it will quickly calculate the difference between its parent and itself,the child. It only evaluates the pawn that moved between the parent and the child.

- With the score of each possible move on the leaves, the algorythm Minimax will run and 
maximize the AI and minimize the player. 

- Alpha Beta is implemented to prune some leaves and 
optimize a lot the process.

## How to run:

1. Firstly first, run the file server.py, a webpage should open.

1. Then, in the terminal (cmd), go to the directory "ai" with the command `cd ai`.

1. Run the file avalam5.0.py with the command `python Avalam5.0.py 8080`(the port 8080 is an example), a webpage should open with "pong" in return.
