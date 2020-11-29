import random

n=9
m=3
num=362880

def baseBoard():
    board=[[(0) for i in range(n)] for j in range(n)]
    for i in range (n):
        for j in range (n):
            board[i][j]=int((i*m +i//m + j) % n + 1)
            

    return board
        
def transposed(board):
    board=[list(i) for i in zip(*board)]
    return board

def swapRowSmall(board):
    zone=random.randrange(m)
    rowFir=random.randrange(m)
    rowSec=random.randrange(m)

    while rowFir==rowSec:
        rowSec=random.randrange(m)
        
    lineFir=int(zone*m+rowFir)
    lineSec=int(zone*m+rowSec)

    board[lineFir],board[lineSec]=board[lineSec],board[lineFir]
    return board

def swapColSmall(board):
    board=transposed(board)
    board=swapRowSmall(board)
    board=transposed(board)
    return board


def swapRowBig(board):
    zone=random.randrange(m)
    rowFir=random.randrange(m)
    rowSec=random.randrange(m)

    while rowFir==rowSec:
        rowSec=random.randrange(m)
        
    for i in range (m):
        x1=int(rowFir*m+i)
        x2=int(rowSec*m+i)
        board[x1],board[x2]=board[x2],board[x1]

    return board

def swapColBig(board):
    board=transposed(board)
    board=swapRowBig(board)
    board=transposed(board)
    return board

def mixing(board, seedN):
    random.seed(seedN)
    variants=[transposed, swapRowSmall, swapColSmall, swapRowBig, swapColBig]
    for i in range(n):
        func=random.randrange(len(variants))
        board=variants[func](board)
    return board

def deletion (board, difficult):
    deletionB=[[(0) for i in range(n)] for j in range(n)]
    iterat=0
    if difficult==1:
        delCount=int(n*n*0.6)
    elif difficult==2:
        delCount=int(n*n*0.65)
    elif difficult==3:
        delCount=int(n*n*0.7)
    
    while iterat < delCount:
        i,j=random.randrange(n), random.randrange(n)
        if deletionB[i][j]==0:
            iterat+=1
            deletionB[i][j]=1
            numDeleted=board[i][j]
            board[i][j]=0
    return board
             


def main():
    global seedN
    seedN=random.randrange(num)
    firstBoard=baseBoard()
    board=mixing(firstBoard, seedN)
    return board, seedN
