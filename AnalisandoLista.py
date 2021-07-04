print('')
print('ANALISADOR')
print('')
itotal=0
media=0
maiorih=0
hvelho=0
for lista in range (1,5):
    nome=(input(f'Digite o nome da {lista}° pessoa: ')).strip()
    idade=int(input('Digite a idade:'))
    g=str(input('Sexo (F/M): ')).strip()
    print('')
    itotal += idade 
    if lista==1 and g in 'Mm':
        maiorih=idade
        hvelho=nome
    if g in 'Mm' and idade > maiorih :
         maiorih=idade
         hvelho=nome
           

media= itotal /4 
print(f'A média de idade dessas pessoas é de {media} anos')
print(f'O homem mais velho tem {idade} anos e se chama {nome}')

  
