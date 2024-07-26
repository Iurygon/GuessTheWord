from random import randrange
from time import sleep

aObjeto         = ['Colher', 'Ventilador', 'Travesseiro', 'Celular', 'Computador']
aPais           = ['Brasil', 'Canada', 'Estados Unidos', 'Portugal', 'Chile']
aFrutas         = ['Laranja', 'Abacate', 'Abacaxi', 'Banana', 'Tomate']
aTemas          = [aObjeto, aPais, aFrutas]

nTentativa      = 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

print('Bem vindo ao jogo da forca! Você terá cinco tentativas de advinhar a palavra escolhida.')
sleep(1.5)
cTemaEscolhido  = input('Selecione um tema de palavra: [0] Objetos [1] Países [2] Frutas: ')
sleep(1.5)

def palavraAleatoria(tema):
    cPalavra = tema[randrange(0, len(tema), 1)]
    return cPalavra

def encontraLetra(letraEscolhida, palavra):
    for letra in palavra:
        if letraEscolhida == palavra[letra]:   
            

def jogoDaForca():
    match cTemaEscolhido:
        case '0': cPalavra = palavraAleatoria(aObjeto)
        case '1': cPalavra = palavraAleatoria(aPais)
        case '2': cPalavra = palavraAleatoria(aFrutas)
    print(f'Sua palavra tem {len(cPalavra)} caracteres.')
    cLetra = input('Qual letra você gostaria de tentar primeiro?')

