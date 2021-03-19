# Exemplo de Listas

def mostrar_exemplo():
    lista = [1, 4.5, 23, 12, 9999, 1213]

    print(type(lista))
    print(lista)

    print(lista[0])

    print(len(lista))  # Tamanho da coleção

    # Duas maneiras de pegar o último item da lista
    print(f'Meu último elemento é: {lista[len(lista) - 1]}')
    print(f'Meu último elemento é: {lista[-1]}')

    # Fatiamento da lista
    print(lista[0:2])
    print(lista[:2])

    numeros = list(range(1, 11))
    print(numeros)
    print(numeros[1: 7: 2])

    # Exemplo de tratamento de exceção em Python
    try:
        print(lista[99999999])
    except IndexError as e:
        print('Deu erro: {}'.format(e))