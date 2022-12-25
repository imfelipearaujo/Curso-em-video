#Exercício 059 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar | [ 2 ] multiplicar | [ 3 ] maior | [ 4 ] novos números | [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

#Minha resposta
"""from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('Digite uma das opções abaixo para continuar')
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Sua opção: '))

while opcao != 5:
    if opcao == 1:
        print('A soma entre {} e {} é {}!'.format(n1, n2, n1 + n2))
        print('\n')
        sleep(2)
        print('Digite uma das opções abaixo para continuar')
        print('''[ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        opcao = int(input('Sua opção: '))
    elif opcao == 2:
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
        print('\n')
        sleep(2)
        print('Digite uma das opções abaixo para continuar')
        print('''[ 1 ] somar
                [ 2 ] multiplicar
                [ 3 ] maior
                [ 4 ] novos números
                [ 5 ] sair do programa''')
        opcao = int(input('Sua opção: '))
    elif opcao == 3:
        maior = 0
        if n1 > n2 and n2 < n1:
            maior = n1
            print('Entre {} e {}, o número {} é o maior!'.format(n1, n2, maior))
            print('\n')
            sleep(2)
            print('Digite uma das opções abaixo para continuar')
            print('''[ 1 ] somar
                     [ 2 ] multiplicar
                     [ 3 ] maior
                     [ 4 ] novos números
                     [ 5 ] sair do programa''')
            opcao = int(input('Sua opção: '))


        elif n2 > n1 and n1 < n2:
            maior = n2
            print('Entre {} e {}, o número {} é o maior!'.format(n1, n2, maior))
            print('\n')
            sleep(2)
            print('Digite uma das opções abaixo para continuar')
            print('''[ 1 ] somar
                     [ 2 ] multiplicar
                     [ 3 ] maior
                     [ 4 ] novos números
                     [ 5 ] sair do programa''')
            opcao = int(input('Sua opção: '))

        elif n1 == n2 == n1:
            print('Os números são iguais, nenhum é maior.')
            print('\n')
            sleep(2)
            print('Digite uma das opções abaixo para continuar')
            print('''[ 1 ] somar
                     [ 2 ] multiplicar
                     [ 3 ] maior
                     [ 4 ] novos números
                     [ 5 ] sair do programa''')
            opcao = int(input('Sua opção: '))

    elif opcao == 4:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
        print('\n')
        sleep(2)
        print('Digite uma das opções abaixo para continuar')
        print('''[ 1 ] somar
                 [ 2 ] multiplicar
                 [ 3 ] maior
                 [ 4 ] novos números
                 [ 5 ] sair do programa''')
        opcao = int(input('Sua opção: '))
    else:
        print('Opção inválida, Tente novamente.')
        print('\n')
        sleep(2)
        print('Digite uma das opções abaixo para continuar')
        print('''[ 1 ] somar
                 [ 2 ] multiplicar
                 [ 3 ] maior
                 [ 4 ] novos números
                 [ 5 ] sair do programa''')
        opcao = int(input('Sua opção: '))

print('Finalizando...')
sleep(2)
print('Fim do programa! Volte sempre!')'''"""

#resposta do professor
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção  = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')