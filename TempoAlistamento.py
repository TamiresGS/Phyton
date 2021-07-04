print('')
print('')
from datetime import date
anoatual=date.today().year
print('Saiba se já está na hora de você se alistar')
anonasc=int(input('Que ano você nasceu: (Ex:1998)'))
print('')
idade= anoatual - anonasc
if idade>18:
    print('O tempo de se alistar para o Exército Brasileiro já passou.\nRegularize sua situação.')
elif idade==18: 
    print('Chegou o momento de se alistar\nEntre no site do Exército Brasileiro\nE dê início ao procedimento.')
else:
    print(f'Ainda não chegou a hora de se alistar\nDaqui {18 - idade} anos ao completar 18 anos fique atento\nFaça seu alistamento.')
      
