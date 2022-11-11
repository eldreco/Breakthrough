from jogoBT import*
from jogar import*

class jogadorBT_27(Jogador):
    
    def __init__(self, state, player):
        self.state = state
        self.player = player
        
    def func_aval_27(self, state, player):
        return state[1] #????