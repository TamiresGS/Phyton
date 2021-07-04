print('')
print('')

resp1=(input('Você sonha com a Casa Própria? ')).lower()
print('')
if resp1=='sim':
    print('Nós podemos te ajudar')
    vcasa = float(input('Digite o valor do Imóvel: R$ '))
    print('')
    vsal = float(input('Digite o valor do seu salário:R$ '))
    print('')
    anospagar=float(input('Em quantos anos deseja pagar: '))
    print('')
    parcelamento = vcasa/(anospagar*12)
    if parcelamento > vsal*30/100:
        print('Não é possível realizar esse financiamento\n pois o valor do Imóvel excede 30% do seu salário.')

    elif parcelamento < vsal*30/100:
        print('Esse sonho pode ser possível!!!\nSeu financiamento foi PRÉ APROVADO!')
       
        print('')
        print(f'O valor do Imóvel sendo {vcasa:.2f}')
        print(f'O parcelamento será em {anospagar:.0f} vezes')
        print(f'O valor das parcelas será de {parcelamento:.2f}')
        
else:
    print('Então deveria pensar nessa forma de empreendimento, querendo ajuda entre em contato conosco.')
      
    
