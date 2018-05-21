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
print'without stategic playing {}'.format(stop-start)
plt.subplot(1,2,1)
plt.hist(x)
plt.xlabel('draw player 1 or player 2')
plt.ylabel(' Number of wins')
plt.title('Without strategic playing')


def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            # use `evaluate(board)`, and store as `winner`.
            random_place(board,player)
            winner=evaluate(board)
            if winner != 0:
                break
    return winner

play_strategic_game()  
a=[]
start=time.time()
for _ in range(1000):
    a.append(play_strategic_game())
stop=time.time()
print'with strategic playing {}'.format(stop-start)
plt.subplot(1,2,2)
plt.hist(a)
plt.xlabel('draw player 1 or player 2')
plt.ylabel(' Number of wins')
plt.title('With strategic playing')

plt.show()
plt.close()
