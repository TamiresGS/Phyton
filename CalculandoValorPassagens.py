print('Desafio 31')
print('')
d=float(input('Qual é a distância em Km da seu destino? '))

if d<=200:
    print('O valor da sua passagem será no valor de R$ {:.2f}'.format(d*0.50))
else:
    print('O valor da sua passagem será no valor de R$ {:.2f}'.format(d*0.45))
