import random
import sys

n=9
m=3

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

def checkDir(checkPol,x1,y1):
    c=[0,0,0,0]
    direct=0
    summ=0
    b=5
    if x1<n-1:
        if checkPol[x1+1][y1]==0:
            c[0]=1
    if y1<n-1:
        if checkPol[x1][y1+1]==0:
            c[1]=1
    if x1>0:
        if checkPol[x1-1][y1]==0:
            c[2]=1
    if y1>0:
        if checkPol[x1][y1-1]==0:
            c[3]=1
    for i in range(4):
        summ+=c[i]
    if summ==0:
        direct=5
    while direct==0:
        b=random.randrange(4)
        direct=c[b]

    return b
            

def sudokuKiller():
    checkPol=[[(0) for i in range(n)] for j in range(n)]
    m=n*n
    c=0
    x=0
    y=0
    k=-1
    r=0
    while k!=0:

        c+=1
        number=random.randrange(3,6)
        while (number>0):
            if (x<=n-1) and (y<=n-1) and (x>=0) and (y>=0):
                if checkPol[x][y]==0:
                    checkPol[x][y]=c
                    number-=1
                    r=checkDir(checkPol,x,y)

                    if r==5:
                        number=0
                    if r==0:
                        x+=1
                    if r==1:
                        y+=1
                    if r==2:
                        x-=1
                    if r==3:
                        y-=1

                else:
                    number=0
            
        k=0

        for i in range(n):
            for j in range(n):
                if checkPol[i][j]==0:
                    k=1
                    x=i
                    y=j
                    break
            if checkPol[i][j]==0:
                break

    return checkPol,c

def mixing(board, seedN):
    random.seed(seedN)
    variants=[transposed, swapRowSmall, swapColSmall, swapRowBig, swapColBig]
    for i in range(n):
        func=random.randrange(len(variants))
        board=variants[func](board)
    return board

def deletion (board):
    deletionB=[[(0) for i in range(n)] for j in range(n)]
    iterat=0
    delCount=int(n*n*0.6)
    
    while iterat < delCount:
        i,j=random.randrange(n), random.randrange(n)
        if deletionB[i][j]==0:
            iterat+=1
            deletionB[i][j]=1
            numDeleted=board[i][j]
            board[i][j]=0
            #if SolvingMethods.isPossible()=0:
                #board[i][j]=numDeleted
                #iterat-=1
    return board
             


def main():
    global seedN
    seedN = random.randrange(sys.maxsize)
    firstBoard=baseBoard()
    board=mixing(firstBoard, seedN)
    return board, seedN
