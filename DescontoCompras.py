print('=====Desafio12=====')
print('')
print('Estamos com uma promoção especial para você ')
print('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤')
print('')
print('A primeira compra você ganha 5% de desconto e frete grátis!\nÉ isso mesmo!!!')
print('')
c=float(input('Digite o valor total da sua compra:$'))
d=(c/100)*5
t=c-d
print('Com seu desconto o total a pagar é de:${:.2f}'.format(t))
print('Desconto é de ${:.2f}'.format(d))