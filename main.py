import primitivos.main_primitivos as secao_primitivos
import operadores.main_operadores as secao_operadores

import desvios.se as ex_if
import desvios.repeticao as ex_repeticao

import sequencias.lista as ex_seq
import sequencias.funcoes_listas as ex_funcoes_listas
import sequencias.dicionario as ex_dicionario

# Fundamentos de lógica de programação com Python

print('-------------------------------------------')
print('--------- Aprendizado de Python -----------')
print('-------------------------------------------')
print('Qual seção você quer ver? \n\n')

print('1 - Tipos Primitivos')
print('2 - Operadores')
print('3 - Listas, Sequências')
print('4 - Desvios e Laços de Repetições')
entrada = input('Sua resposta: ')

if not entrada.isdigit():
    print('Texto digitado não é número')
else:
    alternativa = int(entrada)

    if alternativa == 1:
        secao_primitivos.mostrar_secao()
    elif alternativa == 2:
        secao_operadores.mostrar_secao()
    elif alternativa == 3:
        print('Em manutenção')
    elif alternativa == 4:
        print('Em manutenção')
    else:
        print('Opção não existe')