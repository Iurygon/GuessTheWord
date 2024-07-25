from random import randrange

aObjeto         = ['Colher', 'Ventilador', 'Travesseiro', 'Celular', 'Computador']
aPais           = ['Brasil', 'Canada', 'Estados Unidos', 'Portugal', 'Chile']
aFrutas         = ['Laranja', 'Abacate', 'Abacaxi', 'Banana', 'Tomate']
aTemas          = [aObjeto, aPais, aFrutas]

cTemaEscolhido  = input('Selecione um tema de palavra: [0] Objetos [1] Países [2] Frutas: ')
cPalavra        = ''
cLetra          = ''

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def palavraAleatoria(tema):
    cPalavra = tema[randrange(0, len(tema), 1)]
    return cPalavra

match cTemaEscolhido:
    case '0': palavraAleatoria(aObjeto)
    case '1': palavraAleatoria(aPais)
    case '2': palavraAleatoria(aFrutas)
