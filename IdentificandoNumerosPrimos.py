print('')
print('=' *30)
print('      NÚMEROS PRIMOS    ')
print('=' *30)
print('')
num=int(input('Digite um número: '))
tot=0
for c in range (1, num + 1):
    if num % c == 0:
    	tot += 1
if tot==2:
    print(f'Esse número é um número primo')
else:
    print(f'Esse número não é um número primo')    
  
         
    
