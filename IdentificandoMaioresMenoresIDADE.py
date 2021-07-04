print('')
from datetime import date
anoatual=date.today().year
print('Digite o ano de nascimento de 7 pessoas\nVamos lá?')
print('')
tmaior=0
tmenor=0

for pess in range(1,8):
   nasc =int(input(f'{pess}° pessoa:  '))
  
   idade = anoatual - nasc
   if idade > 17:
       tmaior += 1 
   else:
        tmenor += 1
print('')        
print(f'Dentre essas pessoas {tmaior} são maiores de idade')
print(f'E {tmenor} pessoas são menores de idade.')