print('FECHAMENTO DO SEMEMSTRE')

n1=float(input('Digite a sua primeira nota: '))
n2=float(input('Digite a sua segunda nota: '))
m= (n1+n2)/2
print(f'Sua média é {m:.1f}')
if m>=7:
   print('Você foi aprovado! PARABÉNS')
elif m<7 and m>=5:
   print('Você está de RECUPERAÇÃO! SE DEDIQUE')
elif m<5:
   print('Você foi reprovado! ESTUDE MAIS')