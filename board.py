import numpy
from chesspieces import let2num
class Board:
    def __init__(self,player1,player2):
        """(Board,Player,Player) -> None"""
        
        if player1.color == "white":
            self.white = player1
            self.black = player2
        else:
            self.white = player2
            self.black = player1
        
        self.board_spaces = list()
        temp = list()
        for i in range(8):
            temp.append("empty")
        for i in range(8):
            self.board_spaces.append(list(temp))
        
        self.initialize_pieces(player1)
        self.initialize_pieces(player2)

    def initialize_pieces(self,player):
        for i in player.pieces:
            i.board = self
            self.update_position(i,exsits=False)
            if i.position[0] != "H":
                self.board_spaces[int(i.position[-1])-1].pop(int(let2num[i.position[0]]+1))
            else:
                self.board_spaces[int(i.position[-1])-1].pop(-1) 
            
    def update_position(self,piece,old_postion=None,exsits=True):
        self.board_spaces[int(piece.position[-1])-1].insert(int(let2num[piece.position[0]]),piece)
        if exsits:
            self.board_spaces[int(old_postion[-1])-1].insert(int(let2num[old_postion[0]])+1,"empty")
            self.board_spaces[int(old_postion[-1])-1].pop(int(let2num[old_postion[0]])+1)
    
    def Get_Space(self,space):
        try:
            return self.board_spaces[int(space[-1])-1][let2num[space[0]]]
        except:
            return None
       
    
    def __repr__(self):
        new_str = ""
        for i in self.board_spaces:
            new_str+=str(i)+"\n"
        
        return new_str
            
