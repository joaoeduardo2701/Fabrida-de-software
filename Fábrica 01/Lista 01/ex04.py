num = int(input('Digite um número: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'O número {num} é divisível por 3 e por 5')
elif num % 3 == 0:
    print(f'O número {num} é divisível apenas por 3')
elif num % 5 == 0:
    print(f'O número {num} é divísivel apenas por 5')
else:
    print('Valor inválido')
    