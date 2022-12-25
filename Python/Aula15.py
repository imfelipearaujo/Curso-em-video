#Aula 15 - Interrompendo repetições while

'Teoria'
#Lações de Repetição - Parte 3
#break =

'Prática'
"""n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s)) #PEP - fstring
"""
nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.')
print('O {} tem {} anos.'.format(nome, idade))
