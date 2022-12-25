#Exercício 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
#Minha resposta
"""resp = 1
maior = homens = mulheres = 0
while resp != 2:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm' or sexo in 'Ff':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres = mulheres + 1
    print('Deseja continuar?\n[1] para continuar\n[2] para sair')
    resp = int(input('Sua opção: '))
    if resp != 1 and resp != 2:
        print('Deseja continuar?\n[1] para continuar\n[2] para sair')
        resp = int(input('Sua opção: '))
    print('')
print(f'Tiveram {maior} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} homens')
print(f'Tivemos {mulheres} mulheres com menos de 20 anos.')
print('Programa finalizado com sucesso!')"""

#Resposta do professor
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF:':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 =+ 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
