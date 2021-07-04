print('DESAFIO 34')
print('')

salario=float(input('Informe o salário do funcionário: '))

if salario <= 1250:
    print('O aumento do salário será de 15%, portanto o valor do aumento é de R$ {:.2f}\nO salário atual será R${:.2f} '.format(salario / 100 * 15,salario/100*15+salario))
else:
    print('O aumento do salário será de 10%, portanto o valor do aumento é de R$ {:.2f}\nO salário atual será R${:.2f} '.format(salario/100*10,salario/100*10 +salario))
