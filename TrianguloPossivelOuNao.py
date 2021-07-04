print('DESAFIO 35')
print('')
print('SERÁ QUE DÁ UM TRIÂNGULO')
r1=float(input('Digite o primeiro comprimento de reta:'))
r2=float(input('Digite o segundo comprimento de reta:'))
r3=float(input('Digite o último comprimento de reta:'))

if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1 +r2:
    print('Com esses valores É POSSÍVEL FORMAR UM TRIÂNGULO!')
else:
    print('Com esses valores NÃO É POSSÍVEL FORMAR UM TRIÂNGULO.')