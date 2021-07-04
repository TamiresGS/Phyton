print('')
print('SOMANDO NÚMEROS IMPARES')
print('')
print('Vamos somar todos os números Ímpares\nNo intervalo de 1 até 500')
s = 0
for c in range (1,501):
    if c % 3 == 0 and c % 2 != 0:
       s +=c
print (f'A soma entre os valores é: {s}')