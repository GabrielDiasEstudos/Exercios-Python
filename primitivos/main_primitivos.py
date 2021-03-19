## Seção de tipos primitivos
import primitivos.inteiros as ex_inteiros
import primitivos.ponto_flutuantes as ex_pontoflutuante
import primitivos.textos as ex_texto
import primitivos.booleanos as ex_booleanos

def mostrar_secao():
    print('-------------------------------------------')
    print('-------- Seção de Tipos Primitivos --------')
    print('-------------------------------------------\n\n')

    print('Qual capítulo você desejar ver?')
    print('1 - Inteiro')
    print('2 - Ponto Flutuante')
    print('3 - Texto (String)')
    print('4 - Lógicos (Booleanos)')

    entrada = input('Sua Resposta? ')

    if not entrada.isdigit():
        print('Resposta não é um número')
        return

    alternativa = int(entrada)

    lista_opcoes = { 
        1 : ex_inteiros, 
        2 : ex_pontoflutuante,
        3 : ex_texto,
        4 : ex_booleanos
    }

    try:
        lista_opcoes[alternativa].mostrar_exemplo()
    except KeyError:
        print('Seção não existe')