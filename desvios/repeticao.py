
def mostrar_exemplo():
    idades = [17, 38, 70, 80]
    print(classificar_idade(idades[0], 'Gabriel'))

    print('\n----------------------------------------------------')
    for idade in idades:
        print(classificar_idade(idade, 'Pessoa'))

def classificar_idade(idade, nome):
    if idade < 18:
        return '{} é menor de idade: sua idade é {}'.format(nome, idade)
    elif idade >= 65:
        return '{} é pessoa idosa: sua idade é {}'.format(nome, idade)
    else:
        return '{} é maior de idade: sua idade é {}'.format(nome, idade)