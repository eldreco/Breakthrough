from jogoBT import*
from jogar import*
from random import*

class jogadorBT_27(Jogador):
    def __init__(self, nome, state, player, fun):
        self.nome = nome
        self.player = player
        self.fun = fun
    def display(self):
        print(nome+" ")

def func_aval_27(self, state, player):
    pass

def func_aval_random(self,state,player):
    return random.choice(actions(state))

def func_aval_Belarmino(self,state,player):
    pass    

def jogaBreak_Through(jog1, jog2):
    jogo = JogoBT_27()
    estado = jogo.initial
    prox_jogador = jog1
    lista_jogadas = []
    while not jogo.terminal_test(estado):
        jogada = prox_jogador.fun