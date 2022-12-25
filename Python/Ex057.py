#Exercício 057 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

#Minha resposta
s = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()
masc = 'M'
fem = 'F'
while s != masc or s != fem:
    if s == masc or s == fem:
        print('Sexo {} registrado com sucesso.'.format(s))
    else:
        print('Dados inválidos.', end=' ')
        s = str(input('Por favor, informe seu sexo: ')).strip().upper()
print('Fim')

#Resposta professor
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
