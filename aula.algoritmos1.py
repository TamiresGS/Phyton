print('')
print('Empréstimo aprovado com facilidade no pagamento é AQUIIIII!!!')
emprest=float(input('Qual valor que você precisa? '))
taxa=emprest*20/100
tp=taxa+emprest
print('')
print('O valor cobrado é de 20% em cima da quantia solicitada')
print(f'Logo o valor da taxa é de {taxa:.2f}')
print(f'E o total a pagar será de {taxa+emprest:.2f}')
print('')
print('Parcelamos em até 12x sem juros')
parc=int(input	('Deseja realizar o pagamento em quantas vez: '))
qp=tp/parc
print('')
print(f'O total de {parc} vezes, sairá por {qp} mensal')