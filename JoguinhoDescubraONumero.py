print('DESAFIO 28')
print('')

from random import randint
from time import sleep

computador= randint(0,5)

print('Tente adivinhar')
jogador=int(input('Um número inteiro  de 0 a 5 escolhido pelo computador: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você venceu, PARABÉNS!')
    
else:
    print(f'ERROU,o número escolhido foi {computador} você perdeu')
    
    
