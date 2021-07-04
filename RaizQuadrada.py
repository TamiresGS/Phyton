print('Aula08')
print('')

import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz quadrada de {} é igual {}'.format(num,raiz))
print('A raiz quadrada de {} é igual a {}'.format(num,math.ceil(raiz)))
print('A raiz quadrada de {} é igual a {}'.format(num,math.floor(raiz)))
print('A raiz quadrada de {} é igual a {:.2f}'.format(num,raiz))
print('')

from math import sqrt
num=int(input('Digite um número:'))
raiz=sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))
print('')

from math import sqrt,floor
num=int(input('Digite um número:'))
raiz=sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))
