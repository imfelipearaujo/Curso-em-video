#Exercício 079 - Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = list()
resp = 'S'
while resp != 'N' or resp != 'S':
    if resp == 'S':
        num = (int(input('Digite um valor: ')))
        if num in lista:
            print(f'O número {num} não foi adicionado a lista pois já existe!')
        else:
            lista.append(num)
            print(f'O número {num} foi adicionado a lista!')
        print(f'A sua lista é o momento é: {sorted(lista)}')
        print('-=' * 20)
        print(' ')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print(' ')
    elif resp == 'N':
        break
    else:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print(' ')
print('--' * 20)
print(f'{"Fim do programa":^40}')
print('--' * 20)
print(f'A sua lista ficou da seguinte forma: ')
print(sorted(lista))