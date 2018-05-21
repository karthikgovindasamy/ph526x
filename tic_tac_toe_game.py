import numpy as np
import time
import matplotlib.pyplot as plt
import random
def create_board():
    return np.zeros([3,3],dtype='int')

def place(board,player,position):
    if(board[position[0]][position[1]]==0):
        board[position[0]][position[1]]=player
    return board    

def possibilities(board):
    x=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==0:
                x.append((i,j))
    return x

def random_place(board,player):
    selection=possibilities(board)
    y=random.choice(selection)
    board=place(board,player,y)
    return board

def row_win(board,player):
    for i in range(3):
        if([board[i][x] for x in range(3)]==([player]*3)):
            return True
    else:
        return False

def col_win(board,player):
    for i in range(3):
        if([board[x][i] for x in range(3)]==([player]*3)):
            return True
    else:
        return False

def diag_win(board,player):
    if([board[i][i] for i in range(3)]==([player]*3)):
            return True
    else:
        return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
    	if(row_win(board,player)or col_win(board,player) or diag_win(board,player)):
            winner=player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board=create_board()
    while evaluate(board)==0:
        random_place(board,1)
        if evaluate(board)==0:
            random_place(board,2)
    return evaluate(board)

x=[]
start=time.time()
for _ in range(1000):
    x.append(play_game())
stop=time.time()
print(stop-start)
plt.hist(x)
plt.show()