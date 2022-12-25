#Exercício 058 - melhore o jogo do desafio 028 onde o computador vai "pensar em um número
#entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos papites
#foram necessários para vencer.
#Minha resposta
'''from random import randint
from time import sleep
computador = randint(0, 10)
print('-=-' * 20)
print('Sou seu computador...')
sleep(2)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(1)

c = 0
while jogador != computador:
    print('\33[31mVOCÊ PERDEU! Eu pensei no número {} e não no {}! Tente novamente!\33[m'.format(computador, jogador))
    c = c + 1
    computador = randint(0, 10)
    jogador = int(input('Em que número eu pensei entre 0 e 10? '))
    print('PROCESSANDO...')
    sleep(1)
if jogador == computador:
    print('\33[32mPARABÉNS, você acertou! Foram necessárias {} vezes para ganhar você de mim.\33[m'.format(c + 1))
print('\33[7;37;40m======================================= FIM =======================================\33[m')'''

#Resposta do professor
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
