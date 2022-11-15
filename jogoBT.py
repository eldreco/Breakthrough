from jogos import*
from jogar import *
from jogadorBT import *

EstadoBT_27 = namedtuple('State', 'to_move, utility, board, moves')

class JogoBT_27(Game):
    #to_move = 1
    #utility = 0 #????
    #size = 8

    board = {"a1" : 'W', "b1" : 'W', "c1" : 'W', "d1" : 'W', "e1" : 'W', "f1" : 'W', "g1" : 'W', "h1" : 'W',
                "a2" : 'W', "b2" : 'W', "c2" : 'W', "d2" : 'W', "e2" : 'W', "f2" : 'W', "g2" : 'W', "h2" : 'W',
                "a7" : 'B', "b7" : 'B', "c7" : 'B', "d7" : 'B', "e7" : 'B', "f7" : 'B', "g7" : 'B', "h7" : 'B',
                "a8" : 'B', "b8" : 'B', "c8" : 'B', "d8" : 'B', "e8" : 'B', "f8" : 'B', "g8" : 'B', "h8" : 'B'}
    moves = ['a2-a3', 'a2-b3', 'b2-a3', 'b2-b3', 'b2-c3', 'c2-b3', 'c2-c3', 'c2-d3',
                'd2-c3', 'd2-d3', 'd2-e3', 'e2-d3', 'e2-e3', 'e2-f3', 'f2-e3', 'f2-f3',
                'f2-g3', 'g2-f3', 'g2-g3', 'g2-h3', 'h2-g3','h2-h3']
    initial = EstadoBT_27(1, 0, board, moves)

    def _init(self, size = 8):
        self.size = size
        self.initial = initial

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
        move = move.split("-")
        pos_from = move[0]
        pos_to = move[1]
        new_board = state.board.copy()
        new_board[pos_to] = new_board.get(pos_from)   
        del new_board[pos_from]
        result = EstadoBT_27(next_to_move, state.utility, new_board, state.moves)
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

Belarmino = jogadorBT_27("Belarmino",2, func_aval_Belarmino)

minimax = Jogador("minima", minimax_player)
Ronaldo = jogadorBT_27("Ronaldo", 2, func_aval_flex)
Messi = jogadorBT_27("Messi", 2, func_aval_chorao)

jj = JogoBT_27()

listaJogadores = [Belarmino, Belarmino, Belarmino, Belarmino, minimax, minimax, Ronaldo,Messi]

faz_campeonato(jj, listaJogadores, 10)

#print(joga11(jj, Ronaldo, Belarmino))

#jj.jogar(query_player, random_player)

