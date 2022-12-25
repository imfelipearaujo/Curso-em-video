#Estrutura de repetição while

'Teoria'
#while é usado quando não sabemos o range
# for = estrutura de repetição com variável de controle
# while = estrutura de repetição com teste lógico

'Prática'
#Usando o FOR
for c in range(1, 10):
    print(c)
print('Fim')
print('=' * 20)
print('')

#Usando o WHILE
c = 1
while c < 10:
    print(c)
    c = c + 1
print('=' * 20)
print('')

#O código irá repetir 4 vezes até parar
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')
print('=' * 20)
print('')

#O código só irá parar quando o usuário digitar 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
print('=' * 20)
print('')

#Resposta sim
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
print('=' * 20)
print('')

#
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} ímpares!'.format(par, impar))