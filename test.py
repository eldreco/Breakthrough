from jogoBT import*
from jogadorBT import*

#------------------------------------------------------------------------
#                       Estatísticas

Belarmino1 = jogadorBT_27("Belarmino1",4, func_aval_Belarmino)
Belarmino2 = jogadorBT_27("Belarmino2",4, func_aval_Belarmino)
Ronaldo = jogadorBT_27("Ronaldo", 4, func_aval_flex)
Messi = jogadorBT_27("Messi", 2, func_aval_chorao)
Mutu = jogadorBT_27("Mutu", 4, func_aval_mutu)
David = jogadorBT_27("David", 4, func_aval_copiado)
Escolhido1 = jogadorBT_27("Escolhido1", 4, func_aval_defesa)
Escolhido2 = jogadorBT_27("Escolhido2", 4, func_aval_defesa)


jj = JogoBT_27()

#joga11com_timeout(jj, Belarmino1, Belarmino2, 10)

counter = 0
for i in range(1,101):
    result = joga11com_timeout(jj, Escolhido1, Belarmino1, 10)
    if result[-1] == -1:
        counter+= 1
    print("game", i, "result",counter)