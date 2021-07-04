print('DESAFIO 29')
print('')

v=float(input('Qual velocidade que seu carro está agora na estrada: '))
if v>80:
    print('Você ultrapassou a velocidade permitida de 80Km/h, você foi multado')
e=(v-80)   
if e>1:
    print(' Você excedeu o limite em {:.1f}Km/h\n O valor da multa é de R$ {:.2f}.'.format(e,e*7))
