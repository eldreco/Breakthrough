##############################
####---------APAGAR--------###
from types import NoneType
from jogos import *
class JogoBT_27(Game):
    
    to_move = 1
    utility = 0 #????

    board = {"a1" : 'W', "b1" : 'W', "c1" : 'W', "d1" : 'W', "e1" : 'W', "f1" : 'W', "g1" : 'W', "h1" : 'W',
                "a2" : 'W', "b2" : 'W', "c2" : 'W', "d2" : 'W', "e2" : 'W', "f2" : 'W', "g2" : 'W', "h2" : 'W',
                "a7" : 'B', "b7" : 'B', "c7" : 'B', "d7" : 'B', "e7" : 'B', "f7" : 'B', "g7" : 'B', "h7" : 'B',
                "a8" : 'B', "b8" : 'B', "c8" : 'B', "d8" : 'B', "e8" : 'B', "f8" : 'B', "g8" : 'B', "h8" : 'B',};
    moves = ['a2-a3', 'a2-b3', 'b2-a3', 'b2-b3', 'b2-c3', 'c2-b3', 'c2-c3', 'c2-d3',
                'd2-c3', 'd2-d3', 'd2-e3', 'e2-d3', 'e2-e3', 'e2-f3', 'f2-e3', 'f2-f3',
                'f2-g3', 'g2-f3', 'g2-g3', 'g2-h3', 'h2-g3','h2-h3']
    initial = GameState(to_move, utility, board, moves)

    def _init(self, size = 8, initial = initial):
        self.size = size
        self.to_move = initial[0]
        self.initial = initial

    def actions(self, state):
        return
    
    def result(self, state, move):
        return
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        return 

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        for x in state.board:
            if "8" in x and state.board.get(x) == "W":
                return True
            elif "1" in x and state.board.get(x) == "B":
                return True
        return False
        

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        return "W" if state[0] == 1 else "B"
    
    def display(self, state):
        print("------------------")
        counter = 8
        result = ""
        for i in range(counter,0, -1):
            result = ""
            result+=str(i)
            result+="|"
            for c in (chr(i) for i in range(97, 97+counter)):   
                piece = self.board.get(c+str(i))
                if type(piece) == NoneType:
                    result+=". "
                else:
                    result+=self.board.get(c+str(i))
                    result+=" "
            
            print(result)
        print("------------------")
        print("|a b c d e f g h")
        print("--NEXT PLAYER: ", self.to_move(state))

       
            
bt = JogoBT_27()
bt.display(bt.initial)
print(bt.terminal_test(bt.initial))