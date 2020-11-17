from tkinter import *
from solvingMethods import puzzle, puzzleSolving

pole=int(9)
size=50

def print_board(board):
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
    canvas.pack(side=LEFT, padx=50,pady=20)

def click_button():
    btn.place_forget()
    canvas.pack_forget()
    boardSolved=puzzleSolving
    print_board(boardSolved)



window=Tk()
window.title("SUDOKU")
window.geometry("800x550")
board=puzzle
print_board(board)

btn = Button(window, text="Solve",background="#235",foreground="white",font="Arial 16", width=15, command=click_button)
btn.place(x=550,y=50)

btnExit=Button(window,text="Exit",background="#235",foreground="white",font="Arial 16",width=15,command=window.destroy)
btnExit.place(x=550,y=100)

window.mainloop()
