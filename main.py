import primitivos.main_primitivos as secao_primitivos
import operadores.main_operadores as secao_operadores
import sequencias.main_sequencias as secao_sequencias
import desvios.main_desvios as secao_desvios

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
        secao_sequencias.mostrar_secao()
    elif alternativa == 4:
        secao_desvios.mostrar_secao()
    else:
        print('Opção não existe')