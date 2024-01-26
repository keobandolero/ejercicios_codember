cadena = '&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&'


def desifra(cadena):
    resultado= ''
    cero = 0
    for caracter in cadena:
        if caracter == '#':
            cero += 1
        elif caracter == '@':
            cero -= 1
        elif caracter == '*':
            cero *= cero
        elif caracter == '&':
            resultado += str(cero)
    return resultado
    #!El codigo se describe solo super easy.

print(desifra(cadena))


""" "#" Incrementa el valor numérico en 1.
 "@" Decrementa el valor numérico en 1.
 "*" Multiplica el valor numérico por sí mismo.
 "&" Imprime el valor numérico actual. """