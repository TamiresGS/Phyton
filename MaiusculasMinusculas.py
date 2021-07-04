print('====DESAFIO====')
print('')
nome=str(input('Digite seu nome completo:')).strip()
print('Maiúsculas : ',nome.upper())
print('Minúsculas : ',nome.lower())

print('Seu nome contém {} letras'.format(len(nome)- nome.count(' ')))

