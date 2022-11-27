from jogar import*
from random import*

class jogadorBT_27(JogadorAlfaBeta):
    pass

def func_aval_flex(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000000
    column_values = {'a' : 0, 'b':300, 'c' : 200, 'd' : 400, 'e' : 400, 'f' : 200, 'g' : 300 ,'h' : 0}
    n_blacks = []
    n_whites = []
    tower_value = 500
    n_tower_b = 0
    n_tower_g = 0
    n_tower_d = 0
    n_tower_e = 0

    player_piece = 'W' if player == 1 else 'B'

    for pos in state.board.keys(): 

        pos_piece = state.board.get(pos)

        if player == 1:
            if pos[1] == 8:
                return win_value
        else:
            if pos[1] == 1:
                return win_value
        
        if pos_piece == "W":
            n_whites.append(pos)
        else:
            n_blacks.append(pos)

        if pos_piece == player_piece:
            score += column_values.get(pos[0])
    
    if player == 1:
        dif = len(n_whites) - len(n_blacks)
        score+= dif*attack_value
    else:
        dif = len(n_blacks) - len(n_whites)
        score+= dif*attack_value

    score+=func_aval_Belarmino_David(state, player)/1000

    return score

def func_aval_copiado(state, player):

    #funcs

    def eval_column(state, player):
        
        #Value the amount of pieces in collumns b, d, e and g in order for 
        #the player to prioritize placing pieces in those collumns

        result = 0
        player = 'W' if player == 1 else 'B'

        for pos in state.board.keys():

            piece = state.board.get(pos)

            if piece == player:

                if pos[0] == 'b' or pos[0] == 'g':
                    result += 2 
                elif pos[0] == 'd' or pos[0] == 'e':
                    result += 1

        return result

    def eval_attack(state, player):

        #Value a bigger difference between pieces of the player and the adversary, such that the
        #player will capture a piece when possible

        player = 'W' if player == 1 else 'B'
        n_white = 0
        n_blacks = 0
        dif = 0

        for pos in state.board.keys():

            piece = state.board.get(pos)

            if piece == 'W':
                n_white+=1
            else:
                n_blacks+=1

            
            if player == 'W':

                dif = n_white - n_blacks

            else:
                dif = n_blacks - n_white

        return dif

    def eval_endgame(state, player):
        
        score = 0
        player = 'W' if player == 1 else 'B'

        for pos in state.board.keys():

            piece = state.board.get(pos)

            if piece == 'W' and pos[1] == 8:
                return 15
            elif piece == 'B' and pos[1] == 1:
                return -15



        return score

    def eval_defense(state, player):

        #Devalue states where the adversary has many pieces
        #on the player's side

        player_to_avoid = 'B' if player == 1 else 'W'
        score = 0

        for pos in state.board.keys():

            piece = state.board.get(pos)

            if piece == player_to_avoid and int(pos[1]) < 5 and player_to_avoid == 'B':
                score-=2

            elif piece == player_to_avoid and int(pos[1]) > 5 and player_to_avoid == 'W':
                score-=2

        return score

    def eval_backline(state, player):

        #Values a rear line of defense

        player = 'W' if player == 1 else 'B'
        score = 0
        

        for pos in state.board.keys():

            piece = state.board.get(pos)

            if piece == player and pos[1] == 1:
                score+=100

        return score

    def eval_towers(state, player):

        #Values the existance of continuos towers in certain collumns
        score = 0

        player = 'W' if player == 1 else 'B'

        for pos in state.board.keys():

            next_pos = pos[0] + str(int(pos[1]) + 1)

            for pos2 in state.board.keys():

                next_pos2 = pos2[0] + str(int(pos2[1]) + 1)
                piece1 = state.board.get(pos)
                piece2 = state.board.get(pos2) 

                if pos == next_pos and next_pos2 == pos2 and piece1 == player and piece2 == player:
                    score+=15

        return score

    def eval_advance(state,player):
        result = 0
        if player == 1:
            for x in range(1,9):
                result += pow(x,x) * state.line_whites.get(str(x))
        else:
            for x in range(8, 0, -1):
                result += pow(9-x,9-x) * state.line_blacks.get(str(x))
        return result/1000

    #funcs



    evaluators = [eval_column, eval_attack, eval_defense, eval_advance]
    score = 0

    for evaluator in evaluators:

        score += evaluator(state, player)
    
    return score
    
    

def func_aval_passivo(state, player):

    score = 0
    win_value = 10000000
    attack_value = 10000
    column_values = {'a' : 0, 'b':400, 'c' : 100, 'd' : 300, 'e' : 300, 'f' : 100, 'g' : 400 ,'h' : 0}
    n_blacks = []
    n_whites = []

    n_pieces_per_line = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0} 

    player_piece = 'W' if player == 1 else 'B'

    for pos in state.board.keys(): 

        pos_piece = state.board.get(pos)

        if player == 1:
            if pos[1] == 8:
                return win_value
        else:
            if pos[1] == 1:
                return win_value

        
        if pos_piece == "W":
            n_whites.append(pos)
            n_whites_in_line = n_pieces_per_line[int(pos[1])]
            n_whites_in_line+=1
            n_pieces_per_line[int(pos[1])] = n_whites_in_line
        else:
            n_blacks.append(pos)
            n_blacks_in_line = n_pieces_per_line[int(pos[1])]
            n_blacks_in_line+=1
            n_pieces_per_line[int(pos[1])] = n_blacks_in_line

        if pos_piece == player_piece:
            score += column_values.get(pos[0])
    
    result = 0

    if player == 1:
        dif = len(n_whites) - len(n_blacks)
        score+= dif*attack_value

        for x in range(1,9):
            result += (pow(x,x) * n_pieces_per_line.get(x))

    else:
        dif = len(n_blacks) - len(n_whites)
        score+= dif*attack_value

        for x in range(8, 0, -1):
            result += (pow(9-x,9-x) * n_pieces_per_line.get(x))


    return score + result/1000

def func_aval_chorao(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000
    column_values = {'a' : 0, 'b':400, 'c' : 200, 'd' : 300, 'e' : 300, 'f' : 200, 'g' : 400 ,'h' : 0}
    n_blacks = []
    n_whites = []
    n_tower_b = 0
    n_tower_g = 0

    player_piece = 'W' if player == 1 else 'B'

    for pos in state.board.keys(): 

        pos_piece = state.board.get(pos)

        if player == 1:
            if pos[1] == 8:
                return win_value
        else:
            if pos[1] == 1:
                return win_value
        
        if pos_piece == "W":
            n_whites.append(pos)

        else:
            n_blacks.append(pos)

        if pos_piece == player_piece:
            score += column_values.get(pos[0])
    
    if player == 1:
        dif = len(n_whites) - len(n_blacks)
        return dif*attack_value
    else:
        dif = len(n_blacks) - len(n_whites)
        return dif*attack_value

    score+=func_aval_Belarmino_David(state, player)/1000

    return score
    
def count_pieces(state, line, player):
    count = 0
    if player == 1:
        for pos in state.board.keys():
            if str(line) in pos and state.board.get(pos) == "W":
                count += 1
    else:
        for pos in state.board.keys():
            if str(line) in pos and state.board.get(pos) == "B":
                count += 1
    return count

def func_aval_Belarmino_David(state,player):
    result = 0

    if player == 1:

        for x in range(1,9):
            result += pow(x,x) * count_pieces(state, x, player)
    else:
        for x in range(8, 0, -1):
            result += pow(9-x,9-x) * count_pieces(state, x, player)
    
    return result

def func_aval_mutu(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000
    column_values = {'a' : 0, 'b' : 400, 'c' : 400, 'd' : 200, 'e' : 200, 'f' : 400, 'g' : 400 ,'h' : 0}
    w_line_values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8}
    b_line_values = {'1' : 8, '2' : 7, '3' : 6, '4' : 5, '5' : 4, '6' : 3, '7' : 2, '8' : 1}
    n_blacks = []
    n_whites = []
    n_tower_b = 0
    n_tower_g = 0

    player_piece = 'W' if player == 1 else 'B'

    keys_list = reversed(state.board.keys())

    for pos in keys_list: 

        if player == 1:
            if pos[1] == 8:
                return win_value
        else:
            if pos[1] == 1:
                return win_value

        pos_piece = state.board.get(pos)
        
        if pos_piece == player_piece:
            if player_piece == 1:
                score += column_values.get(pos[0]) * w_line_values.get(pos[0])
            else:
                score += column_values.get(pos[0]) * b_line_values.get(pos[1])

        if pos_piece == "W":
            n_whites.append(pos)
        else:
            n_blacks.append(pos)
    
    if player == 1:
        dif = len(n_whites) - len(n_blacks)
        score += dif*attack_value
    else:
        dif = len(n_blacks) - len(n_whites)
        score += dif*attack_value

    score+=func_aval_Belarmino_David(state, player)/100

    return score
        