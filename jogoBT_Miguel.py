from jogos import*
from jogadorBT_Miguel import*
from jogar import*

EstadoBT_Miguel = namedtuple('State', 'to_move, utility, board, moves, whites, blacks, col_whites, col_blacks, line_whites, line_blacks')

class JogoBT_Miguel(Game):
    #to_move = 1
    #utility = 0 #????
    #size = 8

    board = {"a1" : 'W', "b1" : 'W', "c1" : 'W', "d1" : 'W', "e1" : 'W', "f1" : 'W', "g1" : 'W', "h1" : 'W',
                "a2" : 'W', "b2" : 'W', "c2" : 'W', "d2" : 'W', "e2" : 'W', "f2" : 'W', "g2" : 'W', "h2" : 'W',
                "a7" : 'B', "b7" : 'B', "c7" : 'B', "d7" : 'B', "e7" : 'B', "f7" : 'B', "g7" : 'B', "h7" : 'B',
                "a8" : 'B', "b8" : 'B', "c8" : 'B', "d8" : 'B', "e8" : 'B', "f8" : 'B', "g8" : 'B', "h8" : 'B'}
    whites = dict()
    blacks = dict()
    col_blacks = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0}
    col_whites = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0}
    line_whites = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0}
    line_blacks = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0}
    for pos in board.keys():
        if board.get(pos) == "W":
            whites[pos] = 'W'
            col_whites[pos[0]] = col_whites[pos[0]] + 1
            line_whites[pos[1]] = line_whites[pos[1]] + 1
        else:
            blacks[pos] = 'B'
            col_blacks[pos[0]] = col_blacks[pos[0]] + 1
            line_blacks[pos[1]] = line_blacks[pos[1]] + 1
    moves = ['a2-a3', 'a2-b3', 'b2-a3', 'b2-b3', 'b2-c3', 'c2-b3', 'c2-c3', 'c2-d3',
                'd2-c3', 'd2-d3', 'd2-e3', 'e2-d3', 'e2-e3', 'e2-f3', 'f2-e3', 'f2-f3',
                'f2-g3', 'g2-f3', 'g2-g3', 'g2-h3', 'h2-g3','h2-h3']
    initial = EstadoBT_Miguel(1, 0, board, moves, whites, blacks, col_whites, col_blacks, line_whites, line_blacks)

    def _init(self, size = 8):
        self.size = size
        self.initial = initial
        for pos in initial.board.keys():
            if initial.board.get(pos) == "W":
                whites.add(pos)
                col_whites[pos[0]] = col_whites[pos[0]] + 1
                line_whites[pos[1]] = line_whites[pos[1]] + 1
            else:
                blacks.add(pos)
                col_blacks[pos[0]] = col_blacks[pos[0]] + 1
                line_blacks[pos[1]] = line_blacks[pos[1]] + 1

    def actions(self, state):
        player = "W" if self.to_move(state) == 1 else "B"
        actions = list()

        for pos in state.board.keys():
            if player == "W":
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
                        if state.board.get(new_pos) != player:
                            actions.append(pos + "-" + new_pos)

                    #Move left
                    if row <= 8 and col - 1 >= 97:
                        #Move fits inside board
                        #Check if there is a player piece there
                        new_pos = chr(col-1) + str(row)
                        if state.board.get(new_pos) != player:
                            actions.append(pos + "-" + new_pos)

            elif player == "B":
                if state.board.get(pos) == player:
                    #Position occupied by piece Player
                    col = ord(pos[0])
                    row = int(pos[1]) - 1
                    col_limit = 97+8
                        
                    #Move forward
                    if row > 0:
                        #Move fits inside board
                        #Check if there is a player piece there
                        new_pos = chr(col) + str(row)
                        if new_pos not in state.board.keys():
                            actions.append(pos + "-" + new_pos)

                    #Move right
                    if row > 0 and col + 1 < col_limit:
                        #Move fits inside board
                        #Check if there is a player piece there
                        new_pos = chr(col+1) + str(row)
                        if state.board.get(new_pos) != player:
                            actions.append(pos + "-" + new_pos)

                    #Move left
                    if row > 0  and col - 1 >= 97:
                        #Move fits inside board
                        #Check if there is a player piece there
                        new_pos = chr(col-1) + str(row)
                        if state.board.get(new_pos) != player:
                            actions.append(pos + "-" + new_pos)
        return sorted(actions)
    
    def result(self, state, move):
        next_to_move = 2 if state.to_move == 1 else 1
        andre = move.split("-")
        pos_from = andre[0]
        pos_to = andre[1]
        new_board = state.board.copy()
        new_board[pos_to] = new_board.get(pos_from)  
        new_whites = state.whites.copy()
        new_blacks = state.blacks.copy()
        new_col_whites = state.col_whites.copy()
        new_col_blacks = state.col_blacks.copy()
        new_line_whites = state.line_whites.copy()
        new_line_blacks = state.line_blacks.copy()
        if new_board.get(pos_from) == 'W':
            new_whites[pos_to] = new_whites.get(pos_from)
            del new_whites[pos_from]
            new_col_whites[move[0]] = new_col_whites[move[0]] - 1
            new_col_whites[move[3]] = new_col_whites[move[3]] + 1
            new_line_whites[move[1]] = new_line_whites[move[1]] - 1
            new_line_whites[move[4]] = new_line_whites[move[4]] + 1
        else:
            new_blacks[pos_to] = new_blacks.get(pos_from)
            del new_blacks[pos_from]
            new_col_blacks[move[0]] = new_col_blacks[move[0]] - 1
            new_col_blacks[move[3]] = new_col_blacks[move[3]] + 1
            new_line_blacks[move[1]] = new_line_blacks[move[1]] - 1
            new_line_blacks[move[4]] = new_line_blacks[move[4]] + 1
        del new_board[pos_from]
        result = EstadoBT_Miguel(next_to_move, state.utility, new_board, state.moves, new_whites, new_blacks, new_col_whites, new_col_blacks, new_line_whites, new_line_blacks)
        return result
    
    def utility(self, state, player):
        """Return the value of this final state to player."""
        return -1 if self.to_move(state) == 1 else 1


    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        n_whites = 0
        n_blacks = 0

        for pos in state.board.keys():
            pos_piece = state.board.get(pos)
            if pos_piece == "W":
                n_whites+=1
            else:
                n_blacks+=1
            if pos[1] == str(8) and pos_piece == "W":
                return True
            if pos[1] == str(1) and pos_piece == "B":
                return True
        if n_whites == 0 or n_blacks == 0:
            return True
        return False
    
    def display(self, state):
        print("-----------------")
        counter = 8
        result = ""
        for i in range(counter,0, -1):
            result = ""
            result+=str(i)
            result+="|"
            for c in (chr(i) for i in range(97, 97+counter)):   
                piece = state.board.get(c+str(i))
                if type(piece) != str:
                    result+=". "
                else:
                    result+=state.board.get(c+str(i))
                    result+=" "
            print(result)
        print("-+---------------")
        print(" |a b c d e f g h")
        if not self.terminal_test(state):
            print("--NEXT PLAYER:", "W" if self.to_move(state) == 1 else "B")    
    
    def executa(self, estado, listaJogadas):
        "executa varias jogadas sobre um estado dado"
        "devolve o estado final "
        s = estado
        for j in listaJogadas:
            s = self.result(s, j)
        return s

jj = JogoBT_Miguel()
Belarmino = jogadorBT_27("Belarmino", 4, func_aval_Belarmino)
Bela = jogadorBT_27("Bela", 4, func_aval_Belarmino)
Mutu = jogadorBT_27("Mutu", 4, func_aval_27)
Ronaldo = jogadorBT_27("Ronaldo", 2, func_aval_flex)

#joga11com_timeout(jj, Belarmino, Mutu, 10)
# python jogoBT_Miguel.py

counter = 0
for i in range(1,11):
    result = joga11com_timeout(jj, Mutu, Belarmino, 20)
    if result[-1] == 1:
        counter+= 1
    print("game", i, "result",counter)
