from jogos import*

EstadoBT_27 = namedtuple('State', 'to_move, utility, board, moves')

class JogoBT_27(Game):
    to_move = 1
    utility = 0 #????
    size = 8
    board = {"a1" : 'W', "b1" : 'W', "c1" : 'W', "d1" : 'W', "e1" : 'W', "f1" : 'W', "g1" : 'W', "h1" : 'W',
                "a2" : 'W', "b2" : 'W', "c2" : 'W', "d2" : 'W', "e2" : 'W', "f2" : 'W', "g2" : 'W', "h2" : 'W',
                "a7" : 'B', "b7" : 'B', "c7" : 'B', "d7" : 'B', "e7" : 'B', "f7" : 'B', "g7" : 'B', "h7" : 'B',
                "a8" : 'B', "b8" : 'B', "c8" : 'B', "d8" : 'B', "e8" : 'B', "f8" : 'B', "g8" : 'B', "h8" : 'B'}
    moves = ['a2-a3', 'a2-b3', 'b2-a3', 'b2-b3', 'b2-c3', 'c2-b3', 'c2-c3', 'c2-d3',
                'd2-c3', 'd2-d3', 'd2-e3', 'e2-d3', 'e2-e3', 'e2-f3', 'f2-e3', 'f2-f3',
                'f2-g3', 'g2-f3', 'g2-g3', 'g2-h3', 'h2-g3','h2-h3']
    initial = EstadoBT_27(to_move, utility, board, moves)


    def _init(self, size = 8):
        self.size = size
        self.to_move = initial[0]
        self.initial = EstadoBT_27(to_move, utility, board, moves)

    def actions(self, state):
        player = self.to_move(state)
        actions = list()

        for pos in state.board.keys():
            if state.board.get(pos) == player:
                #Position occupied by piece Player
                col = ord(pos[0])
                row = int(pos[1]) + 1
                col_limit = 97+8
                    
                #Move forward
                if row <= 8:
                    #Move fits inside board
                    #Check if there is a player piece there
                    new_pos = chr(col) + str(row)
                    if new_pos not in state.board.keys():
                        actions.append(pos + "-" + new_pos)

                #Move right
                if row <= 8 and col + 1 < col_limit:
                    #Move fits inside board
                    #Check if there is a player piece there
                    new_pos = chr(col+1) + str(row)
                    if new_pos not in state.board.keys():
                        actions.append(pos + "-" + new_pos)

                #Move left
                if row <= 8 and col - 1 >= 97:
                    #Move fits inside board
                    #Check if there is a player piece there
                    new_pos = chr(col-1) + str(row)
                    if new_pos not in state.board.keys():
                        actions.append(pos + "-" + new_pos)
        return sorted(actions)
    
    def result(self, state, move):
        next_to_move = 1 if state.to_move == 0 else 0
        next_board = dict()
        move = move.split("-")
        pos_from = move[0]
        pos_to = move[1]
        state.board[pos_to] = state.board.get(pos_from)   
        del state.board[pos_from] 
  
        result = EstadoBT_27(next_to_move, state.utility, state.board, state.moves)
        return result
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        if self.terminal_test(state) == True:
            return -1 if player == self.to_move(state) else 1
        return 0 

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
        print("-----------------")
        counter = 8
        result = ""
        for i in range(counter,0, -1):
            result = ""
            result+=str(i)
            result+="|"
            for c in (chr(i) for i in range(97, 97+counter)):   
                piece = self.board.get(c+str(i))
                if type(piece) != str:
                    result+=". "
                else:
                    result+=self.board.get(c+str(i))
                    result+=" "
            
            print(result)
        print("-+---------------")
        print(" |a b c d e f g h")
        if not self.terminal_test(state):
            print("--NEXT PLAYER:", self.to_move(state))    
    
       
            
bt = JogoBT_27()
bt.display(bt.initial)

print(bt.actions(bt.initial))
