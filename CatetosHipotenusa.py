print('====Desafio17====')
print('')

import math
print('Calculando a Hipotenusa de um triângulo retângulo')
co=float(input('Digite a medida do Cateto Oposto:'))
ca=float(input('Agora digite a medida do Cateto adjacente:'))
hi=math.hypot(co,ca)
print('A hipotenusa desse triângulo retângulo{:.3f}'.format(hi)) 