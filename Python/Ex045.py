#Exercício 045 - Crie um programa que faça o computador jogar Jokenpô com você
"""import random
from time import sleep

jokenpo = ['pedra', 'papel', 'tesoura']
escolhido = random.choice(jokenpo)
jogador = str(input('Qual você escolhe: pedra, papel ou tesoura? ')).strip().lower()

#Computador ganhando
if escolhido == 'pedra' and jogador == 'tesoura' or escolhido == 'papel' and jogador == 'pedra' or escolhido == 'tesoura' and jogador == 'papel':
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ...')
    sleep(0.3)
    print('Eu escolho {} e você {}, GANHEEEI. Boa sorte na próxima!'.format(escolhido, jogador))

#Empate
elif escolhido == 'pedra' and jogador == 'pedra' or escolhido == 'tesoura' and jogador == 'tesoura' or escolhido == 'papel' and jogador == 'papel':
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ...')
    sleep(0.3)
    print('Eu escolho {} e você {}, DROGA! Empatamos, vamos de novo que vou ganhar!'.format(escolhido, jogador))

#Usuário ganhando
elif jogador == 'pedra' and escolhido == 'tesoura' or jogador == 'papel' and escolhido == 'pedra' or jogador == 'tesoura' and escolhido == 'papel':
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ...')
    sleep(0.3)
    print('Você conseguiu ganhar de mim, você escolheu {} e eu {}. Sorte de principiante!'.format(jogador, escolhido))"""

#Resolução do professor abaixo:
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador ==2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
