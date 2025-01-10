from board import Board
from player import Player
from chesspieces import *

from tkinter import *

def reload_board():
    print("Reloading...")
    

    for i in range(8):
        for j in range(8):
##            print(i,j)
            if main_board.board_spaces[i][j] != "empty":
                butt_label = main_board.board_spaces[i][j].name+" "+main_board.board_spaces[i][j].color
                buttons = Button(root,text=butt_label).grid(row=i,column=j)
            else:
                buttons = Button(root,text="_"*len(butt_label)).grid(row=i,column=j)

    
    print("Reloaded!")

player1 = Player("white")
player2 = Player("black")
print(player1.pieces)

main_board = Board(player1,player2)

root = Tk()



reload_board()
print(main_board)

main_board.Get_Space("A2").move_piece("A3")


print(main_board)
reload_board()

root.mainloop()
