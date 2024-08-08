from random import randrange
from time import sleep
import os

aObjeto         = ['COLHER', 'VENTILADOR', 'TRAVESSEIRO', 'CELULAR', 'COMPUTADOR']
aPais           = ['BRAZIL', 'CANADA', 'MONGOLIA', 'PORTUGAL', 'CHILE']
aFrutas         = ['LARANJA', 'ABACATE', 'ABACAXI', 'BANANA', 'TOMATE']
aTemas          = [aObjeto, aPais, aFrutas]

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

def palavraAleatoria(tema):
    cPalavra = tema[randrange(0, len(tema), 1)]
    return cPalavra

def encontraLetra(letraEscolhida, palavra, resultado):
    for i in range(len(palavra)):
        if letraEscolhida.upper() == palavra[i]:   
            resultado[i] = palavra[i]
    return resultado

def jogoDaForca():
    try:
        cTemaEscolhido  = int(input('Selecione um tema de palavra: [0] Objetos [1] Países [2] Frutas: '))
        match cTemaEscolhido:
            case 0: cPalavra = palavraAleatoria(aObjeto)
            case 1: cPalavra = palavraAleatoria(aPais)
            case 2: cPalavra = palavraAleatoria(aFrutas)
        print(f'Sua palavra tem {len(cPalavra)} caracteres.')
        
        cResultado = []
        nPontuacao = 5
        for i in cPalavra:
            cResultado.append('_')

        for i in range(0, 5):
            print(f'Restam {5 - i} tentivas.')
            cLetra = input('Advinhe uma letra:')
            cResultado = encontraLetra(cLetra, cPalavra, cResultado)
            print(''.join(cResultado))
            nPalpite = int(input(f'Deseja realizar um palpite?  [0] Sim [1] Não. Você perderá suas chances restantes, mas ganhará {nPontuacao} pontos.'))
            if nPalpite == 0:
                break
            nPontuacao = nPontuacao - 1

        cResposta = input('E então, qual é a palavra?').strip(' ').upper()
        if cResposta == cPalavra:
            print(f'Parabéns! Você acertou e ganhou {nPontuacao} pontos!!')
        else:
            print(f'Que pena, você não acertou! A palavra correta era {cPalavra}')
    except:
        print('O valor digitado deve estar entre as opções disponíveis.')
        jogoDaForca()
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

print('Bem vindo ao jogo da forca! Você terá cinco tentativas de advinhar a palavra escolhida.')
sleep(1.5)
# try:
#     jogoDaForca()
# except:
#     print('O valor digitado deve estar entre as opções disponíveis.')
    
jogoDaForca()
