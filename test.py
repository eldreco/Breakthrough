from jogoBT_Andre import*
from jogadorBT_Andre import*

#------------------------------------------------------------------------
#                       Estatísticas

Belarmino1 = jogadorBT_27("Belarmino1",2, func_aval_Belarmino)
Belarmino2 = jogadorBT_27("Belarmino2",4, func_aval_Belarmino)
Ronaldo = jogadorBT_27("Ronaldo", 3, func_aval_flex)
Messi = jogadorBT_27("Messi", 2, func_aval_chorao)
Mutu = jogadorBT_27("Mutu", 3, func_aval_mutu)


Copiado = jogadorBT_27("Copiado", 3, func_aval_copiado)
#Copiado2 = jogadorBT_27("Copiado2", 4, func_aval_copiado2)



jj = JogoBT_27()




joga11com_timeout(jj, Ronaldo, Belarmino1, 10)

def testes():
    print("testes")
    counter = 0

    for i in range(1,51):
        result = joga11com_timeout(jj, Mutu, Ronaldo, 10)
        if result[-1] == -1:
            counter+= 1
        print("game", i, "result",counter)


#testes()