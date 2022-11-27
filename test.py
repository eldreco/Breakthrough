from jogadorBT_David import *
from jogadorBT_Miguel import *
from jogoBT_David import *
from jogoBT_Miguel import *

jogo1 = JogoBT_27()
jogo2 = JogoBT_Miguel()

jogadorDavid = JogadorAlfaBeta('David', 4, func_aval_copiado)
#jogadorMiguel = JogadorAlfaBeta('Miguel', 1, func_aval_27)
#jogadorBelarmino = JogadorAlfaBeta('Belarmino', 1, func_aval_Belarmino)
#jogadorRandom = Jogador('Random', random_player)
#jogadorRonaldo = JogadorAlfaBeta('Ronaldo', 4, func_aval_flex)
#jogadorMutu2 = JogadorAlfaBeta('Mutu2', 4, func_aval_mutu)
jogadorBelarminoBurro = JogadorAlfaBeta('BelarminoBurro', 4 , func_aval_Belarmino_David)

score = 0
print('Depth 1, white, jog1')
for i in range(0, 100):

    result = uiui_joga11com_timeout(JogoBT_Miguel, jogadorBelarminoBurro, JogoBT_Miguel, jogadorDavid, jogo1, 10)
    if result[-1] == -1:
        score+=1

    print('Jogo: ', i , ' Vitórias: ', score)
