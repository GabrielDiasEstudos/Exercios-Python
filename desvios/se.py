# If

def mostrar_exemplo():
    idade = 18

    mensagem = classificar_idade(idade, 'Gabriel')

    print(mensagem)
    

# Exemplo de função

def classificar_idade(idade, nome):
    if idade < 18:
        return '{} é menor de idade: sua idade é {}'.format(nome, idade)
    elif idade >= 65:
        return '{} é pessoa idosa: sua idade é {}'.format(nome, idade)
    else:
        return '{} é maior de idade: sua idade é {}'.format(nome, idade)