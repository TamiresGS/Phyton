print('')
print('')
print('Confederação de Natação')
print('')
print('Estamos com vagas abertas\nPara diferentes categorias')
print('')
print('CATEGORIAS     IDADE')
print('Mirim       Até 9 anos ')
print('Infantil    Até 14 anos')
print('Junior      Até 19 anos')
print('Sênior      Até 20 anos')
print('Master      Até 25 anos')
print('')

	   
anonasc=int(input('Informe seu ano de nascimento (Ex:2005): '))
from datetime import date
anoatual=date.today().year
idade=anoatual-anonasc
print(f'Você tem {idade} anos.')

if idade>25:
   print('Infelizmente você não se encaixa em nenhuma das categorias.')
elif idade<=25 and idade>20:
   print('Você pretence a categoria Master')
elif idade<=20 and idade>19:
   print('Você pertence a categoria Sênior')
elif idade<=19 and idade>14:
   print('Você pertence a categoria Júnior')  
elif idade<=14 and idade>9:
    print('Você pertence a categoria Infantil')
else:
    print('Você pertence a categoria Mirim')