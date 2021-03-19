## Seção de Operadores

import operadores.aritmeticos as exemplo_operacoes
import operadores.unarios as exemplo_unarios
import operadores.logicos as exemplo_logicos
import operadores.comparacao as exemplo_comparacao

def mostrar_secao():
    print('-------------------------------------------')
    print('----------- Seção de Operadores -----------')
    print('-------------------------------------------\n\n')

    print('Qual capítulo você desejar ver?')
    print('1 - Aritméticos')
    print('2 - Unários')
    print('3 - Lógicos')
    print('4 - Comparação')

    entrada = input('Sua Resposta? ')

    if not entrada.isdigit():
        print('Resposta não é um número')
        return

    alternativa = int(entrada)

    lista_opcoes = { 
        1 : exemplo_operacoes, 
        2 : exemplo_unarios,
        3 : exemplo_logicos,
        4 : exemplo_comparacao
    }

    try:
        lista_opcoes[alternativa].mostrar_exemplo()
    except KeyError:
        print('Seção não existe')
