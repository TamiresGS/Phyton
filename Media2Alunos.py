n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1 + n2)/2
print('A média das suas notas é {:.1f}'.format(m))
if m>=6.0:
    print('Sua nota foi boa, Parabéns!!!')
else:
    print('Sua nota foi ruim, melhore e estude mais!!!')

print('PARABÉNS' if m>=6.0 else 'ESTUDE MAIS')