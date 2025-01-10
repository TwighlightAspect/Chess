#board is 8x8
import chesspieces as piece

class Player:
    def __init__(self,piece_color): #color if black or white
        self.pieces = self.MakePieces(piece_color)
        self.color = piece_color
        
    def MakePieces(self,color): #row 1 is pawns and row 2 is other pieces
        if color == "white":
            row1= "7"
            row2 = "8"
        else:
            row1 = "2"
            row2 = "1"
        piece_list = list()
        
        #pawns
        for i in range(8):
            piece_list.append(piece.Pawn(piece.num2let[i]+row1,color))
        
        #rooks   
        piece_list.append(piece.Rook("A"+row2,color))
        piece_list.append(piece.Rook("H"+row2,color))
        
        #knights
        piece_list.append(piece.Knight("B"+row2,color))
        piece_list.append(piece.Knight("G"+row2,color))
        
        #bishops
        piece_list.append(piece.Bishop("C"+row2,color))
        piece_list.append(piece.Bishop("F"+row2,color))
        
        #queen
        piece_list.append(piece.Queen("E"+row2,color))
        
        #king
        piece_list.append(piece.King("D"+row2,color))
        
        return piece_list
    
    def Upgrade_pawn(self,pawn,upgrade):
        """Precondition: upgrade is either rook,bishop,knight, or queen"""
        upgraded = True
        if upgrade == "rook":
            obj = piece.Rook(pawn.position,pawn.color)
        elif upgrade == "bishop":
            obj = piece.Bishop(pawn.position,pawn.color)
        elif upgrade == "knight":
            obj = piece.Knight(pawn.position,pawn.color)
        elif upgrade == "queen":
            obj = piece.Queen(pawn.position,pawn.color)
        else:
            upgraded = False
            
        if upgraded:
            self.pieces.remove(pawn)
            self.pieces.append(obj)
            del pawn

    def __repr__(self):
        return self.pieces

