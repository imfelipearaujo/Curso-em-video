"""Exercício 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que
o vencedor tirou o maior número no dado."""
from random import randint
from time import sleep
for v in range(1, 4):
    jogo = randint(1, 6)
jogadores = {'jogador1': jogo, 'jogador2': jogo, 'jogador3': jogo, 'jogador4': jogo}
print('-=' * 5, '<<< VALORES SORTEADOS >>>', '-=' * 5)
for k, v in jogadores.items():
    jogo = randint(1, 6)
    print(f'O {k} tirou {jogo}')
    sleep(1)
print()
print('-=' * 5, '<<< RANKING DOS JOGADORES >>>', '-=' * 5)
