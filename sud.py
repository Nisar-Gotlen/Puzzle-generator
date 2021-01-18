import random
from tkinter import *
from tkinter import messagebox
import copy
import generation
import math

pole=int(9)
size=50
genSeed=0

def createBoard():
    heightfr=widthfr=442
    global frame
    frame = Frame(window,width=widthfr, height=heightfr, highlightbackground="black", highlightcolor="black", highlightthickness=4, bd=0)   
    frame.place(x=20,y=20)
    global canvas
    canvas = Canvas(frame,width=widthfr, height=heightfr)
    canvas.pack()
    global entries
    entries = []
    for i in range(pole):
        if i%3==0:
            canvas.create_line(50*i-3,0,50*i-3,heightfr+1,width=4,fill='grey')
            canvas.create_line(0,50*i-3,widthfr+1,50*i-3,width=4,fill='grey')
        e = []
        for j in range(pole):
            entry = Entry(frame, width=3, font=("Helvetica", 15), relief=RIDGE, justify=CENTER)
            e.append(entry)
            entry.place(x=i*50,y=j*50, height=45, width=45)
        entries.append(e)

def classicSudoku():
    global copyBoard
    global seedMes
    seedMes=message.get()
    if seedMes=='':
        firstBoard,genSeed=generation.main()
        seedText.config(text=genSeed)
    else:
        baseBoard=generation.baseBoard()
        firstBoard=generation.mixing(baseBoard, int(seedMes))
    copyBoard=copy.deepcopy(firstBoard)
    if dif!=0:
        board=generation.deletion(firstBoard, dif, 1)
        for i in range (pole):
            for j in range(pole):
                if board[i][j]!=0:
                    entries[j][i].insert (0, board[i][j])
                    entries[j][i].config(state="readonly")

def searchingForBlocks(x,y,blockBoard):

    if x<pole-1:
        if math.fabs(blockBoard[x][y]-blockBoard[x+1][y])>=1:
            canvas.create_line(50*y,50*(x+1)-3,50*(y+1),50*(x+1)-3,width=4,fill='blue',dash=(10,2))

    if y<pole-1:
        if math.fabs(blockBoard[x][y]-blockBoard[x][y+1])>=1:
            canvas.create_line(50*(y+1)-3,50*x,50*(y+1)-3,50*(x+1),width=4,fill='blue',dash=(10,2))
    

def killerSudoku():
    global copyBoard
    global seedMes
    seedMes=message.get()
    if seedMes=='':
        firstBoard,genSeed=generation.main()
        seedText.config(text=genSeed)
    else:
        baseBoard=generation.baseBoard()
        firstBoard=generation.mixing(baseBoard, int(seedMes))
    copyBoard=copy.deepcopy(firstBoard)
    blockBoard,maxNum, dictN=generation.sudokuKiller(firstBoard)
    if dif!=0:
        board=generation.deletion(firstBoard, dif,2)
        for i in range (pole):
            for j in range(pole):
                if board[i][j]!=0:
                    entries[j][i].insert (0, board[i][j])
                    entries[j][i].config(state="readonly")

    
        for x in range(pole):
            for y in range(pole):
                searchingForBlocks(x,y,blockBoard)

        for i in range(1,maxNum+1):
            x1=y1=0
            for x in range(pole):
                for y in range(pole):
                    if blockBoard[x][y]==i:
                        x1,y1=x,y
                        break
            text=Label(frame, text=dictN[i])
            text.place(x=y1*50,y=x1*50)
        
    

def checkBoard():
    c=0
    items = [[(0) for i in range(pole)] for j in range(pole)]
    for i in range (pole):
        for j in range(pole):
            if (entries[i][j].get().isdigit()) or (entries[i][j].get()==''):
                if entries[i][j].get()=='':
                    items[j][i]=0
                else:
                    items[j][i]=int(entries[i][j].get())
            else:
                items[j][i]=-1
                c=1


    if items==copyBoard:
        messagebox.showinfo("Correct answer","You win")
    elif c==1:
        messagebox.showinfo("Words","You need to write numbers")
    else:
        messagebox.showinfo("Wrong answer","You have mistakes")

def changingSeed(seed):
    mesEntry.delete("0", "end")
    seedText.config(text=seed)

def seedChange():
    global seedMes
    seedMes=message.get()
    if dif!=0:
        if seedMes.isdigit():
            if int(seedMes)>0:
                frame.place_forget()
                createBoard()
                if buttonText=="Classic":
                    classicSudoku()          
                elif buttonText=="Killer Sudoku":
                    killerSudoku()
                changingSeed(seedMes)
            else:
                 messagebox.showinfo("Error","Seed in the wrong range")
        else:
            messagebox.showinfo("Error", "Wrong seed")


def returnToTheMenu():
    frameMenu.pack()
    frameMain.pack_forget()
    frame.place_forget()

def Easy():
    global dif
    dif=1
    if message.get()=='':
        frame.place_forget()
        createBoard()
        if buttonText=="Classic":
            classicSudoku()
        elif buttonText=="Killer Sudoku":
            killerSudoku()
    else:
        seedChange()

def Medium():
    global dif
    dif=2
    if message.get()=='':
        frame.place_forget()
        createBoard()
        if buttonText=="Classic":
            classicSudoku()
        elif buttonText=="Killer Sudoku":
            killerSudoku()
    else:
        seedChange()

def Hard():
    global dif
    dif=3
    if message.get()=='':
        frame.place_forget()
        createBoard()
        if buttonText=="Classic":
            classicSudoku()
        elif buttonText=="Killer Sudoku":
            killerSudoku()
    else:
        seedChange()
                
                
def startGame():
    global frameMain
    frameMain = Frame(window, width=850, height=650)
    board=[[(0) for i in range(pole)] for j in range(pole)]

    btnCheck = Button(frameMain, text="Check",background="#235",foreground="white",font="Arial 16", width=15, command=checkBoard)
    btnCheck.place(x=550,y=20)

    btnReturn = Button(frameMain, text="Return",background="#235",foreground="white",font="Arial 16", width=15, command=returnToTheMenu)
    btnReturn.place(x=20,y=560)

    textLabel=Label(frameMain,text="Your seed:", foreground="black",font="Arial 20",width=15, justify="center")
    textLabel.place(x=525,y=200)

    global seedText
    seedText=Label(frameMain,text=genSeed, foreground="black",font="Arial 16",width=25, justify="center")
    seedText.place(x=500,y=250)

    global message
    message = StringVar()
    global mesEntry
    mesEntry = Entry(frameMain,textvariable=message, background="white",foreground="black",font="Arial 16",width=16, justify="center", bd="3",)
    mesEntry.place (x=550,y=300)


    global dif
    dif=0
    btnEasy=Button(frameMain,text="Easy",background="#235",foreground="white",font="Arial 16",width=8, command=Easy)
    btnEasy.place(x=490,y=385)

    btnMed=Button(frameMain,text="Medium",background="#235",foreground="white",font="Arial 16",width=8, command=Medium)
    btnMed.place(x=600,y=385)

    btnHard=Button(frameMain,text="Hard",background="#235",foreground="white",font="Arial 16",width=8, command=Hard)
    btnHard.place(x=710,y=385)

    createBoard()

    frameMain.pack()


def on_click(event):
    global buttonText
    buttonText = event.widget.cget('text')
    startGame()
    frameMenu.pack_forget()


def main():
    global frameMenu
    frameMenu = Frame(window, width=850, height=650,bg = "white")
    frameMenu.pack()

    textLabel=Label(frameMenu, text="SUDOKU", foreground="black",font="Arial 46", justify="center",bg = "white")
    textLabel.pack(padx=10, pady=70,side="top")

    btnClassic=Button(frameMenu,text="Classic",background="#235",foreground="white",font="Arial 32",width=12)
    btnClassic.bind('<Button-1>', on_click)
    btnClassic.pack(padx=10, pady=10,anchor=CENTER)

    btnKiller=Button(frameMenu,text="Killer Sudoku",background="#235",foreground="white",font="Arial 32",width=12)
    btnKiller.bind('<Button-1>', on_click)
    btnKiller.pack(padx=10, pady=10,anchor=CENTER)


    window.mainloop()

window=Tk()
window.title("SUDOKU")
window.geometry("850x650")
window.config(bg = "white")
main()



