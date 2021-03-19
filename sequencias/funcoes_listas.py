# Adição e Remoção

def mostrar_exemplo():
    numeros = list(range(1, 11))

    # print(dir(numeros)) # lista as funções da lista

    print(numeros)
    numeros.pop()  # remove o último item
    # help(numeros.pop())  # função documentação

    print(numeros)

    numeros.append(10) # adiciona um elemento

    print(numeros)

    numeros.extend([11, 12]) # junta uma lista com a outra
    print(numeros)

    print([1, 3] + [2, 4])

    print([1, 3] * 3)