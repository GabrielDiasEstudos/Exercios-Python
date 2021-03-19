# Dicionario

def mostrar_exemplo():
    linguas = {'pt' : 'Portugues', 'en' : 'Inglês'}
    
    print(linguas)
    print(linguas['pt'])

    try:
        print(linguas['es'])
    except KeyError as e:
        print(f'Erro: {e}')
    
    linguas['es'] = 'Espanhol'
    print(linguas)

    for valor in linguas.values():
        print(valor)

    for chave, valor in linguas.items():
        print(chave, valor)