## Seção de Estruturas de Desvio e Laços de Repetiçãos

import desvios.se as ex_if
import desvios.repeticao as ex_repeticao

def mostrar_secao():
    print('---------------------------------------------------------')
    print('-- Seção de Estruturas de Desvio e Laços de Repetiçãos --')
    print('---------------------------------------------------------\n\n')

    print('Qual capítulo você desejar ver?')
    print('1 - Se (If)')
    print('2 - Para cada (For)')

    entrada = input('Sua Resposta? ')

    if not entrada.isdigit():
        print('Resposta não é um número')
        return

    alternativa = int(entrada)

    lista_opcoes = { 
        1 : ex_if, 
        2 : ex_repeticao,
    }

    try:
        lista_opcoes[alternativa].mostrar_exemplo()
    except KeyError:
        print('Seção não existe')