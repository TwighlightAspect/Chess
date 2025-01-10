let2num = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
num2let = ["A","B","C","D","E","F","G","H"]

class ChessPiece:
    
    def __init__(self,position,color):
        self.position = position #i.e E4, D3,B2
        self.name = "abstract piece"
        self.color = color
        self.board = "unknown"
        if self.color == "white":
            self.enemy = "black"
            self.forward = -1
        else:
            self.enemy = "white"
            self.forward = 1
    
    def move_piece(self, new_pos):
        if new_pos in self.possiblepos():
            old_pos = str(self.position)
            self.position = new_pos
            self.board.update_position(self,old_pos)
            print("moved")
        else:
            print("i cant move it move it anymore")
            print(self.possiblepos())
    
    def move_forward(self,spaces,can_attack = True):
        row1 = int(self.position[-1])
        col2 = let2num[self.position[0]]  
        check_pos = self.board.Get_Space(num2let[col2]+str(row1+self.forward))
        if check_pos == "empty":
            self.position = check_pos
        elif check_pos.color == self.enemy and can_attack:
            self.position = check_pos
            
    
    def left_diag(self,spaces,can_attack = True):
        row1 = int(self.position[-1])
        col2 = let2num[self.position[0]]
        if col2 != 0: 
            check_pos = self.board.Get_Space(num2let[col2]+str(row1+self.forward))
            if check_pos == "empty":
                self.position = num2let[col2]+str(row1+self.forward)
            elif check_pos.color == self.enemy and can_attack:
                self.position = check_pos.position
        
    def possiblepos(self):
        return list()
    
    def __repr__(self):
        # return "I am a "+self.name+" at postion "+self.position
        return self.name+" "+self.color+" "+self.position
    def __str__(self):
        return self.name

class Pawn(ChessPiece):
    def __init__(self,position,color):
        super().__init__(position,color)
        self.name = "Pawn"
        self.candouble = True #can move twice for first move of pawn

    
        
    def possiblepos(self): #possible positions to move pawn to
        row1 = int(self.position[-1])
        col2 = let2num[self.position[0]]        
        positions = []
        
        # print(type(num2let[col2]))
        
        #normal move
        check_pos = self.board.Get_Space(num2let[col2]+str(row1+self.forward))
        # print("pos",check_pos)
        if check_pos == "empty":
            positions.append(num2let[col2]+str(row1+self.forward))
        
        #double move
        check_pos = self.board.Get_Space(num2let[col2]+str(row1+self.forward))
        if check_pos == "empty" and self.candouble:
            positions.append(num2let[col2]+str(row1+self.forward))
        
        #attacks
        check_pos = self.board.Get_Space(num2let[col2+1]+str(row1+self.forward))
        if check_pos != "empty":
            if check_pos.color == self.enemy:
                positions.append(num2let[col2+1]+str(row1+self.forward))
                
        check_pos = self.board.Get_Space(num2let[col2-1]+str(row1+self.forward))
        if check_pos != "empty":
            if check_pos.color == self.enemy:
                positions.append(num2let[col2-1]+str(row1+self.forward))
        return positions
        
        
        
        
        
        
        
class Rook(ChessPiece):
    def __init__(self, position,color):
        super().__init__(position,color)
        self.name = "Rook"

class Knight(ChessPiece):
    def __init__(self, position,color):
        super().__init__(position,color)
        self.name = "Knight"

class Bishop(ChessPiece):
    def __init__(self, position,color):
        super().__init__(position,color)
        self.name = "Bishop"

class Queen(ChessPiece):
    def __init__(self, position,color):
        super().__init__(position,color)
        self.name = "Queen"

class King(ChessPiece):
    def __init__(self, position,color):
        super().__init__(position,color)
        self.name = "King"

