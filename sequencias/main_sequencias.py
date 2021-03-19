## Seção de Estruturas Sequenciais

import sequencias.lista as ex_lista
import sequencias.funcoes_listas as ex_funcoes_listas
import sequencias.dicionario as ex_dicionario

def mostrar_secao():
    print('-------------------------------------------')
    print('-------- Seção de Operadores --------')
    print('-------------------------------------------\n\n')

    print('Qual capítulo você desejar ver?')
    print('1 - Listas')
    print('2 - Funções de Listas')
    print('3 - Dicionários')

    entrada = input('Sua Resposta? ')

    if not entrada.isdigit():
        print('Resposta não é um número')
        return

    alternativa = int(entrada)

    lista_opcoes = { 
        1 : ex_lista, 
        2 : ex_funcoes_listas,
        3 : ex_dicionario
    }

    try:
        lista_opcoes[alternativa].mostrar_exemplo()
    except KeyError:
        print('Seção não existe')
