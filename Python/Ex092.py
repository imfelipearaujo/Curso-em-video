"""Exercício 092 - crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
dicionario['idade'] = 2022 - int(input('Ano de Nascimento: '))
dicionario['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dicionario['ctps'] > 0:
    dicionario['contratação'] = int(input('Ano de Contratação: '))
    dicionario['salário'] = float(input('Salário: R$ '))
    dicionario['aposentadoria'] = dicionario['idade'] + 40
    for k, v in dicionario.items():
        print(f'- {k} tem o valor de {v}.')
else:
    for k, v in dicionario.items():
        print(f' - {k} tem o valor de {v}.')

