import random
import sys
import copy
import solvingMethods

n=9
m=3
difClassic={1:44,2:49,3:45,4:53,5:51,6:55}
difKiller={1:45,2:53,3:51,4:64,5:64,6:81}


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

def blocksSum(board, checkPol, maxN):
    dict={}
    for i in range(1,maxN+1):
        sum=0
        x1=y1=0
        for x in range(n):
            for y in range(n):
                if checkPol[x][y]==i:
                    sum+=board[x][y]
        dict[i]=sum
    return dict

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
            

def sudokuKiller(board):
    checkPol=[[(0) for i in range(n)] for j in range(n)]
    c=x=y=r=0
    k=-1
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
                    x,y=i,j
                    break
            if checkPol[i][j]==0:
                break

    dict=blocksSum(board, checkPol, c)

    return checkPol,c, dict


def mixing(board, seedN):
    random.seed(seedN)
    variants=[transposed, swapRowSmall, swapColSmall, swapRowBig, swapColBig]
    for i in range(n):
        func=random.randrange(len(variants))
        board=variants[func](board)
    return board

def Easy(board):
    flag=0
    if solvingMethods.SolvingMethod(board).SingleCandControl==0:
        if solvingMethods.SolvingMethod(board).NakedPairsControl==0:
           if solvingMethods.SolvingMethod(board).NakedThreeControl==0:
               if solvingMethods.SolvingMethod(board).HidPairControl==0:
                   if solvingMethods.SolvingMethod(board).HidTreeControl==0:
                       if (solvingMethods.SolvingMethod(board).DeleteExtraVal>=3) and (solvingMethods.SolvingMethod(board).DeleteExtraVal<=5):
                           flag=1
    return flag

def Medium(board):
    flag=0
    if solvingMethods.SolvingMethod(board).SingleCandControl<=1:
        if solvingMethods.SolvingMethod(board).NakedPairsControl==0:
           if solvingMethods.SolvingMethod(board).NakedThreeControl==0:
               if solvingMethods.SolvingMethod(board).HidPairControl==0:
                   if solvingMethods.SolvingMethod(board).HidTreeControl==0:
                       if (solvingMethods.SolvingMethod(board).DeleteExtraVal>=3) and (solvingMethods.SolvingMethod(board).DeleteExtraVal<=10):
                           flag=1
    return flag

def Hard(board):
    flag=0
    if solvingMethods.SolvingMethod(board).SingleCandControl<=4:
        if solvingMethods.SolvingMethod(board).NakedPairsControl<=2:
           if solvingMethods.SolvingMethod(board).NakedThreeControl<=1:
               if solvingMethods.SolvingMethod(board).HidPairControl<=1:
                   if solvingMethods.SolvingMethod(board).HidTreeControl<=1:
                       if (solvingMethods.SolvingMethod(board).DeleteExtraVal>=3) and (solvingMethods.SolvingMethod(board).DeleteExtraVal<=10):
                           flag=1
    return flag

def deletion (board, dif,typeG):
    deletionB=[[(0) for i in range(n)] for j in range(n)]
    iterat=0
    c=0
    if typeG==1:
        delCount=difClassic[dif*2-1]+random.randrange(difClassic[dif*2]-difClassic[dif*2-1]+1)
    elif typeG==2:
        delCount=difKiller[dif*2-1]+random.randrange(difClassic[dif*2]-difClassic[dif*2-1]+1)
    meth=1
    while iterat < delCount:
        i,j=random.randrange(n), random.randrange(n)
        if deletionB[i][j]==0:
            iterat+=1
            deletionB[i][j]=1
            c+=1
            numDeleted=board[i][j]
            board[i][j]=0
            if solvingMethods.SolvingMethods(board).isPossible()==0:
                board[i][j]=numDeleted
                iterat-=1
            if (typeG==1) and (iterat>difClassic[dif*2-1]):
                if dif==1:
                    meth=Easy(board)
                elif dif==2:
                    meth=Medium(board)
                elif dif==3:
                    meth=Hard(board)
            if (typeG==2) and (iterat>difKiller[dif*2-1]):
                if dif==1:
                    meth=Easy(board)
                elif dif==2:
                    meth=Easy(board)
                elif dif==3:
                    meth=Easy(board)
            if meth==0:
                break
            copyBoard=copy.deepcopy(board)
        if c==n*n:
            break
    return copyBoard
             


def main():
    global seedN
    seedN = random.randrange(sys.maxsize)
    firstBoard=baseBoard()
    board=mixing(firstBoard, seedN)
    return board, seedN
