print('')
print('='*30)
print('PROGRESSÃO ARITHMETICA ')
print('Veremos os 10 primeiros termos')
print('='*30)
print('')
p=int(input('Digite o primeiro termo:'))
r=int(input('Digite a razão: '))
d= p + (10 - 1) * r
for c in range (p,d+r,r):
    print(c)
