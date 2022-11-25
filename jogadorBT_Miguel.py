from jogar import*
from random import*

class jogadorBT_27(JogadorAlfaBeta):
    pass

def func_aval_Belarmino(state,player):
    result = 0
    if player == 1:
        for x in range(1,9):
            result += pow(x,x) * state.line_whites.get(str(x))
    else:
        for x in range(8, 0, -1):
            result += pow(9-x,9-x) * state.line_blacks.get(str(x))
    return result

def func_aval_27(state,player):
    if player == 1:
        return atacante(state, player)
    else:
        return defesa(state, player)

def atacante(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000000000
    column_values = {'a' : 0, 'b' : 400, 'c' : 300, 'd' : 400, 'e' : 400, 'f' : 300, 'g' : 400 ,'h' : 0}
    w_line_values = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8}

    if state.line_whites[str(8)] >= 1:
        return win_value
    elif state.line_blacks[str(1)] >= 1:
        return -1000

    dif = len(state.whites.keys()) - len(state.blacks.keys())
    score += dif*attack_value

    for pos in reversed(state.whites.keys()): 
        score += column_values.get(pos[0]) * w_line_values.get(pos[1])

    score+=func_aval_Belarmino(state, player)/10000000

    return score

def defesa(state, player):
    win_value = float('inf')
    attack_value = 10000000000
    score = 0
    column_values = {'a' : 0, 'b': 400, 'c' : 200, 'd' : 400, 'e' : 400, 'f' : 200, 'g' : 400,'h' : 0}
    b_line_values = {'2' : 100, '3' : 90, '4' : 50, '5' : 50, '6' : 60, '7' : 70, '8' : 80}

    if state.line_blacks[str(1)] >= 1:
        return win_value
    elif state.line_whites[str(8)] >= 1:
        return -1000000

    dif = len(state.blacks.keys()) - len(state.whites.keys())
    score += dif*attack_value

    for pos in state.blacks.keys(): 
        score += column_values.get(pos[0]) * b_line_values.get(pos[1])

    return score

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
        
        if player == 1:
            next_pos = pos[0] + str(int(pos[1]) + 1)

        else:
            next_pos = pos[0] + str(int(pos[1]) - 1)

        for pos2 in state.board.keys():
            if pos2[0] == 'b' and pos2 == next_pos:
                n_tower_b += 1
            if pos2[0] == 'g' and pos2 == next_pos:
                n_tower_g += 1
            if pos2[0] == 'd' and pos2 == next_pos:
                n_tower_d += 1
            if pos2[0] == 'e' and pos2 == next_pos:
                n_tower_e += 1

        score += n_tower_b * tower_value
        score += n_tower_g * tower_value
        score += n_tower_d * tower_value
        score += n_tower_e * tower_value
        score += n_tower_b * tower_value + n_tower_g * tower_value + n_tower_d * tower_value + n_tower_e * tower_value
        
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

    score+=func_aval_Belarmino(state, player)/1000

    return score


