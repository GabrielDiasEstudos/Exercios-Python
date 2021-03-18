# Operadores Lógicos

def mostrar_exemplo():
    mostrar_exemplo_operador_and()

    mostrar_exemplo_operador_or()

def mostrar_exemplo_operador_and():
    print('----------------------------------------------------')
    print('------------------- OPERADOR AND -------------------')

    primeira_validacao_and = True and True
    print(f'Verdadeiro e verdadeiro = {primeira_validacao_and}')

    segunda_validacao_and = True and False
    print(f'Verdadeiro e falso = {segunda_validacao_and}')

    terceira_validacao_and = False and False
    print(f'Falso e falso = {terceira_validacao_and}')
    print('----------------------------------------------------\n\n')

def mostrar_exemplo_operador_or():
    print('------------------- OPERADOR OR --------------------')
    primeira_validacao_or = True or True
    print(f'Verdadeiro ou verdadeiro = {primeira_validacao_or}')

    segunda_validacao_or = True or False
    print(f'Verdadeiro ou falso = {segunda_validacao_or}')

    terceira_validacao_or = False or False
    print(f'Falso ou falso = {terceira_validacao_or}')
    print('----------------------------------------------------\n\n')