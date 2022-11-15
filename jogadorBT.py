from jogar import*
from random import*

class jogadorBT_27(JogadorAlfaBeta):
    pass

def func_aval_27(state, player):
    return 1
    
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
        