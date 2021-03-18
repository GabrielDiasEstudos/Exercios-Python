import primitivos.inteiros as exemplo_inteiros
import primitivos.ponto_flutuantes as ex_pontoflutuante
import primitivos.textos as ex_texto
import primitivos.booleanos as ex_booleanos

import operadores.aritmeticos as exemplo_operacoes
import operadores.unarios as exemplo_unarios
import operadores.logicos as exemplo_logicos

#Fundamentos de lógica de programação com Python

alternativa = 7

if alternativa == 1:
    exemplo_inteiros.mostrar_exemplo()
elif alternativa == 2:
    exemplo_operacoes.mostrar_exemplo()
elif alternativa == 3:
    ex_pontoflutuante.mostrar_exemplo()
elif alternativa == 4:
    ex_texto.mostrar_exemplo()
elif alternativa == 5:
    ex_booleanos.mostrar_exemplo()
elif alternativa == 6:
    exemplo_unarios.mostrar_exemplo()
elif alternativa == 7:
    exemplo_logicos.mostrar_exemplo()