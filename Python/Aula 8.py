#Aula 8 - Trabalhando com módulos
#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os
#comandos import e from/import no Python. Veja como carregar bibliotecas de
#funções e utilizar vários recursos adicionais nos seus programas utilizando
#módulos built-in e módulos externos, oferecidos no Pypi.

#Duas maneiras de importar bibliotecas no Python
#'import(bebida)' - importa todas as bebidas (generalista)
#from(doce(import(pudim))) - importa apenas o pudim (específico)

#Isso serve para quando você não vai utilizar a biblioteca como um todo, apenas algum item específico dela

#'Biblioteca: math'
#'ceil - arredondamento para cima
#floor - arredondamento para baixo
#trunc - eliminar da vírgula para frente
#pow - potência, funciona similar ao **
#sqrt - raíz quadrada
#factorial - cálculo fatorial

#import math (irá importar tudo)
#from math import sqrt (irá importar somente a raíz quadrada)
#from math import sqrt, ceil (irá importar a raíz quadrada e arredondamento para cima)

#from math import sqrt, floor
#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de {} é igual a {:.2f}!'.format(num, floor(raiz)))

#import random
#num = random.randint(1,10)
#print(num)

import emoji
print(emoji.emojize('Olá, mundo :earth_americas:', use_aliases=True))
