print('')
print('')

print('VOCÊ SABE O QUE É IMC?')
print('')
print('IMC é a sigla para Índice de Massa Corpórea\nparâmetro adotado pela OMS para calcular o peso ideal de cada pessoa.')
print('')
print('O índice é calculado da seguinte maneira:\nDivide-se o peso do paciente (Kilos)\nPela sua altura  elevada ao quadrado.\nDiz-se que o indivíduo tem peso ideal,\nquando o resultado do IMC está entre 18,5 e\n24,9.') 
print('')
print('Você quer saber o seu IMC?')
print('')
peso=float(input('Digite seu peso (ex:72.5): '))
print('')
altura=float(input('Digite sua altura (ex:1.70): '))
print('')
imc=peso/(altura*altura)
print(f'Seu IMC é {imc:.1f}')
print('')
from time import sleep
sleep(2)
print('Aqui temos a Tabela Classificação')
print('')


print('CLASSIFICAÇÃO            IMC')
print('Abaixo do Peso        Abaixo 18.5')
print('Peso Normal           18.5 - 24,9')
print('Sobrepeso             25.0 - 29.9')
print('Obesidade Grau I      30.0 - 34.9')
print('Obesidade Grau II     35.0 - 39.9')
print('Obesidade Mórbida     Maior  40.0') 
print('')
print('Com base nessa classificação')

if imc<18.5:
    print('Você está abaixo do peso ideal.')
    
elif imc>=18.5 and imc<=24.9:
    print('Você está com o peso ideal.')
    
elif imc>=25 and imc<=29.9:
    print('Você está com sobrepeso.')
    
elif imc>=30 and imc<=34.9:
    print('Você está com Obesidade Grau I.')
    
elif imc>=35 and imc<=39.9:
    print('Você está com Obesidade Grau II.')

elif imc>=40:
    print('Você está com Obesidade Mórbida.')