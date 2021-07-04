print('')
print('SITUAÇÕES CREUZA')
print('')
import time
anoatual=int(input('Em que ano estamos?'))
anonasc=int(input('Em que ano você nasceu?'))
idade= anoatual - anonasc

print('Vamos pensar...')
time.sleep (1)
print(f'Então você têm {idade} anos!!!')
print('')
if idade>=30:
    print('A idade está chegando\nSe exercite regularmente!')
    print('')
    atv=int(input('Qual atividade você prefere?\nDigite 1 para Caminhada\nDigite 2 para Pedalar: '))
    if atv == 1:
        print('')
       
        time.sleep(1)
        print('Você sabia que caminhando é possível queimar até 400 calorias por hora.')
        print('Além de benefícios como:\n-Diminuição de inchaço,\n-Previne doenças,\n-Fortace os músculos,\n-Melhora a postura corporal,\n-E promove relaxamento,\n-Dentre outros benefícios...\nEntão comece hoje mesmo!!!')
    else:
        print('')
        print('Sabia que pedalando é possível queimar até 700 calorias por hora, então está esperando o que? Comece hoje mesmo!!!')
        print('Além de benefícios como:')
        print('-Melhora a resistência muscular,\n-Desenvolve o bem-estar,')
        print('-Tem baixo impacto em suas articulações,\n-Reduz o colesterol,')
        print('-Dentre outros benefícios...')
        print('')
    print('Nunca é tarde para cuidar da saúde.')
else:
    print('Cuidado com os excessos, cuide do seu corpo e mente!')
