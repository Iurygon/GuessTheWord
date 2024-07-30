from random import randrange
from time import sleep

aObjeto         = ['COLHER', 'VENTILADOR', 'TRAVESSEIRO', 'CELULAR', 'COMPUTADOR']
aPais           = ['BRAZIL', 'CANADA', 'MONGOLIA', 'PORTUGAL', 'CHILE']
aFrutas         = ['LARANJA', 'ABACATE', 'ABACAXI', 'BANANA', 'TOMATE']
aTemas          = [aObjeto, aPais, aFrutas]

nTentativa      = 5
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

print('Bem vindo ao jogo da forca! Você terá cinco tentativas de advinhar a palavra escolhida.')
sleep(1.5)
cTemaEscolhido  = input('Selecione um tema de palavra: [0] Objetos [1] Países [2] Frutas: ').strip(' ')
sleep(1.5)

def palavraAleatoria(tema):
    cPalavra = tema[randrange(0, len(tema), 1)]
    return cPalavra

def encontraLetra(letraEscolhida, palavra, resultado):
    for i in range(len(palavra)):
        if letraEscolhida.upper() == palavra[i]:   
            resultado[i] = palavra[i]
    return resultado

def jogoDaForca():
    match cTemaEscolhido:
        case '0': cPalavra = palavraAleatoria(aObjeto)
        case '1': cPalavra = palavraAleatoria(aPais)
        case '2': cPalavra = palavraAleatoria(aFrutas)
    print(f'Sua palavra tem {len(cPalavra)} caracteres.')
    cResultado = []
    for i in cPalavra:
        cResultado.append('_')
    for i in range(0, 5):
        print(f'Esta é a tentativa número {i + 1}. Restam {5 - i}')
        cLetra = input('Advinhe uma letra:')
        cResultado = encontraLetra(cLetra, cPalavra, cResultado)
        print(''.join(cResultado))
    print('Acabaram as tentativas!')
    cResposta = input('E então, qual é a palavra?').strip(' ').upper()
    if cResposta == cPalavra:
        print('Parabéns! Você acertou!!')
    else:
        print(f'Que pena, você não acertou! A palavra correta era {cPalavra}')

jogoDaForca()
