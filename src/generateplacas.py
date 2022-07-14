from itertools import product

def placaspatentes():
    listaLetras = []
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    alpha_list = [letras]*3
    digit_list = [numeros]*3
    for i in product(*alpha_list):
        for j in product(*digit_list):
          listaLetras.append(''.join(i + j))
    return listaLetras