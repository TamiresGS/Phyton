print('===== DESAFIO 11 =====')
print('')
print('Olá está precisando calcular a quantidade de Tinta para pintar sua parede?\nPodemos te ajudar!!!')
print('')
a=float(input('Qual a altura da sua parede em metros:'))
print('')
l=float(input('Qual é a largura da sua parede em metros:'))
print('')
s=a*l
t=s/2
print(f'Sua parede tem {a}×{l} e sua área é de {s}m.')
print('Então você precisará de {} litros de Tinta para pintar sua parede'.format(t))
print('*Já incluso duas camadas de tinta')