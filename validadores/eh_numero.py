def eh_numero(texto_teste):
    try:
        int(texto_teste)
    except ValueError:
        return False
    return True