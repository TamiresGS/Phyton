print('')
print('')
print('FORMA DE PAGAMENTO')
print('')
compra=float(input('Digite o valor da sua compra: R$ '))
print('')
print('Opções de pagamento ')
print('')

print('[1]Dinheiro')
print('[2]Cartão Débito')
print('[3]Cartão Crédito 1x')
print('[4]Cartão Crédito 2x')
print('[5]Cartão Crédito 3x')
print('')
fp=int(input('Selecione a forma de pagamento:'))
print('')
if fp==1:
   print('O pagamento em Dinheiro libera 10% de desconto')
   print(f'Seu desconto é de R${compra*10/100:.2f}\nTotal a pagar é de R$ {compra-(compra*10/100)}')
elif fp==2:
    print('O pagamento no Débito libera 5% de desconto')
    print(f'Seu desconto é de R${compra*5/100:.2f}\nTotal a pagar é de R${compra- compra*5/100}')
elif fp==3:
    print(f'O valor total a pagar é {compra} ')  
     
elif fp==4:
    print(f'O valor total a pagar é de {compra}')
    print(f'Sendo duas parcelas de {compra/2}')
elif fp==5:
    nv=compra+compra*20/100
    print(f'O pagamento parcelado em 3x ou mais\né cobrado juros de 20%')
    print(f'Sendo juros de R${compra*20/100}\nTotal da compra R${nv}')
    print(f'Sendo três parcelas de R${nv/3}')