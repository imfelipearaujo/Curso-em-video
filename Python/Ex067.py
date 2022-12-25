#Exercício 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
#digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
#Minha resposta
"""num = 1
while num != 0:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1,11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')"""

#Resposta do professor
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO.')
