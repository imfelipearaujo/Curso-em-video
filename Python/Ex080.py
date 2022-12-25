#Exercício 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
#em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[len(lista)-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1


print('\n')
print(f'Essa é sua lista: {lista}')
print('\n')
print('Fim do programa')
