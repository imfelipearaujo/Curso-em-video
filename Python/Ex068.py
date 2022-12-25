#Exercício 068 - Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando
#o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
#Minha resposta
"""from random import randint
cont = derrota = 0
computador = randint(1, 10)
jogador = 0
esc = ''
while derrota == 0:
    jogador = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    s = computador + jogador
    if jogador % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU PAR.')
        if esc in 'Pp':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
        else:
            break
            print('Você PERDEU!')
            derrota += 1
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {s} DEU ÍMPAR.')
        if esc in 'ÍíIi':
            cont += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
        else:
            print('Você PERDEU!')
            derrota += 1
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')"""

#Reposta do professor
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
