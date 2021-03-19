import primitivos.inteiros as exemplo_inteiros
import primitivos.ponto_flutuantes as ex_pontoflutuante
import primitivos.textos as ex_texto
import primitivos.booleanos as ex_booleanos

import operadores.aritmeticos as exemplo_operacoes
import operadores.unarios as exemplo_unarios
import operadores.logicos as exemplo_logicos
import operadores.comparacao as exemplo_comparacao

import desvios.se as ex_if

import sequencias.lista as ex_seq
import sequencias.funcoes_listas as ex_funcoes_listas

#Fundamentos de lógica de programação com Python

entrada = input('Qual exemplo você quer ver? ')

if not entrada.isdigit():
    print('Texto digitado não é número')
else:
    alternativa = int(entrada)

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
    elif alternativa == 8:
        exemplo_comparacao.mostrar_exemplo()
    elif alternativa == 9:
        ex_if.mostrar_exemplo()
    elif alternativa == 10:
        ex_seq.mostrar_exemplo()
    elif alternativa == 11:
        ex_funcoes_listas.mostrar_exemplo()