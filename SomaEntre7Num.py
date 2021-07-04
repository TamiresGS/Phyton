print('')
s=0
for c in range (1,7):
    num=int(input(f'Digite o {c} número: '))
    if c % 2 == 0:
       s += c
print('')       
print(f'A soma entre os números pares totaliza:{s}')
    