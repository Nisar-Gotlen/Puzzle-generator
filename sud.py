import random
from tkinter import *
from tkinter import messagebox
from solvingMethods import puzzle, puzzleSolving
import generation

pole=int(9)
size=50

def printBoard(board):
    global canvas
    x=5
    canvas = Canvas(window, width=pole*size+x*2-3,height=pole*size+x*2-3,bg="white")
    for row in range(pole):
        for col in range(pole):
            x1, y1 = row * size+x, col * size+x
            x2, y2 = (row+1) * size+x, (col+1) * size+x
            canvas.create_rectangle((x1, y1), (x2, y2),outline="black")
            if (board[col][row]==0):
                num=" "
            else:
                num=str(board[col][row])
            canvas.create_text(x1+size/2, y1+size/2, font="Arial 14",text=num)
            if (col % 3==0):
                canvas.create_line(x1,y1,x2,y1,width=3)
            if (row % 3==0):
                canvas.create_line(x1,y1,x1,y2,width=3)
            if (col==8):
                canvas.create_line(x2,y2,x1,y2,width=3)
            if (row==8):
                canvas.create_line(x2,y2,x2,y1,width=3)
    canvas.place(x=50,y=50)

def clickBtn():
    btn.place_forget()
    canvas.pack_forget()
    boardSolved=puzzleSolving
    printBoard(boardSolved)

def changingSeed(seed):
    mesEntry.delete("0", "end")
    seedText.config(text=seed)

def seedBtn():
    global seedMes
    seedMes=message.get()
    if seedMes.isdigit():
        if int(seedMes)<generation.num:
            canvas.pack_forget()
            random.seed(seedMes)
            firstBoard=generation.baseBoard()
            board=generation.mixing(firstBoard, int(seedMes))
            printBoard(board)
            changingSeed(seedMes)
        else:
             messagebox.showinfo("Error","Seed in the wrong range")
    else:
        messagebox.showinfo("Error", "Wrong seed")

def generate(dif):
    firstBoard,genSeed=generation.main()
    board=generation.deletion(firstBoard,dif)
    printBoard(board)
    changingSeed(genSeed)

def Easy():
    generate(1)

def Middle():
    generate(2)

def Hard():
    generate(3)


window=Tk()
window.title("SUDOKU")
window.geometry("850x650")
board=[[(0) for i in range(pole)] for j in range(pole)]
printBoard(board)

btn = Button(window, text="Solve",background="#235",foreground="white",font="Arial 16", width=15, command=clickBtn)
btn.place(x=550,y=50)

btnExit=Button(window,text="Exit",background="#235",foreground="white",font="Arial 16",width=15,command=window.destroy)
btnExit.place(x=550,y=100)

textLabel=Label(text="Your seed:", foreground="black",font="Arial 20",width=15, justify="center")
textLabel.place(x=525,y=200)

seedText=Label(text=0, foreground="black",font="Arial 20",width=15, justify="center")
seedText.place(x=525,y=250)

message = StringVar()
mesEntry = Entry(textvariable=message, background="white",foreground="black",font="Arial 16",width=16, justify="center", bd="3",)
mesEntry.insert (0, "Enter seed")
mesEntry.place (x=550,y=400)

btnOk=Button(window,text="Enter",background="#235",foreground="white",font="Arial 16",width=15, command=seedBtn)
btnOk.place(x=550,y=450)

btnEasy=Button(window,text="Easy",background="#235",foreground="white",font="Arial 16",width=8, command=Easy)
btnEasy.place(x=50,y=550)

btnMiddle=Button(window,text="Middle",background="#235",foreground="white",font="Arial 16",width=8, command=Middle)
btnMiddle.place(x=210,y=550)

btnMiddle=Button(window,text="Hard",background="#235",foreground="white",font="Arial 16",width=8, command=Hard)
btnMiddle.place(x=370,y=550)

window.mainloop()

