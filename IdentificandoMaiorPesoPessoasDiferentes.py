print('')
maior=0
menor=0
for c in range (1,8):
    peso=float(input(f'Digite o peso da {c}° pessoa: '))
    if c == 1:
        maior=peso
        menor=peso
    else:
         if peso > maior:
             maior=peso
         if peso < menor:

print('')             menor=peso
print(f'O maior peso lido {maior} Kg')
print(f'E o menor peso lido {menor} Kg') 