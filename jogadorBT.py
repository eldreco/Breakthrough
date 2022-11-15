from jogar import*
from random import*

class jogadorBT_27(JogadorAlfaBeta):
    pass

def func_aval_flex(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000000
    column_values = {'a' : 0, 'b':400, 'c' : 200, 'd' : 300, 'e' : 300, 'f' : 200, 'g' : 400 ,'h' : 0}
    n_blacks = 0
    n_whites = 0
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
            n_whites+=1

        else:
            n_blacks+=1

        if pos_piece == player_piece:
            score += column_values.get(pos[0])
        


    
    if player == 1:
        dif = n_whites - n_blacks

        score+= dif*attack_value

    score+=func_aval_Belarmino(state, player)/1000

    return score


def func_aval_chorao(state, player):
    score = 0
    win_value = float('inf')
    attack_value = 10000
    column_values = {'a' : 0, 'b':400, 'c' : 200, 'd' : 300, 'e' : 300, 'f' : 200, 'g' : 400 ,'h' : 0}
    n_blacks = 0
    n_whites = 0
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
            n_whites+=1

        else:
            n_blacks+=1

        if pos_piece == player_piece:
            score += column_values.get(pos[0])
        


    
    if player == 1:
        dif = n_whites - n_blacks

        return dif*attack_value

    score+=func_aval_Belarmino(state, player)/1000

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

def func_aval_Belarmino(state,player):
    result = 0
    for x in range(1,9):
        result += pow(x,x) * count_pieces(state, x, player)
    return result    
        