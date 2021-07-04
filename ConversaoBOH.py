print('')
print('')
print('Convertendo')
num=int(input('Digite um número: '))
print('''Escolha qual conversão: 
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')
op=int(input('Digite a sua escolha: '))
if op==1:
  print(f'O {num} convertido para Binario é {bin(num)}')
elif op==2:
    print(f'O {num} convertido para Octal é {oct(num)}')
elif op==3:
    print(f' O {num} convertido para Hexadecimal é {hex(num)}')
else:
  print('Opção inexistente')