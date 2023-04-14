idade = int(input('Digite a sua idade: '))
tempo_serviço = int(input('Qual o tempo de serviço? '))

if idade >= 65:
    print('Pode se aposentar')
elif tempo_serviço >= 30:
    print('Pode se aposentar')
elif idade >= 60 and tempo_serviço >= 25:
    print('Pode se aposentar')
else:
    print('Ainda não pode se aposentar')
 